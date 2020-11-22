-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 22, 2020 at 06:05 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `data`
--

-- --------------------------------------------------------

--
-- Table structure for table `enfermedades`
--

CREATE TABLE `enfermedades` (
  `idEnfermedades` int(100) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `enfermedades`
--

INSERT INTO `enfermedades` (`idEnfermedades`, `nombre`) VALUES
(1, 'resfriado común'),
(2, 'asma'),
(3, 'influenza estacional'),
(4, 'noumonía'),
(5, 'covid-19'),
(6, 'cáncer de pulmón'),
(7, 'faringitis'),
(8, 'enfisema pulmonar'),
(9, 'fibrosis pulmonar'),
(10, 'bronquitis');

-- --------------------------------------------------------

--
-- Table structure for table `intensidad`
--

CREATE TABLE `intensidad` (
  `idIntensidad` int(100) NOT NULL,
  `enfermedadId` int(100) NOT NULL,
  `sintomaId` int(100) NOT NULL,
  `intensidad` decimal(4,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `intensidad`
--

INSERT INTO `intensidad` (`idIntensidad`, `enfermedadId`, `sintomaId`, `intensidad`) VALUES
(1, 1, 1, '0.60'),
(2, 1, 2, '0.85'),
(3, 1, 3, '0.60'),
(4, 1, 4, '0.70'),
(5, 1, 5, '0.45'),
(6, 1, 6, '0.70'),
(7, 1, 7, '0.00'),
(8, 1, 8, '0.20'),
(9, 1, 9, '0.00'),
(10, 1, 10, '0.40'),
(11, 1, 11, '0.00'),
(12, 1, 12, '0.00'),
(13, 1, 13, '0.00'),
(14, 1, 14, '0.75'),
(15, 1, 15, '0.00'),
(16, 1, 16, '0.00'),
(17, 1, 17, '0.20'),
(18, 1, 18, '0.85'),
(19, 2, 1, '0.30'),
(20, 2, 2, '0.75'),
(21, 2, 3, '0.00'),
(22, 2, 4, '0.00'),
(23, 2, 5, '0.15'),
(24, 2, 6, '0.00'),
(25, 2, 7, '0.90'),
(26, 2, 8, '0.00'),
(27, 2, 9, '0.00'),
(28, 2, 10, '0.00'),
(29, 2, 11, '0.00'),
(30, 2, 12, '0.85'),
(31, 2, 13, '0.00'),
(32, 2, 14, '0.95'),
(33, 2, 15, '0.00'),
(34, 2, 16, '0.90'),
(35, 2, 17, '0.85'),
(36, 2, 18, '0.40'),
(37, 3, 1, '0.75'),
(38, 3, 2, '0.30'),
(39, 3, 3, '0.60'),
(40, 3, 4, '0.55'),
(41, 3, 5, '0.80'),
(42, 3, 6, '0.90'),
(43, 3, 7, '0.00'),
(44, 3, 8, '0.90'),
(45, 3, 9, '0.70'),
(46, 3, 10, '0.95'),
(47, 3, 11, '0.65'),
(48, 3, 12, '0.25'),
(49, 3, 13, '0.00'),
(50, 3, 14, '0.30'),
(51, 3, 15, '0.00'),
(52, 3, 16, '0.00'),
(53, 3, 17, '0.35'),
(54, 3, 18, '0.75'),
(55, 4, 1, '0.85'),
(56, 4, 2, '0.80'),
(57, 4, 3, '0.65'),
(58, 4, 4, '0.00'),
(59, 4, 5, '0.00'),
(60, 4, 6, '0.65'),
(61, 4, 7, '0.40'),
(62, 4, 8, '0.75'),
(63, 4, 9, '0.70'),
(64, 4, 10, '0.00'),
(65, 4, 11, '0.70'),
(66, 4, 12, '0.90'),
(67, 4, 13, '0.20'),
(68, 4, 14, '0.20'),
(69, 4, 15, '0.00'),
(70, 4, 16, '0.00'),
(71, 4, 17, '0.65'),
(72, 4, 18, '0.00'),
(73, 5, 1, '0.95'),
(74, 5, 2, '0.95'),
(75, 5, 3, '0.95'),
(76, 5, 4, '0.80'),
(77, 5, 5, '0.75'),
(78, 5, 6, '0.70'),
(79, 5, 7, '0.00'),
(80, 5, 8, '0.95'),
(81, 5, 9, '0.60'),
(82, 5, 10, '0.75'),
(83, 5, 11, '0.30'),
(84, 5, 12, '0.45'),
(85, 5, 13, '0.00'),
(86, 5, 14, '0.00'),
(87, 5, 15, '0.00'),
(88, 5, 16, '0.00'),
(89, 5, 17, '0.70'),
(90, 5, 18, '0.80'),
(91, 6, 1, '0.90'),
(92, 6, 2, '0.85'),
(93, 6, 3, '0.00'),
(94, 6, 4, '0.00'),
(95, 6, 5, '0.70'),
(96, 6, 6, '0.00'),
(97, 6, 7, '0.00'),
(98, 6, 8, '0.75'),
(99, 6, 9, '0.00'),
(100, 6, 10, '0.00'),
(101, 6, 11, '0.00'),
(102, 6, 12, '0.90'),
(103, 6, 13, '1.00'),
(104, 6, 14, '0.90'),
(105, 6, 15, '1.00'),
(106, 6, 16, '0.00'),
(107, 6, 17, '0.55'),
(108, 6, 18, '0.00'),
(109, 7, 1, '0.80'),
(110, 7, 2, '0.85'),
(111, 7, 3, '0.75'),
(112, 7, 4, '0.10'),
(113, 7, 5, '0.90'),
(114, 7, 6, '0.70'),
(115, 7, 7, '0.00'),
(116, 7, 8, '0.00'),
(117, 7, 9, '0.00'),
(118, 7, 10, '0.75'),
(119, 7, 11, '0.00'),
(120, 7, 12, '0.65'),
(121, 7, 13, '0.00'),
(122, 7, 14, '0.10'),
(123, 7, 15, '0.00'),
(124, 7, 16, '0.00'),
(125, 7, 17, '0.30'),
(126, 7, 18, '0.45'),
(127, 8, 1, '0.80'),
(128, 8, 2, '1.00'),
(129, 8, 3, '0.00'),
(130, 8, 4, '0.00'),
(131, 8, 5, '0.20'),
(132, 8, 6, '0.00'),
(133, 8, 7, '0.00'),
(134, 8, 8, '0.80'),
(135, 8, 9, '0.00'),
(136, 8, 10, '0.00'),
(137, 8, 11, '0.00'),
(138, 8, 12, '0.90'),
(139, 8, 13, '0.20'),
(140, 8, 14, '0.55'),
(141, 8, 15, '0.70'),
(142, 8, 16, '0.90'),
(143, 8, 17, '0.80'),
(144, 8, 18, '0.00'),
(145, 9, 1, '0.80'),
(146, 9, 2, '0.95'),
(147, 9, 3, '0.00'),
(148, 9, 4, '0.00'),
(149, 9, 5, '0.35'),
(150, 9, 6, '0.20'),
(151, 9, 7, '0.00'),
(152, 9, 8, '0.85'),
(153, 9, 9, '0.00'),
(154, 9, 10, '0.90'),
(155, 9, 11, '0.00'),
(156, 9, 12, '0.55'),
(157, 9, 13, '0.00'),
(158, 9, 14, '0.20'),
(159, 9, 15, '0.95'),
(160, 9, 16, '0.00'),
(161, 9, 17, '0.30'),
(162, 9, 18, '0.00'),
(163, 10, 1, '0.85'),
(164, 10, 2, '0.90'),
(165, 10, 3, '0.75'),
(166, 10, 4, '0.00'),
(167, 10, 5, '0.35'),
(168, 10, 6, '0.00'),
(169, 10, 7, '0.00'),
(170, 10, 8, '0.85'),
(171, 10, 9, '0.00'),
(172, 10, 10, '0.55'),
(173, 10, 11, '0.00'),
(174, 10, 12, '0.90'),
(175, 10, 13, '0.65'),
(176, 10, 14, '0.45'),
(177, 10, 15, '0.00'),
(178, 10, 16, '0.00'),
(179, 10, 17, '0.75'),
(180, 10, 18, '0.70');

-- --------------------------------------------------------

--
-- Table structure for table `sintoma`
--

CREATE TABLE `sintoma` (
  `idSintoma` int(100) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `sintoma`
--

INSERT INTO `sintoma` (`idSintoma`, `nombre`) VALUES
(1, 'tos'),
(2, 'dificultad para respirar'),
(3, 'fiebre'),
(4, 'estornudos'),
(5, 'dolor de garganta'),
(6, 'dolor de cabeza'),
(7, 'confusión'),
(8, 'fatiga'),
(9, 'diarrea'),
(10, 'dolor corporal/muscular'),
(11, 'nausea/vómito'),
(12, 'dolor de pecho'),
(13, 'sangre en el esputo'),
(14, 'sabilancias'),
(15, 'pérdida de peso sin causa aparente'),
(16, 'coloración azulada en la piel'),
(17, 'problemas para dormir'),
(18, 'congestión/goteo nasal');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `enfermedades`
--
ALTER TABLE `enfermedades`
  ADD PRIMARY KEY (`idEnfermedades`);

--
-- Indexes for table `intensidad`
--
ALTER TABLE `intensidad`
  ADD PRIMARY KEY (`idIntensidad`);

--
-- Indexes for table `sintoma`
--
ALTER TABLE `sintoma`
  ADD PRIMARY KEY (`idSintoma`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
