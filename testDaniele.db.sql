-- MySQL dump 10.13  Distrib 5.1.68, for apple-darwin12.5.0 (i386)
--
-- Host: localhost    Database: testDaniele
-- ------------------------------------------------------
-- Server version	5.1.68

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cat_apartments`
--

DROP TABLE IF EXISTS `cat_apartments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cat_apartments` (
  `id_apartment` int(9) NOT NULL AUTO_INCREMENT,
  `description` varchar(90) NOT NULL,
  PRIMARY KEY (`id_apartment`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat_apartments`
--

LOCK TABLES `cat_apartments` WRITE;
/*!40000 ALTER TABLE `cat_apartments` DISABLE KEYS */;
INSERT INTO `cat_apartments` VALUES (1,'Administration'),(2,'Direction');
/*!40000 ALTER TABLE `cat_apartments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cat_employees`
--

DROP TABLE IF EXISTS `cat_employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cat_employees` (
  `id_employee` int(9) NOT NULL AUTO_INCREMENT,
  `id_apartment` int(8) NOT NULL,
  `nombre` varchar(90) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pwd` text NOT NULL,
  `fech_birth` datetime NOT NULL,
  `salario` double NOT NULL,
  PRIMARY KEY (`id_employee`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat_employees`
--

LOCK TABLES `cat_employees` WRITE;
/*!40000 ALTER TABLE `cat_employees` DISABLE KEYS */;
INSERT INTO `cat_employees` VALUES (1,1,'xOCh','xochilpili@gmail.com','myultrasecurepassword','1981-11-25 00:00:00',20000),(2,2,'Tereza','tereza.chavez@gmail.com','secret','1986-10-27 00:00:00',15000),(3,1,'nom','mail@ma.ccc','password','2013-07-09 00:00:00',1000),(4,2,'fulano de tal','email@mail.com','password','2013-07-09 00:00:00',1400),(5,1,'some','em@asd.com','password','2013-07-09 00:00:00',1200);
/*!40000 ALTER TABLE `cat_employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id_usr` int(8) NOT NULL,
  `username` varchar(10) NOT NULL,
  `pass` text NOT NULL,
  PRIMARY KEY (`id_usr`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-06 22:09:18
