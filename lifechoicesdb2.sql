-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: lifechoicesdb2
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `date_entered` datetime DEFAULT NULL,
  `date_time_entered` datetime DEFAULT NULL,
  `time_exit` datetime DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Adele','Peaches','2021-07-07 10:34:41.581403','Admin','2021-07-09 00:00:00','2021-07-09 11:45:00',NULL),(2,'Sofia','Ronaldo','2021-07-09 10:23:52.825475','Admin','2021-07-09 00:00:00',NULL,NULL),(11,'Godwin','Green','2021-07-09 10:21:18.997319','Select Department','2021-07-09 00:00:00','2021-07-09 10:50:18',NULL);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guest`
--

DROP TABLE IF EXISTS `guest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guest` (
  `id_num` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `surname` varchar(255) DEFAULT NULL,
  `phone_num` int DEFAULT NULL,
  `kin_name` varchar(255) DEFAULT NULL,
  `kin_num` varchar(255) DEFAULT NULL,
  `date_entered` varchar(255) DEFAULT NULL,
  `id_card` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_num`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest`
--

LOCK TABLES `guest` WRITE;
/*!40000 ALTER TABLE `guest` DISABLE KEYS */;
INSERT INTO `guest` VALUES (1,'Thabo','Setsubi',605545859,'Ayanda','834140547','2021-07-07 10:15:41.182642',NULL);
/*!40000 ALTER TABLE `guest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `signed`
--

DROP TABLE IF EXISTS `signed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `signed` (
  `sign_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `date_enter` datetime DEFAULT NULL,
  `time_enter` datetime DEFAULT NULL,
  `time_exit` datetime DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sign_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signed`
--

LOCK TABLES `signed` WRITE;
/*!40000 ALTER TABLE `signed` DISABLE KEYS */;
/*!40000 ALTER TABLE `signed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `stud_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `date_entered` datetime DEFAULT NULL,
  `date_time_entered` datetime DEFAULT NULL,
  `time_exit` datetime DEFAULT NULL,
  PRIMARY KEY (`stud_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (4,'Thabo','Apple','2021-07-09 10:18:17.536472','LCA','2021-07-10 00:00:00','2021-07-10 13:30:16',NULL),(5,'Ronald','Pokemon','2021-07-09 10:18:42.651620','LCA','2021-07-09 00:00:00','2021-07-09 10:50:18',NULL),(6,'Aaliyah','Weird','2021-07-09 10:18:58.283216','LCA','2021-07-09 00:00:00','2021-07-09 10:50:18',NULL),(7,'Justin','Cigarettes','2021-07-09 10:19:18.390872','LCA','2021-07-09 00:00:00','2021-07-09 10:50:18',NULL),(8,'Mikayla','Lollipop','2021-07-09 10:19:40.264281','LCA','2021-07-09 00:00:00','2021-07-09 10:50:18',NULL),(9,'Ethan','Juice','2021-07-09 10:19:59.875560','LCS','2021-07-09 00:00:00','2021-07-09 10:50:18',NULL),(10,'Izzy','Laugh','2021-07-09 10:20:12.007790','LCS','2021-07-09 00:00:00','2021-07-09 10:50:18',NULL),(12,'Candice','Red','2021-07-09 10:21:36.734950','Lecturer','2021-07-09 00:00:00','2021-07-09 10:50:18',NULL),(13,'Thapelo','Python','2021-07-09 10:21:50.319329','Lecturer','2021-07-09 00:00:00','2021-07-09 10:50:18',NULL);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 10:10:09
