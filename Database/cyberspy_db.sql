-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 03, 2023 at 03:32 PM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cyberspy_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `attack_table`
--

CREATE TABLE IF NOT EXISTS `attack_table` (
  `attack_id` int(11) NOT NULL AUTO_INCREMENT,
  `file_id` int(11) NOT NULL,
  `attack_types` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `rank` int(11) NOT NULL,
  PRIMARY KEY (`attack_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=54 ;

--
-- Dumping data for table `attack_table`
--

INSERT INTO `attack_table` (`attack_id`, `file_id`, `attack_types`, `date`, `rank`) VALUES
(1, 9, 'TCP Based Attack', '2020-01-23', 2),
(2, 10, 'TCP Based Attack', '2020-01-23', 2),
(3, 11, 'TCP Based Attack', '2020-01-30', 2),
(4, 12, 'TCP Based Attack', '2020-01-30', 2),
(5, 13, 'Unlabeled Data', '2020-01-30', 0),
(6, 14, 'TCP Based Attack', '2020-01-30', 2),
(7, 15, 'TCP Based Attack', '2020-01-30', 2),
(8, 16, 'TCP Based Attack', '2020-01-30', 2),
(9, 17, 'TCP Based Attack', '2020-01-30', 2),
(10, 18, 'TCP Based Attack', '2020-01-30', 2),
(11, 19, 'TCP Based Attack', '2020-01-30', 2),
(12, 20, 'TCP Based Attack', '2020-01-30', 2),
(13, 21, 'TCP Based Attack', '2020-01-30', 2),
(14, 22, 'Unlabeled Data', '2020-01-31', 0),
(15, 23, 'Unlabeled Data', '2020-01-31', 0),
(16, 24, 'Unlabeled Data', '2020-01-31', 0),
(17, 25, 'TCP Based Attack', '2020-01-31', 2),
(18, 26, 'TCP Based Attack', '2020-01-31', 2),
(19, 27, 'Unlabeled Data', '2020-01-31', 0),
(20, 28, 'Unlabeled Data', '2020-01-31', 0),
(21, 29, 'Unlabeled Data', '2020-01-31', 0),
(22, 30, 'TCP Based Attack', '2020-01-31', 2),
(23, 31, 'TCP Based Attack', '2020-01-31', 2),
(24, 32, 'TCP Based Attack', '2023-02-27', 2),
(25, 33, 'TCP Based Attack', '2023-02-27', 2),
(26, 34, 'TCP Based Attack', '2023-02-27', 2),
(27, 35, 'TCP Based Attack', '2023-02-27', 2),
(28, 36, 'TCP Based Attack', '2023-02-27', 2),
(29, 37, 'TCP Based Attack', '2023-02-27', 2),
(30, 38, 'TCP Based Attack', '2023-02-28', 2),
(31, 39, 'TCP Based Attack', '2023-02-28', 2),
(32, 40, 'TCP Based Attack', '2023-02-28', 2),
(33, 41, 'TCP Based Attack', '2023-02-28', 2),
(34, 42, 'Unlabeled Data', '2023-03-22', 0),
(35, 43, 'TCP Based Attack', '2023-03-23', 2),
(36, 44, 'TCP Based Attack', '2023-03-23', 2),
(37, 45, 'TCP Based Attack', '2023-03-26', 2),
(38, 46, 'TCP Based Attack', '2023-03-26', 2),
(39, 47, 'TCP Based Attack', '2023-03-27', 2),
(40, 48, 'TCP Based Attack', '2023-03-27', 2),
(41, 49, 'Unlabeled Data', '2023-03-27', 0),
(42, 50, 'TCP Based Attack', '2023-04-18', 2),
(43, 51, 'TCP Based Attack', '2023-04-18', 2),
(44, 52, 'TCP Based Attack', '2023-04-18', 2),
(45, 53, 'TCP Based Attack', '2023-04-18', 2),
(46, 54, 'TCP Based Attack', '2023-04-18', 2),
(47, 55, 'TCP Based Attack', '2023-04-18', 2),
(48, 56, 'TCP Based Attack', '2023-04-18', 2),
(49, 57, 'TCP Based Attack', '2023-04-18', 2),
(50, 58, 'TCP Based Attack', '2023-05-03', 2),
(51, 59, 'TCP Based Attack', '2023-05-03', 2),
(52, 60, 'TCP Based Attack', '2023-05-03', 2),
(53, 61, 'TCP Based Attack', '2023-05-03', 2);

-- --------------------------------------------------------

--
-- Table structure for table `feedback_table`
--

CREATE TABLE IF NOT EXISTS `feedback_table` (
  `Name_of_user` varchar(25) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Experience_with_app` varchar(10) NOT NULL,
  `Rating` varchar(10) NOT NULL,
  `Comments` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback_table`
--

INSERT INTO `feedback_table` (`Name_of_user`, `Email`, `Experience_with_app`, `Rating`, `Comments`) VALUES
('teneena', 'deek94@gmail.com', 'average', 'None', 'j'),
('teneena', 'deek94@gmail.com', 'average', 'None', 'j'),
('teneena', 'deek94@gmail.com', 'bad', 'None', 'ooo');

-- --------------------------------------------------------

--
-- Table structure for table `filedata_table`
--

CREATE TABLE IF NOT EXISTS `filedata_table` (
  `filename` varchar(300) NOT NULL,
  `filetype` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `sender` varchar(25) NOT NULL,
  `receiver` varchar(25) NOT NULL,
  `sending_purpose` varchar(100) NOT NULL,
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=62 ;

--
-- Dumping data for table `filedata_table`
--

INSERT INTO `filedata_table` (`filename`, `filetype`, `date`, `sender`, `receiver`, `sending_purpose`, `file_id`) VALUES
('2016-07-29-14-43-46-919.jpg', 'image', '2019-08-27', 'deek94@gmail.com', 'deek', 'hi', 1),
('djig6sZ.jpg', 'image', '2019-08-27', 'deek94@gmail.com', 'pol', 'oooo', 2),
('dataset_zmwyASh.csv', 'document', '2020-01-31', 'sunitha@gmail.com', 'tan@gmail.com', 'asas', 31),
('dataset_y9jE8uL.csv', 'document', '2023-02-27', 'tan@gmail.com', 'jes@gmail.com', 'test', 32),
('dataset_ySHBzll.csv', 'document', '2023-02-27', 'tan@gmail.com', 'jes@gmail.com', 'test', 33),
('dataset_IsWmC8U.csv', 'document', '2023-02-27', 'jes@gmail.com', 'tan@gmail.com', 'haii', 34),
('dataset_I5RHfGW.csv', 'document', '2023-02-27', 'jes@gmail.com', 'tan@gmail.com', 'haii', 35),
('dataset_SAvgAyq.csv', 'document', '2023-02-27', 'jes@gmail.com', 'tan@gmail.com', 'haaaaii', 36),
('dataset_ab4hWxG.csv', 'document', '2023-02-27', 'jes@gmail.com', 'tan@gmail.com', 'haaaaii', 37),
('dataset_vvroX8E.csv', 'document', '2023-02-28', 'jes@gmail.com', 'tan@gmail.com', 'haaiiiiiiiiiiii', 38),
('dataset_QR4i71l.csv', 'document', '2023-02-28', 'jes@gmail.com', 'tan@gmail.com', 'haaiiiiiiiiiiii', 39),
('dataset_EiAvb2H.csv', 'document', '2023-02-28', 'jes@gmail.com', 'kavya@gmail.com', 'hai nice to meet you', 40),
('dataset_CErbzOp.csv', 'document', '2023-02-28', 'jes@gmail.com', 'kavya@gmail.com', 'hai nice to meet you', 41),
('banner1.jpg', 'image', '2023-03-22', 'tan@gmail.com', 'jesusmj@gmail.com', 'hai', 42),
('dataset_JAaQdF3.csv', 'document', '2023-03-23', 'kavya@gmail.com', 'anju@gmail.com', 'haiiii', 43),
('dataset_Sw5cuOz.csv', 'document', '2023-03-23', 'kavya@gmail.com', 'anju@gmail.com', 'haiiii', 44),
('dataset_1luUshg.csv', 'document', '2023-03-26', 'sunitha@gmail.com', 'deek94@gmail.com', 'hai', 45),
('dataset_pV8p6Du.csv', 'document', '2023-03-26', 'sunitha@gmail.com', 'deek94@gmail.com', 'hai', 46),
('dataset_8CkHncX.csv', 'document', '2023-05-03', 'vaish@gmail.com', 'sunitha@gmail.com', 'Hai Nice to meet you', 59),
('dataset_19uNzDt.csv', 'document', '2023-05-03', 'vaish@gmail.com', 'sunitha@gmail.com', 'hghg', 60),
('dataset_rH9fPiq.csv', 'document', '2023-05-03', 'vaish@gmail.com', 'sunitha@gmail.com', 'hghg', 61);

-- --------------------------------------------------------

--
-- Table structure for table `registernow`
--

CREATE TABLE IF NOT EXISTS `registernow` (
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `email` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `reg_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`reg_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `registernow`
--

INSERT INTO `registernow` (`firstname`, `lastname`, `email`, `password`, `reg_id`) VALUES
('sunitha', 'manoharan', 'sunitha@gmail.com', 'suni', 1),
('Deek', 'dil', 'deek94@gmail.com', 'deelsa15', 2),
('amal', 'geo', 'amal@gmail.com', 'Amal@123', 3),
('shelvin', 'sunil', 'shelvin@gmail.com', '1234', 4),
('vaish', 'mohan', 'vaish@gmail.com', '1234', 5);

-- --------------------------------------------------------

--
-- Table structure for table `reply_table`
--

CREATE TABLE IF NOT EXISTS `reply_table` (
  `reply_id` int(11) NOT NULL AUTO_INCREMENT,
  `from` varchar(50) NOT NULL,
  `to` varchar(50) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `file_type` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `message` varchar(200) NOT NULL,
  PRIMARY KEY (`reply_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `reply_table`
--

