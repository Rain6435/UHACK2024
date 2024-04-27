-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 27, 2024 at 10:35 PM
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
-- Database: `uhack2024`
--

DROP DATABASE IF EXISTS uhack2024;
CREATE DATABASE uhack2024;
USE uhack2024;

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `id` int(10) NOT NULL,
  `location` text NOT NULL,
  `adresse` varchar(100) NOT NULL,
  `team_id` int(10) DEFAULT NULL,
  `is_dangerous` tinyint(1) NOT NULL,
  `creation_date` date NOT NULL,
  `lead_time` date DEFAULT NULL,
  `fix_date` date DEFAULT NULL,
  `status` varchar(45) NOT NULL,
  `image` text DEFAULT NULL,
  `requestor_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `requestor`
--

CREATE TABLE `requestor` (
  `id` int(10) NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `adresse` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `tel` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `requestor`
--

INSERT INTO `requestor` (`id`, `firstname`, `lastname`, `adresse`, `email`, `tel`) VALUES
(8, 'John', 'Doe', '123 rue abc', NULL, NULL),
(9, 'Emily', 'Brown', '123 rue abc', 'emilybrown@abc.com', '6131239988');

-- --------------------------------------------------------

--
-- Table structure for table `team`
--

CREATE TABLE `team` (
  `id` int(10) NOT NULL,
  `name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `work_time` varchar(1) NOT NULL,
  `work_season` varchar(1) NOT NULL,
  `secteur` varchar(45) DEFAULT NULL,
  `is_admin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `team`
--

INSERT INTO `team` (`id`, `name`, `password`, `work_time`, `work_season`, `secteur`, `is_admin`) VALUES
(6, 'hull1', 'root', 'J', 'A', NULL, 0),
(7, 'hull2', 'root', 'J', 'A', 'Hull', 0),
(8, 'aylmer1', 'root', 'J', 'A', 'Aylmer', 1),
(9, 'aylmer2', 'root', 'N', 'A', 'Aylmer', 0),
(10, 'contracteur1', 'root', 'J', 'A', NULL, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `foreign_key_team_teamID` (`team_id`),
  ADD KEY `foreign_key_requestor_requestorID` (`requestor_id`);

--
-- Indexes for table `requestor`
--
ALTER TABLE `requestor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UNIQUE_PERSON` (`firstname`,`lastname`,`adresse`);

--
-- Indexes for table `team`
--
ALTER TABLE `team`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `requestor`
--
ALTER TABLE `requestor`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `team`
--
ALTER TABLE `team`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `request`
--
ALTER TABLE `request`
  ADD CONSTRAINT `foreign_key_requestor_requestorID` FOREIGN KEY (`requestor_id`) REFERENCES `requestor` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `foreign_key_team_teamID` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
