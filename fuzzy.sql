-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 21, 2018 at 08:26 AM
-- Server version: 5.7.21-0ubuntu0.16.04.1
-- PHP Version: 7.0.28-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fuzzy`
--

-- --------------------------------------------------------

--
-- Table structure for table `BatasHimp`
--

CREATE TABLE `BatasHimp` (
  `Batas` varchar(15) NOT NULL,
  `Nilai` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `DataHP`
--

CREATE TABLE `DataHP` (
  `Type` varchar(10) NOT NULL,
  `Kode` int(11) DEFAULT NULL,
  `Harga` double DEFAULT NULL,
  `P` double DEFAULT NULL,
  `L` double DEFAULT NULL,
  `T` double DEFAULT NULL,
  `Berat` double DEFAULT NULL,
  `StandBy` double DEFAULT NULL,
  `TalkTime` double DEFAULT NULL,
  `PhoneBook` int(11) DEFAULT NULL,
  `VoiceDailing` int(11) DEFAULT NULL,
  `Games` int(11) DEFAULT NULL,
  `MessegeLength` int(11) DEFAULT NULL,
  `WAP` tinyint(1) DEFAULT NULL,
  `GPRS` tinyint(1) DEFAULT NULL,
  `Infrared` tinyint(1) DEFAULT NULL,
  `MMS` tinyint(1) DEFAULT NULL,
  `PolyPhonic` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DataHP`
--

