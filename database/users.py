import sqlite3
from jose import jwt
from datetime import datetime, timedelta
import bcrypt
import os

from database import token as JWTTOKEN

def CheckEmailandPersonnelIdinSQL(conn, data):
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM users WHERE email = ? OR personnelId = ?", (data.email, data.personnelId))
    existing_user = mycursor.fetchone()
    mycursor.close()

    if existing_user:
        return {"status": "error", "message": "Username or Email already exists"}
    
    return None  # ✅ ถ้าไม่ซ้ำ ส่ง None กลับ
        
    
# Register
def userRegister(conn, data):
    try:
        conflict = CheckEmailandPersonnelIdinSQL(conn, data)
        if conflict:
            return conflict  # ถ้ามีปัญหาเรื่องซ้ำก็ return ออกทันที
        
        # Check Password is Match
        if data.password != data.confirmPassword:
            return {"status": "error", "message": "Passwords do not match"}
        
        # Username least 8 characters
        if len(data.userName) < 8:
            return {"status": "error", "message": "Username must be at least 8 characters long"}
        
        # hash password
        hashed_password = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())
        
        mycursor = conn.cursor()
        query = """
            INSERT INTO users (userName, password, email, personnelId)
            VALUES (?, ?, ?, ?)
        """
        values = (
            data.userName,
            hashed_password,
            data.email,
            data.personnelId,
        )

        mycursor.execute(query, values)
        conn.commit()  # ✅ commit เพื่อบันทึกลง DB

        mycursor.close()
        return {"status": "success", 
                "message": "User Register Success.",
                "response": "User Registered"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

def userLogin(conn, data):
    try:
        mycursor = conn.cursor()
        sql = "SELECT userId, password, email, role FROM users WHERE email = ?"
        mycursor.execute(sql, (data.email,))
        
        # เช็คว่ามี Email นี้ อยู่จริง
        user = mycursor.fetchone()
        
        # เช็คว่า ทีอีเมล และ Password ที่กรอก ตรงกับ Password ใน SQL
        # ก่อนเช็ค ต้อง hash แล้วค่อยเช็ค
        if user and bcrypt.checkpw(data.password.encode('utf-8'), user['password']):
            token = JWTTOKEN.create_access_token({"userId": user['userId'],
                                                  "role": user['role']})
            
            # ส่งข้อมูล Success Token ในรูปแบบ JSON
            return {
                "status": "success",
                "message": "User Login Success.",
                "response": {"token": token,
                             "userId": user['userId'],
                             "role": user['role']
                            }
                
            }
        # not user / password Invalid
        return {
            "status": "error",
            "message": "Invalid email or password"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    finally:
        mycursor.close()
        
def getUserByUserID(conn, userId):
    try:
        mycursor = conn.cursor()
        mycursor.execute(f'SELECT userName, email, personnelId, role FROM users WHERE userId = {userId}')
        myresult = mycursor.fetchone()
        
        if not myresult:
            return {
                "status": "error",
                "message": f"User {userId} Dont have In database.",
        }
        return {
                "status": "success",
                "message": f"Get User {userId} Success.",
                "response": myresult
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def getUserAll(conn):
    try:
        mycursor = conn.cursor()
        mycursor.execute(f'SELECT userId, userName, email, personnelId, role FROM users')
        myresult = mycursor.fetchall()
        
        if not myresult:
            return {
                "status": "error",
                "message": "Dont have Users In Database.",
        }
        return {
            "status": "success",
            "message": "Get All User Success.",
            "count": len(myresult),
            "response": myresult
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
