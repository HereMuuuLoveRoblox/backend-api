-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2025 at 06:03 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `classroomdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `classroom`
--

CREATE TABLE `classroom` (
  `roomId` int(11) NOT NULL,
  `roomNumber` varchar(20) NOT NULL,
  `roomStatus` tinyint(1) DEFAULT 0,
  `capacity` int(11) DEFAULT NULL,
  `osType` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `classroom`
--

INSERT INTO `classroom` (`roomId`, `roomNumber`, `roomStatus`, `capacity`, `osType`) VALUES
(14, '2233', 1, 40, 'Windows'),
(15, '2234', 1, 35, 'Mac'),
(16, '2221', 1, 40, '-'),
(17, '2212', 0, 40, '-'),
(18, '2213', 1, 40, 'Mac'),
(19, '2214', 1, 40, 'Mac'),
(20, '2235', 1, 40, 'linux'),
(21, '2236', 1, 40, 'Mac,Windows'),
(22, '2241', 1, 40, 'Mac'),
(23, '2242', 1, 50, 'Mac,Windows'),
(24, '2243', 1, 9, 'Mac'),
(25, '22243', 1, 20, '-'),
(26, '1', 0, 40, 'Mac'),
(27, '88', 1, 8, 'Mac');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userId` int(11) NOT NULL,
  `userName` varchar(20) NOT NULL,
  `password` varchar(256) NOT NULL,
  `email` varchar(128) NOT NULL,
  `personnelId` varchar(128) DEFAULT NULL,
  `role` varchar(20) DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userId`, `userName`, `password`, `email`, `personnelId`, `role`) VALUES
(1, 'Anupat Jinda', '$2b$12$naLNmqMGJ03N9rA.a0PFjuUqrK.Bo7ErQRGwUvkZCiWbcHrzutfUS', 'AnupatJinda@gmail.com', '123456789', 'user'),
(3, 'Jittakorn Kabsan', '$2b$12$3AT6YXaEevEcYLuniNihleGw1PIvwONaToKvWfu5EOpn2rwMleeFa', 'JittakornKabsan@gmail.com', '123456789', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `classroom`
--
ALTER TABLE `classroom`
  ADD PRIMARY KEY (`roomId`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userId`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `classroom`
--
ALTER TABLE `classroom`
  MODIFY `roomId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