INSERT INTO `DataHP` (`Type`, `Kode`, `Harga`, `P`, `L`, `T`, `Berat`, `StandBy`, `TalkTime`, `PhoneBook`, `VoiceDailing`, `Games`, `MessegeLength`, `WAP`, `GPRS`, `Infrared`, `MMS`, `PolyPhonic`) VALUES
('6898', 1, 210, 235, 80, 40, 82, 170, 150, 50, 0, 3, 150, NULL, NULL, NULL, NULL, NULL),
('A3618', 2, 725, 111, 47, 22, 86, 180, 240, 100, 0, 4, 160, NULL, NULL, NULL, NULL, NULL),
('A50', 3, 60, 109, 46, 23, 97, 250, 300, 50, 0, 2, 760, NULL, NULL, NULL, NULL, NULL),
('C35', 3, 70, 118, 46, 22, 116, 180, 300, 199, 0, 4, 160, NULL, NULL, NULL, NULL, NULL),
('C45', 3, 73, 109, 46, 23, 107, 200, 300, 50, 0, 4, 760, NULL, NULL, NULL, NULL, NULL),
('CL50', 3, 250, 73, 39, 22, 79, 200, 300, 500, 0, 4, 760, NULL, NULL, NULL, NULL, NULL),
('CMD J5', 4, 144, 144, 46, 19.5, 81, 150, 360, 500, 0, 0, 160, NULL, NULL, NULL, NULL, NULL),
('CMD J6', 4, 125, 144, 46, 19.5, 81, 150, 360, 500, 0, 4, 160, NULL, NULL, NULL, NULL, NULL),
('CMD Z7', 4, 205, 91, 50, 25, 90, 216, 480, 500, 10, 4, 160, NULL, NULL, NULL, NULL, NULL),
('Fisio 620', 5, 120, 104, 46, 20, 85, 330, 285, 300, 10, 3, 250, NULL, NULL, NULL, NULL, NULL),
('LG W 5200', 6, 250, 84, 45, 19.5, 80, 120, 240, 200, 10, 5, 1000, NULL, NULL, NULL, NULL, NULL),
('LG510W', 6, 235, 82.3, 45, 19.5, 79, 200, 160, 200, 10, 5, 1000, NULL, NULL, NULL, NULL, NULL),
('M35', 3, 80, 118, 46, 21, 130, 180, 300, 200, 0, 4, 160, NULL, NULL, NULL, NULL, NULL),
('Mars', 8, 70, 115, 44, 29, 115, 130, 180, 100, 0, 3, 150, NULL, NULL, NULL, NULL, NULL),
('MC 920', 7, 49, 116.5, 45.5, 18.5, 117, 130, 180, 100, 0, 0, 160, NULL, NULL, NULL, NULL, NULL),
('MC 922', 7, 45, 116, 45.5, 22, 125, 150, 180, 100, 0, 0, 160, NULL, NULL, NULL, NULL, NULL),
('ME45', 3, 180, 109, 46, 21, 99, 300, 300, 500, 10, 4, 760, NULL, NULL, NULL, NULL, NULL),
('N3310', 9, 101.5, 113, 48, 22, 133, 355, 55, 250, 8, 4, 460, NULL, NULL, NULL, NULL, NULL),
('N3315', 9, 127.5, 113, 48, 22, 114, 260, 240, 100, 0, 0, 460, NULL, NULL, NULL, NULL, NULL),
('N3330', 9, 85, 113, 48, 22, 107, 245, 155, 100, 8, 4, 460, NULL, NULL, NULL, NULL, NULL),
('N3350', 9, 92.5, 113.7, 48.8, 22.8, 108, 260, 225, 250, 10, 3, 460, NULL, NULL, NULL, NULL, NULL),
('N3510', 9, 120, 118, 41.8, 18, 106, 312, 270, 500, 14, 6, 460, NULL, NULL, NULL, NULL, NULL),
('N3610', 9, 120, 104, 44.5, 21, 91.5, 170, 230, 150, 10, 6, 450, NULL, NULL, NULL, NULL, NULL),
('N5210', 9, 130, 105.5, 47.5, 22.5, 92, 170, 250, 250, 10, 5, 460, NULL, NULL, NULL, NULL, NULL),
('N5510', 9, 115, 134, 58, 28, 155, 260, 270, 250, 10, 5, 450, NULL, NULL, NULL, NULL, NULL),
('N6100', 9, 500, 102, 44, 13.5, 76, 320, 360, 500, 10, 5, 160, NULL, NULL, NULL, NULL, NULL),
('N6310', 9, 225, 129, 49, 130, 130, 480, 180, 500, 10, 4, 460, NULL, NULL, NULL, NULL, NULL),
('N6510', 9, 240, 97, 43, 20, 85, 288, 210, 500, 10, 4, 400, NULL, NULL, NULL, NULL, NULL),
('N7210', 9, 320, 106, 45, 17.5, 83, 300, 300, 500, 10, 4, 400, NULL, NULL, NULL, NULL, NULL),
('N8210', 9, 180, 102, 45, 17, 79, 150, 180, 250, 10, 5, 160, NULL, NULL, NULL, NULL, NULL),
('N8250', 9, 180, 102.5, 19, 5, 81, 150, 210, 250, 10, 5, 160, NULL, NULL, NULL, NULL, NULL),
('N8310', 9, 260, 97, 43, 17, 84, 150, 240, 500, 10, 3, 150, NULL, NULL, NULL, NULL, NULL),
('N8850', 9, 300, 100, 44, 17, 91, 225, 170, 250, 10, 5, 160, NULL, NULL, NULL, NULL, NULL),
('N8855', 9, 445, 102, 46, 21, 98, 225, 255, 250, 10, 5, 165, NULL, NULL, NULL, NULL, NULL),
('N8910', 9, 600, 103, 46, 20, 110, 300, 180, 500, 10, 4, 160, NULL, NULL, NULL, NULL, NULL),
('N9210', 9, 600, 158, 56, 27, 244, 230, 600, 250, 10, 5, 500, NULL, NULL, NULL, NULL, NULL),
('P800', 10, 625, 117, 59, 27, 108, 400, 780, 510, 25, 10, 160, NULL, NULL, NULL, NULL, NULL),
('R220', 11, 82.5, 110, 48, 22, 99, 60, 100, 100, 0, 3, 160, NULL, NULL, NULL, NULL, NULL),
('R310', 2, 80, 131, 53, 25, 170, 160, 270, 99, 10, 4, 160, NULL, NULL, NULL, NULL, NULL),
('R600', 2, 80, 105, 45, 20, 82, 150, 240, 200, 0, 4, 160, NULL, NULL, NULL, NULL, NULL),
('S35', 3, 80, 118, 46, 21, 105, 220, 360, 200, 10, 4, 160, NULL, NULL, NULL, NULL, NULL),
('S45', 3, 190, 109, 46, 20, 93, 300, 360, 500, 10, 4, 760, NULL, NULL, NULL, NULL, NULL),
('SG 2000', 12, 250, 65, 37, 20, 70, 170, 210, 250, 0, 0, 160, NULL, NULL, NULL, NULL, NULL),
('SGH-A100', 11, 80, 80, 42, 22.9, 87, 70, 180, 99, 10, 5, 250, NULL, NULL, NULL, NULL, NULL),
('SGH-A300', 11, 279.9, 81, 42, 22, 83, 80, 240, 99, 0, 7, 250, NULL, NULL, NULL, NULL, NULL),
('SGH-N200', 11, 178, 110, 46, 23, 95, 120, 210, 200, 0, 11, 250, NULL, NULL, NULL, NULL, NULL),
('SGH-N400', 11, 200, 112, 45, 18, 91, 150, 360, 250, 0, 5, 250, NULL, NULL, NULL, NULL, NULL),
('SL45', 3, 280, 105, 42, 17, 88, 170, 240, 2000, 20, 4, 760, NULL, NULL, NULL, NULL, NULL),
('T100', 10, 110, 99, 43.5, 17.7, 75, 200, 270, 100, 10, 5, 960, NULL, NULL, NULL, NULL, NULL),
('T190', 13, 75, 106, 40, 15, 101, 101, 120, 300, 0, 3, 765, NULL, NULL, NULL, NULL, NULL),
('T20', 2, 80, 101, 54, 28, 128, 200, 600, 199, 10, 4, 160, NULL, NULL, NULL, NULL, NULL),
('T200', 2, 130, 105, 48, 20, 85, 220, 780, 300, 0, 5, 960, NULL, NULL, NULL, NULL, NULL),
('T29s', 2, 90, 101, 49, 29, 95, 150, 420, 250, 10, 4, 160, NULL, NULL, NULL, NULL, NULL),
('T39s', 2, 180, 90, 50, 18, 86, 504, 1500, 510, 10, 4, 160, NULL, NULL, NULL, NULL, NULL),
('T65', 2, 140, 105, 49, 22, 94, 300, 600, 300, 10, 2, 160, NULL, NULL, NULL, NULL, NULL),
('T66', 2, 160, 92, 41, 17.5, 59, 200, 300, 100, 10, 3, 160, NULL, NULL, NULL, NULL, NULL),
('T68', 2, 410, 100, 48, 20, 84, 290, 780, 300, 0, 3, 250, NULL, NULL, NULL, NULL, NULL),
('T68i', 10, 355, 100, 48, 20, 85, 390, 720, 510, 10, 8, 1530, NULL, NULL, NULL, NULL, NULL),
('V+3688', 13, 110, 130, 46, 24.5, 80, 100, 210, 100, 10, 4, 160, NULL, NULL, NULL, NULL, NULL),
('Z700', 10, 225, 91, 50, 24, 95, 200, 480, 510, 5, 4, 160, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `JenisHP`
--

CREATE TABLE `JenisHP` (
  `Kode` int(11) NOT NULL,
  `NamaHP` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `JenisHP`
--

INSERT INTO `JenisHP` (`Kode`, `NamaHP`) VALUES
(1, 'TCL'),
(2, 'Ericsson'),
(3, 'Seimens'),
(4, 'Sony'),
(5, 'Philips'),
(6, 'LG'),
(7, 'Sagem'),
(8, 'Trium'),
(9, 'Nokia'),
(10, 'Sony Ericsson'),
(11, 'Samsung'),
(12, 'Nixxo'),
(13, 'Motorola');

-- --------------------------------------------------------

--
-- Table structure for table `karyawan`
--

CREATE TABLE `karyawan` (
  `nip` varchar(2) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `umur` int(11) DEFAULT NULL,
  `masakerja` double DEFAULT NULL,
  `gaji` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `karyawan`
--

INSERT INTO `karyawan` (`nip`, `nama`, `umur`, `masakerja`, `gaji`) VALUES
('01', 'Lia', 30, 6, 750000),
('02', 'Iwan', 48, 17, 1500000),
('03', 'Sari', 36, 14, 1255000),
('04', 'Andi', 37, 4, 1040000),
('05', 'Budi', 42, 12, 950000),
('06', 'Amir', 39, 13, 1600000),
('07', 'Rian', 37, 5, 1250000),
('08', 'Kiki', 32, 1, 550000),
('09', 'Alda', 35, 3, 735000),
('10', 'Yoga', 25, 2, 860000);

-- --------------------------------------------------------

--
-- Table structure for table `Mu`
--

CREATE TABLE `Mu` (
  `Type` varchar(15) DEFAULT NULL,
  `MHarga1` double DEFAULT NULL,
  `MHarga2` double DEFAULT NULL,
  `MHarga3` double DEFAULT NULL,
  `MSize1` double DEFAULT NULL,
  `MSize2` double DEFAULT NULL,
  `MSize3` double DEFAULT NULL,
  `MBerat1` double DEFAULT NULL,
  `MBerat2` double DEFAULT NULL,
  `MBerat3` double DEFAULT NULL,
  `MStandBy1` double DEFAULT NULL,
  `MStandBy2` double DEFAULT NULL,
  `MStandBy3` double DEFAULT NULL,
  `MTalkTime1` double DEFAULT NULL,
  `MTalkTime2` double DEFAULT NULL,
  `MTalkTime3` double DEFAULT NULL,
  `MPhoneBook1` double DEFAULT NULL,
  `MPhoneBook2` double DEFAULT NULL,
  `MPhoneBook3` double DEFAULT NULL,
  `MVoiceDialing1` double DEFAULT NULL,
  `MVoiceDialing2` double DEFAULT NULL,
  `MVoiceDialing3` double DEFAULT NULL,
  `MGames1` double DEFAULT NULL,
  `MGames2` double DEFAULT NULL,
  `MGames3` double DEFAULT NULL,
  `MMessageLength1` double DEFAULT NULL,
  `MMessageLength2` double DEFAULT NULL,
  `MMessageLength3` double DEFAULT NULL,
  `MHarga` double DEFAULT NULL,
  `MSize` double DEFAULT NULL,
  `MBerat` double DEFAULT NULL,
  `MStandBy` double DEFAULT NULL,
  `MTalkTime` double DEFAULT NULL,
  `MPhoneBook` double DEFAULT NULL,
  `MVoiceDialing` double DEFAULT NULL,
  `MGames` double DEFAULT NULL,
  `MMessageLength` double DEFAULT NULL,
  `MWAP` double DEFAULT NULL,
  `MGPRS` double DEFAULT NULL,
  `MInfrared` double DEFAULT NULL,
  `MMMS` double DEFAULT NULL,
  `MPolyPhonic` double DEFAULT NULL,
  `Mu` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `BatasHimp`
--
ALTER TABLE `BatasHimp`
  ADD PRIMARY KEY (`Batas`);

--
-- Indexes for table `DataHP`
--
ALTER TABLE `DataHP`
  ADD PRIMARY KEY (`Type`),
  ADD KEY `Kode` (`Kode`);

--
-- Indexes for table `JenisHP`
--
ALTER TABLE `JenisHP`
  ADD PRIMARY KEY (`Kode`);

--
-- Indexes for table `karyawan`
--
ALTER TABLE `karyawan`
  ADD PRIMARY KEY (`nip`);

--
-- Indexes for table `Mu`
--
ALTER TABLE `Mu`
  ADD KEY `Type` (`Type`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `DataHP`
--
ALTER TABLE `DataHP`
  ADD CONSTRAINT `DataHP_ibfk_1` FOREIGN KEY (`Kode`) REFERENCES `JenisHP` (`Kode`);

--
-- Constraints for table `Mu`
--
ALTER TABLE `Mu`
  ADD CONSTRAINT `Mu_ibfk_1` FOREIGN KEY (`Type`) REFERENCES `DataHP` (`Type`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
