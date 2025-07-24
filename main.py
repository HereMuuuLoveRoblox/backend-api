from fastapi import FastAPI , Depends
from database import connect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database import users as MUsers
from database import token as JWTTOKEN

class UserRegister(BaseModel):
    userName: str
    password: str
    confirmPassword: str
    email: str
    personnelId: str
    
class UserLogin(BaseModel):
    email: str
    password: str
    

# Connect Database
conn = connect.ConnectDB()

origins = [
    "http://localhost:3000",   # สำหรับ frontend React/Vue dev
    "https://yourfrontend.com" # สำหรับ production
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/users/register")
async def post_user_register(data: UserRegister):
    try:
        response = MUsers.userRegister(conn, data)
        return response
    
    except Exception as e:
        return {"Error": str(e)}

@app.post("/users/login")
async def post_user_login(data: UserLogin):
    try:
        response = MUsers.userLogin(conn, data)
        return response
    
    except Exception as e:
        return {"Error": str(e)}

@app.get("/users/getuserall")
async def get_user_all(user_data: dict = Depends(JWTTOKEN.verify_token)):
    
    if user_data['role'] == "user":
        return {"status": "error", "message": "user is not admin"}
    
    try:
        response = MUsers.getUserAll(conn)
        return response
    except Exception as e:
        return {"Error": str(e)}

@app.get("/users/getuserId/{userId}")
async def get_user_by_id(userId: int, user_data: dict = Depends(JWTTOKEN.verify_token)):
    try:

        if user_data['role'] == "user":
            return {"status": "error", "message": "user is not admin"}

        response = MUsers.getUserByUserID(conn, userId)
        return response
    
    except Exception as e:
        return {"Error": str(e)}

@app.put("/users/update/password/{userId}/{old_password}/{new_password}")
async def put_change_password(userId: int, password: str,new_password: str, user_data: dict = Depends(JWTTOKEN.verify_token)):
    try:
        
        response = MUsers.updateUserPassword(conn, userId , password, new_password)
        return response
    
    except Exception as e:
        return {"Error": str(e)}

