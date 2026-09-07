-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 30, 2021 at 09:47 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `huskyplatform`
--

-- --------------------------------------------------------

--
-- Table structure for table `activities`
--

CREATE TABLE `activities` (
  `id` int(250) NOT NULL,
  `activity` varchar(250) NOT NULL,
  `year` varchar(250) NOT NULL,
  `type` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `activities`
--

INSERT INTO `activities` (`id`, `activity`, `year`, `type`) VALUES
(1, 'Think Science presentation', '2019', 'activity'),
(2, 'Robot4Good', '2017', 'activity'),
(3, 'UAEU AI & Robotics Lab Platform', '2020', 'activity');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(250) NOT NULL,
  `userid` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `userid`, `password`) VALUES
(1, 'nurtech', 'password'),
(2, 'husky', 'password'),
(3, '123456789', 'password');

-- --------------------------------------------------------

--
-- Table structure for table `pendingstudents`
--

CREATE TABLE `pendingstudents` (
  `id` int(250) NOT NULL,
  `studentnumber` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `date` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pendingstudentsdeletion`
--

CREATE TABLE `pendingstudentsdeletion` (
  `id` int(250) NOT NULL,
  `studentnumber` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pendingstudentsdeletion`
--

INSERT INTO `pendingstudentsdeletion` (`id`, `studentnumber`) VALUES
(2, '201970087'),
(3, '201970087');

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `id` int(250) NOT NULL,
  `projectname` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `shortdesc` varchar(250) NOT NULL,
  `imageext` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`id`, `projectname`, `title`, `shortdesc`, `imageext`) VALUES
(1, '3dprinter', 'building a concrete 3d printer', 'A concrete 3d printer built in UAEU AI & Robotics lab, currently at phase 2 of the development', 'png'),
(2, 'assistivedevices', 'Rehabilitation and Assistive Devices for Upper Limbs', 'Our target in this research is to build an easy use Rehabilitation and Assistive device for Post-Stroke Patients. We are proud that the initial prototype of the robot arm were short-listed for the Robot4good competition in Dubai, UAE 2017', 'png'),
(3, 'avatartherapy', 'Avatar based interaction therapy: A potential therapeutic approach for children with Autism', 'Autism is a neurodevelopment disorder characterized by severe deficiency in social interaction and communication skills. In this research direction, we are investigating the response of Autistic Children to a robotic-avatar therapeutic system unique', 'png'),
(4, 'camelreader', 'Camel Body Language Reader', 'Camels are considered a key figure in the heritage of the UAE. This research targets understanding Camel behaviors and various moods. The reason for this study is to decrease the possibilities for post-race camel death incidents', 'png'),
(5, 'labplatform', 'UAEU AI and Robotics Lab Platform', 'UAEU AI & Robotics Lab Platform. This platform was designed and built to assist students and staff with lab, web, and cloud services', 'gif'),
(6, 'sample1', 'just a sample from the admin panel', 'This sample project is added from the admin control panel & content management system. feel free to remove and add projects from the admin control panel to see the dynamic effect in the website', 'jpg'),
(7, 'sample2', 'just a sample from the admin panel', 'This sample project is added from the admin control panel & content management system. feel free to remove and add projects from the admin control panel to see the dynamic effect in the website', 'jpg'),
(8, 'sample3', 'just a sample from the admin panel', 'This sample project is added from the admin control panel & content management system. feel free to remove and add projects from the admin control panel to see the dynamic effect in the website', 'jpg'),
(9, 'sample4', 'just a sample from the admin panel', 'This sample project is added from the admin control panel & content management system. feel free to remove and add projects from the admin control panel to see the dynamic effect in the website', 'jpg'),
(10, 'sample5', 'just a sample from the admin panel', 'This sample project is added from the admin control panel & content management system. feel free to remove and add projects from the admin control panel to see the dynamic effect in the website', 'jpg'),
(11, 'sample6', 'just a sample from the admin panel', 'This sample project is added from the admin control panel & content management system. feel free to remove and add projects from the admin control panel to see the dynamic effect in the website', 'jpg'),
(13, 'sample8', 'this is last sample', 'my description is something', 'jpg');

-- --------------------------------------------------------

--
-- Table structure for table `publications`
--

CREATE TABLE `publications` (
  `id` int(250) NOT NULL,
  `publication` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `type` varchar(250) NOT NULL,
  `year` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `publications`
--

INSERT INTO `publications` (`id`, `publication`, `title`, `type`, `year`) VALUES
(1, 'O. Eldirdiry, R. Zaier, A. Al-Yahmedi, I. Bahadur, and F. Alnajjar, â€œModeling of a biped robot for investigating foot drop using MATLAB/Simulink,â€ Simulation Modelling Practice and Theory, vol. 98, p. 101972, Jan. 2020.', 'Modeling of a biped robot for investigating foot drop using MATLAB/Simulink', 'journal', '2020'),
(2, 'F. Alnajjar, S. Khalid, A. A. Vogan, S. Shimoda, R. Nouchi, and R. Kawashima, â€œEmerging Cognitive Intervention Technologies to Meet the Needs of an Aging Population: A Systematic Review,â€ Frontiers in Aging Neuroscience, vol. 11, Oct. 2019.', 'Emerging Cognitive Intervention Technologies to Meet the Needs of an Aging Population: A Systematic Review', 'journal', '2019'),
(3, 'Fady Alnajjar, Nouf Fadel Nasser Alsaedi, Waleed Khalil Ahmed, Robotic gripping assist, 2019', 'Robotic gripping assist', 'patent', '2019'),
(4, 'Hamad Al Jassmi, Fady Alnajjar, Waleed Khalil Ahmed, Compound nozzle for cement 3D printer to produce thermally insulated composite cement', 'cement 3D printer', 'patent', '2019'),
(5, 'S. Adil Abboud, S. Al-Wais, S. H. Abdullah, F. Alnajjar, and A. Al-Jumaily, â€œLabel Self-Advised Support Vector Machine (LSA-SVM)â€”Automated Classification of Foot Drop Rehabilitation Case Study,â€ Biosensors, vol. 9, no. 4, p. 114, Sep. 2019.', 'Label Self-Advised Support Vector Machine (LSA-SVM)â€”Automated Classification of Foot Drop Rehabilitation Case Study', 'journal', '2019');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(250) NOT NULL,
  `studentnumber` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `date` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `studentnumber`, `email`, `password`, `date`) VALUES
(6, '201970116', '201970116@uaeu.ac.ae', 'kmsa3', '2020/04/11'),
(8, '700032870', '700032870@uaeu.ac.ae', '12345678', '2020/04/11'),
(10, '201870230', '201870230@uaeu.ac.ae', '123456', '2020/04/11'),
(12, '930210676', '930210676@uaeu.ac.ae', 'nur@1975', '2020/04/12'),
(23, '123456789', '123456789@uaeu.ac.ae', '123456789', '2020/04/23'),
(25, '201970087', '201970087@uaeu.ac.ae', '****', '2020/05/06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activities`
--
ALTER TABLE `activities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pendingstudents`
--
ALTER TABLE `pendingstudents`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pendingstudentsdeletion`
--
ALTER TABLE `pendingstudentsdeletion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `publications`
--
ALTER TABLE `publications`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activities`
--
ALTER TABLE `activities`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `pendingstudents`
--
ALTER TABLE `pendingstudents`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `pendingstudentsdeletion`
--
ALTER TABLE `pendingstudentsdeletion`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `publications`
--
ALTER TABLE `publications`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
