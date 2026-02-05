-- MySQL dump 10.13  Distrib 8.1.0, for Linux (aarch64)
--
-- Host: localhost    Database: national_parks
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `parks`
--

DROP TABLE IF EXISTS `parks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parks` (
  `park_code` char(4) NOT NULL,
  `park_name` varchar(200) NOT NULL,
  `state` char(20) NOT NULL,
  `acres` int NOT NULL,
  `latitude` decimal(8,5) NOT NULL,
  `longitude` decimal(8,5) NOT NULL,
  PRIMARY KEY (`park_code`),
  UNIQUE KEY `uq_parks_name` (`park_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `species`
--

DROP TABLE IF EXISTS `species`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `species` (
  `species_id` varchar(10) NOT NULL,
  `park_code` varchar(4) NOT NULL,
  `park_name` varchar(200) NOT NULL,
  `category` varchar(50) DEFAULT NULL,
  `tax_order` varchar(50) DEFAULT NULL,
  `family` varchar(50) DEFAULT NULL,
  `scientific_name` varchar(150) DEFAULT NULL,
  `common_names` text,
  `record_status` varchar(50) DEFAULT NULL,
  `occurrence` varchar(50) DEFAULT NULL,
  `nativeness` varchar(50) DEFAULT NULL,
  `abundance` varchar(50) DEFAULT NULL,
  `seasonality` varchar(50) DEFAULT NULL,
  `conservation_status` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`species_id`),
  KEY `idx_species_park_code` (`park_code`),
  CONSTRAINT `fk_species_parks` FOREIGN KEY (`park_code`) REFERENCES `parks` (`park_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-05 21:47:22
