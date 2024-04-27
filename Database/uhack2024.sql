-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 27, 2024 at 07:04 PM
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
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `MUNID` int(10) DEFAULT NULL,
  `CODE_ID` int(10) NOT NULL,
  `SEGMENT` varchar(45) DEFAULT NULL,
  `TYPE` varchar(45) DEFAULT NULL,
  `GENERIQUE` varchar(45) DEFAULT NULL,
  `LIAISON` varchar(45) DEFAULT NULL,
  `SPECIFIQUE` varchar(45) DEFAULT NULL,
  `DIRECTION` varchar(45) DEFAULT NULL,
  `NOM_TOPO` varchar(45) DEFAULT NULL,
  `COTE` varchar(45) DEFAULT NULL,
  `ORIENTATION` varchar(45) DEFAULT NULL,
  `DIREC_UNIQ` varchar(45) DEFAULT NULL,
  `CIV_GAU_DE` int(11) DEFAULT NULL,
  `CIV_GAU_A` int(11) DEFAULT NULL,
  `CIV_DRT_DE` int(11) DEFAULT NULL,
  `CIV_DRT_A` int(11) DEFAULT NULL,
  `LIMITE_VIT` int(11) DEFAULT NULL,
  `HIERARCHIE` int(11) NOT NULL,
  `ENTITEID` varchar(45) NOT NULL,
  `GEOM` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`MUNID`, `CODE_ID`, `SEGMENT`, `TYPE`, `GENERIQUE`, `LIAISON`, `SPECIFIQUE`, `DIRECTION`, `NOM_TOPO`, `COTE`, `ORIENTATION`, `DIREC_UNIQ`, `CIV_GAU_DE`, `CIV_GAU_A`, `CIV_DRT_DE`, `CIV_DRT_A`, `LIMITE_VIT`, `HIERARCHIE`, `ENTITEID`, `GEOM`) VALUES
(NULL, 8047, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, 'abc', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `id` int(10) NOT NULL,
  `location_id` int(10) NOT NULL,
  `team_id` int(10) NOT NULL,
  `is_dangerous` tinyint(1) NOT NULL,
  `creation_date` date NOT NULL,
  `lead_time` date NOT NULL,
  `fix_date` date DEFAULT NULL,
  `status` varchar(45) NOT NULL,
  `image_path` text DEFAULT NULL,
  `requestor_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `request`
--

INSERT INTO `request` (`id`, `location_id`, `team_id`, `is_dangerous`, `creation_date`, `lead_time`, `fix_date`, `status`, `image_path`, `requestor_id`) VALUES
(1, 8047, 10, 1, '2024-04-27', '2024-04-30', NULL, 'PENDING', NULL, 8),
(2, 8047, 10, 1, '2024-04-27', '2024-04-30', NULL, 'PENDING', NULL, 8);

-- --------------------------------------------------------

--
-- Table structure for table `requestor`
--

CREATE TABLE `requestor` (
  `id` int(10) NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `adresse` varchar(45) NOT NULL,
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
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`CODE_ID`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `foreign_key_location_codeID` (`location_id`),
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
  ADD CONSTRAINT `foreign_key_location_codeID` FOREIGN KEY (`location_id`) REFERENCES `location` (`CODE_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `foreign_key_requestor_requestorID` FOREIGN KEY (`requestor_id`) REFERENCES `requestor` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `foreign_key_team_teamID` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
