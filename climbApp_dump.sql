CREATE DATABASE  IF NOT EXISTS `climbing_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `climbing_db`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: climbing_db
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `climbingareas`
--

DROP TABLE IF EXISTS `climbingareas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `climbingareas` (
  `AreaID` int NOT NULL AUTO_INCREMENT,
  `AreaName` varchar(255) NOT NULL,
  `Topography` varchar(255) DEFAULT NULL,
  `EntryFee` decimal(5,2) DEFAULT NULL,
  `NumMonthOpen` int DEFAULT NULL,
  `PeakSeason` varchar(255) DEFAULT NULL,
  `LocationID` int NOT NULL,
  PRIMARY KEY (`AreaID`),
  UNIQUE KEY `AreaName` (`AreaName`),
  KEY `LocationID` (`LocationID`),
  CONSTRAINT `climbingareas_ibfk_1` FOREIGN KEY (`LocationID`) REFERENCES `locations` (`LocationID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `climbingareas`
--

LOCK TABLES `climbingareas` WRITE;
/*!40000 ALTER TABLE `climbingareas` DISABLE KEYS */;
INSERT INTO `climbingareas` VALUES (1,'Yosemite National Park','Mountains',35.00,12,'Summer',1),(2,'Northern Cascades National Park','Mountains',0.00,12,'Summer',2),(3,'Joshua Tree National','Desert',15.00,12,'Fall',3);
/*!40000 ALTER TABLE `climbingareas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `climbingspots`
--

DROP TABLE IF EXISTS `climbingspots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `climbingspots` (
  `SpotID` int NOT NULL AUTO_INCREMENT,
  `SpotName` varchar(255) NOT NULL,
  `TerrainJourney` varchar(255) DEFAULT NULL,
  `CellService` tinyint(1) DEFAULT NULL,
  `AreaID` int NOT NULL,
  PRIMARY KEY (`SpotID`),
  UNIQUE KEY `SpotName` (`SpotName`),
  KEY `AreaID` (`AreaID`),
  CONSTRAINT `climbingspots_ibfk_1` FOREIGN KEY (`AreaID`) REFERENCES `climbingareas` (`AreaID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `climbingspots`
--

LOCK TABLES `climbingspots` WRITE;
/*!40000 ALTER TABLE `climbingspots` DISABLE KEYS */;
INSERT INTO `climbingspots` VALUES (1,'Southern Yosemite','Hike',0,1),(2,'Icicle Creek','Hike',0,2),(3,'Hidden Valley','Hike',0,3);
/*!40000 ALTER TABLE `climbingspots` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `climbs`
--

DROP TABLE IF EXISTS `climbs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `climbs` (
  `ClimbID` int NOT NULL AUTO_INCREMENT,
  `ClimbName` varchar(255) NOT NULL,
  `Difficulty` int DEFAULT NULL,
  `Type` varchar(255) DEFAULT NULL,
  `SpotID` int NOT NULL,
  PRIMARY KEY (`ClimbID`),
  UNIQUE KEY `ClimbName` (`ClimbName`),
  KEY `SpotID` (`SpotID`),
  CONSTRAINT `climbs_ibfk_1` FOREIGN KEY (`SpotID`) REFERENCES `climbingspots` (`SpotID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `climbs`
--

LOCK TABLES `climbs` WRITE;
/*!40000 ALTER TABLE `climbs` DISABLE KEYS */;
INSERT INTO `climbs` VALUES (1,'Wet Hug',0,'Boulder',1),(2,'Sunny and Steep',2,'Boulder',2),(3,'Stem Gem',4,'Boulder',3),(4,'Chuckawalla',1,'Boulder',3),(5,'Big Lizard in my Backyard',0,'Boulder',3),(6,'Little Chucky',4,'Boulder',3),(7,'Medium Chuckie',4,'Boulder',3),(8,'Flintlock Dyno',0,'Boulder',3),(9,'Egg Timer',0,'Boulder',3),(10,'Platypus',0,'Boulder',3),(11,'Dinos Egg',0,'Boulder',3),(12,'Pitch Two',5,'Boulder',3);
/*!40000 ALTER TABLE `climbs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `completedclimbs`
--

DROP TABLE IF EXISTS `completedclimbs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `completedclimbs` (
  `CompletedClimbID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `ClimbID` int NOT NULL,
  `Rating` int DEFAULT NULL,
  PRIMARY KEY (`CompletedClimbID`),
  UNIQUE KEY `UserID` (`UserID`,`ClimbID`),
  KEY `ClimbID` (`ClimbID`),
  CONSTRAINT `completedclimbs_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`),
  CONSTRAINT `completedclimbs_ibfk_2` FOREIGN KEY (`ClimbID`) REFERENCES `climbs` (`ClimbID`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `completedclimbs`
--

LOCK TABLES `completedclimbs` WRITE;
/*!40000 ALTER TABLE `completedclimbs` DISABLE KEYS */;
INSERT INTO `completedclimbs` VALUES (1,1,1,5),(2,1,2,3),(3,1,3,5),(4,1,4,2),(5,1,5,1),(6,1,6,2),(7,1,7,5),(8,1,8,1),(9,1,9,3),(10,1,10,5),(11,1,11,5),(12,1,12,2),(13,2,1,5),(14,2,2,2),(15,2,3,1),(25,2,5,3),(26,2,9,4),(27,2,8,5),(28,23,5,1),(29,23,9,3),(30,23,6,4),(31,23,3,2),(32,24,12,3),(33,24,1,4),(34,25,8,4),(35,25,7,4),(36,25,6,2),(37,26,2,1),(38,27,10,3);
/*!40000 ALTER TABLE `completedclimbs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `LocationID` int NOT NULL AUTO_INCREMENT,
  `State` varchar(255) NOT NULL,
  `City` varchar(255) NOT NULL,
  `Latitude` decimal(9,6) DEFAULT NULL,
  `Longitude` decimal(9,6) DEFAULT NULL,
  PRIMARY KEY (`LocationID`),
  UNIQUE KEY `State` (`State`,`City`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'California','Mariposa',119.538300,37.865100),(2,'Washington','Sedro-Woolley',121.298500,48.771800),(3,'California','Joshua Tree',115.901000,33.873400);
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `userclimbdetails`
--

DROP TABLE IF EXISTS `userclimbdetails`;
/*!50001 DROP VIEW IF EXISTS `userclimbdetails`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `userclimbdetails` AS SELECT 
 1 AS `Username`,
 1 AS `ClimbName`,
 1 AS `SpotName`,
 1 AS `AreaName`,
 1 AS `City`,
 1 AS `State`,
 1 AS `Difficulty`,
 1 AS `Rating`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `SkillLevel` int DEFAULT NULL,
  `Age` int DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Username` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'root','admin',3,21),(2,'user1','pass1',3,27),(3,'user2','pass2',5,50),(4,'user3','pass3',5,49),(5,'user4','pass4',5,23),(6,'user5','pass5',3,21),(7,'Szymon','Kozlowski',NULL,NULL),(8,'Ryan','Jewik',NULL,NULL),(9,'test','pass',NULL,NULL),(10,'123','123',NULL,NULL),(11,'testryan','123',NULL,NULL),(12,'kevin','huang',NULL,NULL),(13,'qwerty','qwerty',NULL,NULL),(14,'qjknfkew','qwefjpqweofi',NULL,NULL),(15,'njgrn','erjiijgre',NULL,NULL),(16,'hghg','jghgh',NULL,NULL),(17,'ieierh','fewiifewu',NULL,NULL),(18,'mike','chin',NULL,NULL),(19,'r','r',NULL,NULL),(20,'w','w',NULL,NULL),(21,'tqt','tre',NULL,NULL),(22,'yryry','hfhfh',NULL,NULL),(23,'ryanj','pass1',NULL,NULL),(24,'tsun9mi','pass1',NULL,NULL),(25,'newuser','pass1',NULL,NULL),(26,'rj','pass1',NULL,NULL),(27,'dynoenjoyer','pass1',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'climbing_db'
--

--
-- Dumping routines for database 'climbing_db'
--

--
-- Final view structure for view `userclimbdetails`
--

/*!50001 DROP VIEW IF EXISTS `userclimbdetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`ryanj`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `userclimbdetails` AS select `u`.`Username` AS `Username`,`c`.`ClimbName` AS `ClimbName`,`cs`.`SpotName` AS `SpotName`,`ca`.`AreaName` AS `AreaName`,`l`.`City` AS `City`,`l`.`State` AS `State`,`c`.`Difficulty` AS `Difficulty`,`cc`.`Rating` AS `Rating` from (((((`completedclimbs` `cc` join `users` `u` on((`cc`.`UserID` = `u`.`UserID`))) join `climbs` `c` on((`cc`.`ClimbID` = `c`.`ClimbID`))) join `climbingspots` `cs` on((`c`.`SpotID` = `cs`.`SpotID`))) join `climbingareas` `ca` on((`cs`.`AreaID` = `ca`.`AreaID`))) join `locations` `l` on((`ca`.`LocationID` = `l`.`LocationID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-02 16:49:53
