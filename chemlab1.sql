-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: chemlab
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `Name` varchar(200) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `Accounttype` varchar(50) NOT NULL,
  `Datejoined` date NOT NULL,
  `Balance` int NOT NULL DEFAULT '100',
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES ('Admin','admin@mail.com','kjirmqhE','admin','2020-12-10',100),('Nahush','nahushvatsa@gmail.com','kjisppiL','student','2020-12-10',999),('Praful','pgchandarana@hotmail.com','kjideU','student','2020-12-11',90),('test','test@test.com','jixwiX','student','2020-12-10',-2026),('test2','test2@test.com','jixwiX','student','2020-12-10',55);
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rentedequipment`
--

DROP TABLE IF EXISTS `rentedequipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rentedequipment` (
  `email` varchar(50) DEFAULT NULL,
  `equipment` varchar(100) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `datetime` timestamp NULL DEFAULT NULL,
  `datetime2` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rentedequipment`
--

LOCK TABLES `rentedequipment` WRITE;
/*!40000 ALTER TABLE `rentedequipment` DISABLE KEYS */;
/*!40000 ALTER TABLE `rentedequipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `totalequipment`
--

DROP TABLE IF EXISTS `totalequipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `totalequipment` (
  `EquipmentName` varchar(150) NOT NULL,
  `TotalStock` int DEFAULT NULL,
  `AvailibleStock` int DEFAULT NULL,
  `Price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `totalequipment`
--

LOCK TABLES `totalequipment` WRITE;
/*!40000 ALTER TABLE `totalequipment` DISABLE KEYS */;
INSERT INTO `totalequipment` VALUES ('Beaker',25,25,10),('Test Tube',30,30,5),('Watchglass',15,15,5),('Flask',20,20,10),('Funnel',15,15,7),('Burette',10,10,15),('Pipette',10,10,15);
/*!40000 ALTER TABLE `totalequipment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-25 10:46:05
