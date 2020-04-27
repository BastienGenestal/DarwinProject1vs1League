-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: darwin1v1league
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ranking` int DEFAULT NULL,
  `user_id` varchar(32) NOT NULL,
  `user_name` varchar(32) DEFAULT NULL,
  `avatar_url` varchar(128) DEFAULT NULL,
  `first_seen` datetime NOT NULL,
  `region` varchar(16) DEFAULT NULL,
  `platform` varchar(16) DEFAULT NULL,
  `elo` int DEFAULT NULL,
  `victory` int DEFAULT NULL,
  `defeat` int DEFAULT NULL,
  `streak` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,NULL,'280819236820221952','Flow','https://cdn.discordapp.com/avatars/280819236820221952/70ba3efcfc81f03ed967ba05c4e2f0e3.webp?size=1024','2020-04-26 22:58:03',NULL,NULL,500,NULL,NULL,NULL),(2,NULL,'361876799669665792','AceOfEu','https://cdn.discordapp.com/avatars/361876799669665792/01dedf894866a89254030a070d5f99e7.webp?size=1024','2020-04-24 21:07:09',NULL,'PC',500,NULL,NULL,NULL),(3,NULL,'455584567429038080','rayce','https://cdn.discordapp.com/avatars/455584567429038080/11c539ee765df54f7ff74e4dafe6289a.webp?size=1024','2020-04-25 00:30:15',NULL,'PC',500,NULL,NULL,NULL),(4,NULL,'417048769012695041','Garou','https://cdn.discordapp.com/avatars/417048769012695041/6c73219ed61bb255f8a6b2627301739f.webp?size=1024','2020-04-24 22:08:10',NULL,NULL,500,NULL,NULL,NULL),(5,NULL,'202563197247422464','mralexc','https://cdn.discordapp.com/avatars/202563197247422464/dd7bdfde53b903276836c0ea19bbfc7a.webp?size=1024','2020-04-25 02:24:18',NULL,'PC',500,NULL,NULL,NULL),(6,NULL,'218832288509591552','TeeZ','https://cdn.discordapp.com/avatars/218832288509591552/29db83708ac72dfc2ee72c1c20659566.webp?size=1024','2020-04-20 18:57:03',NULL,'PC',500,NULL,NULL,NULL),(7,NULL,'546153850529382425','SBR Jade Anthony','https://cdn.discordapp.com/avatars/546153850529382425/78aad28543594c04c96de9e767e13afe.webp?size=1024','2020-04-26 04:24:11',NULL,'PC',500,NULL,NULL,NULL),(8,NULL,'527321349224660992','boomin','https://cdn.discordapp.com/avatars/527321349224660992/3b650c91737dc1b056e1851680d0ebb5.webp?size=1024','2020-04-26 07:10:14',NULL,'PC',500,NULL,NULL,NULL),(9,NULL,'299589266755944458','multi','https://cdn.discordapp.com/avatars/299589266755944458/ab6c7f8a60a315e04648348994f6d765.webp?size=1024','2020-04-26 06:17:58',NULL,'PC',500,NULL,NULL,NULL),(10,NULL,'176715391987351553','PassTheSoap','https://cdn.discordapp.com/avatars/176715391987351553/522d8768d4eee130607a408f24a76e29.webp?size=1024','2020-04-26 16:13:46',NULL,NULL,500,NULL,NULL,NULL),(11,NULL,'664500051732856844','OG VIPER','https://cdn.discordapp.com/avatars/664500051732856844/de35897ac8b14b8c59b6c206c20435ff.webp?size=1024','2020-04-24 23:47:25',NULL,NULL,500,NULL,NULL,NULL),(12,NULL,'380444456924741643','ErzaSkill','https://cdn.discordapp.com/avatars/380444456924741643/a86a8447ceadbe59630ceb1757947dd8.webp?size=1024','2020-04-24 22:42:22',NULL,'PC',500,NULL,NULL,NULL),(13,NULL,'307600981418442762','\"Ziinga\"  Wilfried Hert','https://cdn.discordapp.com/avatars/307600981418442762/eb0d6de88646906c9a94f040085d1f00.webp?size=1024','2020-04-20 19:10:09',NULL,'PC',500,NULL,NULL,NULL),(14,NULL,'452449367496851457','MrDiese','https://cdn.discordapp.com/avatars/452449367496851457/0e875e80a1872c01f6b84a78561c9851.webp?size=1024','2020-04-24 20:07:13',NULL,NULL,500,NULL,NULL,NULL),(15,NULL,'283089027744137218','BL4CKM4RKET','https://cdn.discordapp.com/avatars/283089027744137218/cad0e65d1bd490b7fadfa0afd42f7094.webp?size=1024','2020-04-24 22:24:41',NULL,NULL,500,NULL,NULL,NULL),(16,NULL,'165206487562452993','Yuideh','https://cdn.discordapp.com/avatars/165206487562452993/e895e6ee74f179afc40783f2445cca4c.webp?size=1024','2020-04-24 22:00:03',NULL,'PC',500,NULL,NULL,NULL),(17,NULL,'196358835928039434','Azertiq','https://cdn.discordapp.com/avatars/196358835928039434/b6d4c1335833b8d6da5edaaef390ee0c.webp?size=1024','2020-04-24 22:37:11',NULL,'PC',500,NULL,NULL,NULL),(18,NULL,'480853790552096778','SBR Nickel','https://cdn.discordapp.com/avatars/480853790552096778/194f9b683125bae916233a02bfba98e3.webp?size=1024','2020-04-26 16:04:03',NULL,'PC',500,NULL,NULL,NULL),(19,NULL,'237624941854457857','Poisoned Bunny','https://cdn.discordapp.com/avatars/237624941854457857/35ab5287c248e95aa600a02d99f084a9.webp?size=1024','2020-04-24 20:08:38',NULL,'PC',500,NULL,NULL,NULL),(20,NULL,'193200470498607114','Mig','https://cdn.discordapp.com/avatars/193200470498607114/a88988967568c0a880ca3133a931628d.webp?size=1024','2020-04-26 05:31:58',NULL,'PC',500,NULL,NULL,NULL),(21,NULL,'439364864763363363','Pastry Bread','https://cdn.discordapp.com/avatars/439364864763363363/27cff9ee26b7d9f1ab264c144bd60eec.webp?size=1024','2020-04-24 20:19:59',NULL,'PC',500,NULL,NULL,NULL),(22,NULL,'273670702211792906','nickey','https://cdn.discordapp.com/avatars/273670702211792906/fdbfa956a3a05fb0b3586a1af00c3d72.webp?size=1024','2020-04-26 17:48:10',NULL,NULL,500,NULL,NULL,NULL),(23,NULL,'396298735199453184','GH0STY','https://cdn.discordapp.com/avatars/396298735199453184/deaa93aaf9f5295954d939cb006eed4f.webp?size=1024','2020-04-24 21:41:12',NULL,'PC',500,NULL,NULL,NULL),(24,NULL,'506151685882773507','Roshi.','https://cdn.discordapp.com/avatars/506151685882773507/d899b1017aaac1d32e77ecca5d53e3ef.webp?size=1024','2020-04-25 01:57:35',NULL,'PC',500,NULL,NULL,NULL),(25,NULL,'108700966307495936','Ascndr','https://cdn.discordapp.com/avatars/108700966307495936/a_99c224c587dd0b9799e4c8f86118e6e4.gif?size=1024','2020-04-24 20:04:46',NULL,'PC',500,NULL,NULL,NULL),(26,NULL,'495376797957881867','𝒲𝒪𝒲','https://cdn.discordapp.com/avatars/495376797957881867/161042a996d89c6d155d4cbb8fec12c3.webp?size=1024','2020-04-26 19:16:22',NULL,'PC',500,NULL,NULL,NULL),(27,NULL,'202907967459295232','Kazuma','https://cdn.discordapp.com/avatars/202907967459295232/4054bb6432d76b672dc24bc3eda814c0.webp?size=1024','2020-04-26 04:23:29',NULL,'PC',500,NULL,NULL,NULL),(28,NULL,'371599590841122818','Sushi','https://cdn.discordapp.com/avatars/371599590841122818/1e00cd2af1a5e44f280de874124ccc55.webp?size=1024','2020-04-24 20:04:19',NULL,'PC',500,NULL,NULL,NULL),(29,NULL,'455934510245216263','hypnos.','https://cdn.discordapp.com/avatars/455934510245216263/a_148ee78ae50459da102f415d0339e5bf.gif?size=1024','2020-04-26 04:16:34',NULL,'PC',500,NULL,NULL,NULL),(30,NULL,'390141802214326295','WhoIsThis','https://cdn.discordapp.com/avatars/390141802214326295/31552dd1b06df2f6abf82966c2a989b7.webp?size=1024','2020-04-25 00:32:13',NULL,NULL,500,NULL,NULL,NULL),(31,NULL,'512714438290309158','M4','https://cdn.discordapp.com/avatars/512714438290309158/c6705e729afe2d9e0423f96df80da80a.webp?size=1024','2020-04-25 21:50:17',NULL,NULL,500,NULL,NULL,NULL),(32,NULL,'263705990543835138','Mini Sam','https://cdn.discordapp.com/avatars/263705990543835138/8ef21b96a8bc43d39c811393919a1941.webp?size=1024','2020-04-25 01:26:10',NULL,'PC',500,NULL,NULL,NULL),(33,NULL,'535863932024258571','Zerx','https://cdn.discordapp.com/avatars/535863932024258571/307facd42c7adeb11cfcfc1da6ae625f.webp?size=1024','2020-04-24 21:48:50',NULL,'PC',500,NULL,NULL,NULL),(34,NULL,'332621028180361236','likenyge','https://cdn.discordapp.com/avatars/332621028180361236/ef6f393d540a9efaa1ac5cf61d5bb5cf.webp?size=1024','2020-04-24 20:05:06',NULL,'PC',500,NULL,NULL,NULL),(35,NULL,'641763398530629650','Tor1bus','https://cdn.discordapp.com/avatars/641763398530629650/ea349a5355269933f60f648818123112.webp?size=1024','2020-04-24 21:49:39',NULL,NULL,500,NULL,NULL,NULL),(36,NULL,'176333395444498432','Dabestchicken','https://cdn.discordapp.com/avatars/176333395444498432/c39e091ada7175a89f7c156ef08fee8f.webp?size=1024','2020-04-26 06:42:05',NULL,'PC',500,NULL,NULL,NULL),(37,NULL,'262761650669486080','Nolan The Creator','https://cdn.discordapp.com/avatars/262761650669486080/c4a2b2a5a3b34f0ddf7700e5c9091c8b.webp?size=1024','2020-04-25 21:59:18',NULL,'PC',500,NULL,NULL,NULL),(38,NULL,'157526500063707137','etc','https://cdn.discordapp.com/avatars/157526500063707137/54067d7659b02450084f6be6aa58f22a.webp?size=1024','2020-04-24 22:19:19',NULL,NULL,500,NULL,NULL,NULL),(39,NULL,'401855734029090828','BOT MAX','https://cdn.discordapp.com/avatars/401855734029090828/9fa849ee87414d2dfb30c7583c2dcab2.webp?size=1024','2020-04-26 08:53:58',NULL,'PC',500,NULL,NULL,NULL),(40,NULL,'144785156652138496','Dusta','https://cdn.discordapp.com/avatars/144785156652138496/6b55968c0dd271d558fc86b4cb435f05.webp?size=1024','2020-04-24 20:27:54',NULL,'PC',500,NULL,NULL,NULL),(41,NULL,'290250173571923969','Princess✨','https://cdn.discordapp.com/avatars/290250173571923969/7c70e9a24835573fb6d5da9a9882cb78.webp?size=1024','2020-04-26 04:23:27',NULL,'PS4',500,NULL,NULL,NULL),(42,NULL,'210873714806358016','𝓔𝓵𝓲𝓼𝒆 𝓝𝓪𝓸','https://cdn.discordapp.com/avatars/210873714806358016/ea11c2d6fe8ab8d91118ffcbb6450d81.webp?size=1024','2020-04-25 03:13:03',NULL,NULL,500,NULL,NULL,NULL),(43,NULL,'328981315791880193','Churro','https://cdn.discordapp.com/avatars/328981315791880193/f78da85db794dd53dff5469e6c8ea728.webp?size=1024','2020-04-26 04:25:07',NULL,'PC',500,NULL,NULL,NULL),(44,NULL,'510771887614197801','TVnoise','https://cdn.discordapp.com/avatars/510771887614197801/0f884d491f7bb2c9cd2fb315f15cfb91.webp?size=1024','2020-04-24 20:08:33',NULL,'PC',500,NULL,NULL,NULL),(45,NULL,'415581459236257813','Sohan','https://cdn.discordapp.com/avatars/415581459236257813/d3b77dc6010daf7a4531e378228063ba.webp?size=1024','2020-04-25 21:41:19',NULL,NULL,500,NULL,NULL,NULL),(46,NULL,'327130839588667422','Soj','https://cdn.discordapp.com/avatars/327130839588667422/dc327de458c5197d7499c7bbfd02d052.webp?size=1024','2020-04-27 00:26:21',NULL,'PC',500,NULL,NULL,NULL),(47,NULL,'704156886630400080','bumble bee','https://cdn.discordapp.com/avatars/704156886630400080/29002167060d23b9503e5171280904e7.webp?size=1024','2020-04-27 02:29:58',NULL,NULL,500,NULL,NULL,NULL),(48,NULL,'125375344038379520','Agge','https://cdn.discordapp.com/avatars/125375344038379520/9ded1ad24ca229e57597e252a75a8b9b.webp?size=1024','2020-04-24 23:12:49',NULL,NULL,500,NULL,NULL,NULL),(49,NULL,'402111043347939329','Graf_itti','https://cdn.discordapp.com/avatars/402111043347939329/18088b1e15bdd2e801d3007635562a01.webp?size=1024','2020-04-25 21:00:43',NULL,NULL,500,NULL,NULL,NULL),(50,NULL,'244490875290386432','Swoopyyyyy','https://cdn.discordapp.com/avatars/244490875290386432/70e10b6d23fa9d5e0284f576806d70d4.webp?size=1024','2020-04-25 12:58:01',NULL,NULL,500,NULL,NULL,NULL),(51,NULL,'358553083384692738','ezieR [TDB]','https://cdn.discordapp.com/avatars/358553083384692738/1ef5c5478eb30c06174bdd4d6533f8cb.webp?size=1024','2020-04-25 08:00:05',NULL,NULL,500,NULL,NULL,NULL),(52,NULL,'500104859224244244','.Sp1ral.','https://cdn.discordapp.com/avatars/500104859224244244/45cecd58a164bfb338fb3ab08894b520.webp?size=1024','2020-04-26 18:27:02',NULL,NULL,500,NULL,NULL,NULL),(53,NULL,'418407791242510346','Philipeace','https://cdn.discordapp.com/avatars/418407791242510346/aabb712848e4dc8d0b7d94c6d4786a61.webp?size=1024','2020-04-25 13:33:31',NULL,NULL,500,NULL,NULL,NULL),(54,NULL,'243149909279113236','quelqu\'un','https://cdn.discordapp.com/avatars/243149909279113236/f21ff9fc4f1859355350966443b63665.webp?size=1024','2020-04-24 20:04:43',NULL,'PC',500,NULL,NULL,NULL),(55,NULL,'340546977433387010','Darkn3s5','https://cdn.discordapp.com/avatars/340546977433387010/facb7a5d0c23b063d5e30850b7a3a7c6.webp?size=1024','2020-04-26 06:48:41',NULL,NULL,500,NULL,NULL,NULL),(56,NULL,'619574372092346399','Remix','https://cdn.discordapp.com/avatars/619574372092346399/f7877343940841fa0af0ea269a3e8fa8.webp?size=1024','2020-04-25 00:47:28',NULL,'PC',500,NULL,NULL,NULL),(57,NULL,'329284079726100480','zJewbearOG','https://cdn.discordapp.com/avatars/329284079726100480/ae582561080b0d6a1021d148c0b320a9.webp?size=1024','2020-04-26 10:12:00',NULL,NULL,500,NULL,NULL,NULL),(58,NULL,'426136064780926977','BenjaminSPR','https://cdn.discordapp.com/avatars/426136064780926977/a0f005b4f609983f6e38fa58730dc227.webp?size=1024','2020-04-24 20:44:42',NULL,'PC',500,NULL,NULL,NULL),(59,NULL,'153325297431740416','Y4mikun','https://cdn.discordapp.com/avatars/153325297431740416/a_1b44f020cd6ecb2fa2ca50993aee132a.gif?size=1024','2020-04-25 21:22:56',NULL,NULL,500,NULL,NULL,NULL),(60,NULL,'397077380801363969','Hayden','https://cdn.discordapp.com/avatars/397077380801363969/4b23ecb39a673e8723be6e81e8d6e49d.webp?size=1024','2020-04-25 00:25:44',NULL,'PC',500,NULL,NULL,NULL),(61,NULL,'201340041233039361','JaxDagger','https://cdn.discordapp.com/avatars/201340041233039361/c03f11d4d048ffeffd74732830c01a32.webp?size=1024','2020-04-25 18:46:33',NULL,NULL,500,NULL,NULL,NULL),(62,NULL,'427922423828971531','alphA','https://cdn.discordapp.com/avatars/427922423828971531/d2d85a6d58da0c1c03b447d28b2112ac.webp?size=1024','2020-04-22 21:23:56',NULL,'PC',500,NULL,NULL,NULL),(63,NULL,'673198334281777152','Valentine','https://cdn.discordapp.com/avatars/673198334281777152/cb9703d049ad14beeec1ce92cef6a5a0.webp?size=1024','2020-04-22 22:16:40',NULL,NULL,485,NULL,NULL,0),(64,NULL,'514140882274877462','DaVe','https://cdn.discordapp.com/avatars/514140882274877462/ce8bd9d38d586312e07f104a56600969.webp?size=1024','2020-04-25 22:39:55',NULL,NULL,500,NULL,NULL,NULL),(65,NULL,'370276540409184259','littlevic','https://cdn.discordapp.com/avatars/370276540409184259/fdcd939ffa575c93d42e1781aaecff8c.webp?size=1024','2020-04-24 21:07:57',NULL,'PC',500,NULL,NULL,NULL),(66,NULL,'266375377633542147','MIKUS','https://cdn.discordapp.com/avatars/266375377633542147/e0e6469715992910f1adf052004a788c.webp?size=1024','2020-04-27 02:04:34',NULL,NULL,500,NULL,NULL,NULL),(67,NULL,'277517522968772609','Izanagi','https://cdn.discordapp.com/avatars/277517522968772609/ba873a199a969d2dbd8e7cf3805b5b11.webp?size=1024','2020-04-26 04:23:46',NULL,'PC',500,NULL,NULL,NULL),(68,NULL,'195624294674333706','Nekrosu','https://cdn.discordapp.com/avatars/195624294674333706/a63916c2e79d77a3f0e62525b82c56aa.webp?size=1024','2020-04-24 22:10:52',NULL,NULL,500,NULL,NULL,NULL),(69,NULL,'436726255816015872','m31','https://cdn.discordapp.com/avatars/436726255816015872/29965358bc54fab8b5bb29f1be9db768.webp?size=1024','2020-04-26 04:23:49',NULL,'PC',500,NULL,NULL,NULL),(70,NULL,'358617116112322572','RiCS0','https://cdn.discordapp.com/avatars/358617116112322572/b4453a2d91d8340cc2c91e980e013eb3.webp?size=1024','2020-04-24 19:40:41',NULL,'PC',500,NULL,NULL,NULL),(71,NULL,'207173836666437642','Quentin','https://cdn.discordapp.com/avatars/207173836666437642/08a1d39ae643f28be83e3615bbc0740a.webp?size=1024','2020-04-24 21:07:26',NULL,'PC',500,NULL,NULL,NULL),(72,NULL,'227883327149834241','JeevS','https://cdn.discordapp.com/avatars/227883327149834241/f613de308edf1246bf8c78bfa20ede98.webp?size=1024','2020-04-24 20:57:27',NULL,NULL,500,NULL,NULL,NULL),(73,NULL,'261970223572320257','IceQ','https://cdn.discordapp.com/avatars/261970223572320257/93f0f1ea037da94c0c4b5d009ba351a7.webp?size=1024','2020-04-26 09:08:51',NULL,'PC',500,NULL,NULL,NULL),(74,NULL,'138298541759135744','FrozenNQ','https://cdn.discordapp.com/avatars/138298541759135744/d99e2e4df33f47dd4588eaf025062320.webp?size=1024','2020-04-24 22:46:37',NULL,NULL,500,NULL,NULL,NULL),(75,NULL,'470631846288424960','EhFamous','https://cdn.discordapp.com/avatars/470631846288424960/d1ccbf369b4ce92f77e93624d138ebef.webp?size=1024','2020-04-26 01:53:00',NULL,NULL,500,NULL,NULL,NULL),(76,NULL,'209677404074016769','Purple','https://cdn.discordapp.com/avatars/209677404074016769/8c430765764f3d7ae93a87f021e4ede1.webp?size=1024','2020-04-24 20:05:13',NULL,'PC',500,NULL,NULL,NULL),(77,NULL,'628403801367511080','Skylord','https://cdn.discordapp.com/avatars/628403801367511080/a5ddc5f7ce2901d573e016868b032bcd.webp?size=1024','2020-04-24 20:34:12',NULL,'PC',500,NULL,NULL,NULL),(78,NULL,'164170872968445952','Fee','https://cdn.discordapp.com/avatars/164170872968445952/2d557e6536cd45f9bd69ae8e7f8f241e.webp?size=1024','2020-04-26 04:24:10',NULL,'PC',500,NULL,NULL,NULL),(79,NULL,'270185379770925056','2304_','https://cdn.discordapp.com/avatars/270185379770925056/6431f898ee5e3fed0837dc3919f4c1f8.webp?size=1024','2020-04-24 20:05:07',NULL,NULL,500,NULL,NULL,NULL),(80,NULL,'200267840912097291','3zmo','https://cdn.discordapp.com/avatars/200267840912097291/144e29eb43037843da2011cd8fa920ea.webp?size=1024','2020-04-25 01:27:18',NULL,'PC',500,NULL,NULL,NULL),(81,NULL,'181061433067438080','thelazyslof','https://cdn.discordapp.com/avatars/181061433067438080/eba17157ef72dbc2cca7993f45704b5c.webp?size=1024','2020-04-24 21:38:32',NULL,'PC',500,NULL,NULL,NULL),(82,NULL,'283236278584082432','Khyzz','https://cdn.discordapp.com/avatars/283236278584082432/0c30a2e44fa16bbe15aa65726cebdaf8.webp?size=1024','2020-04-20 18:45:10','EU','PC',NULL,NULL,NULL,NULL),(83,NULL,'239049232030367745','Slurp','https://cdn.discordapp.com/avatars/239049232030367745/acae1b0100efc0d54ce2a926ff25d94a.webp?size=1024','2020-04-24 22:54:19',NULL,'PC',500,NULL,NULL,NULL),(84,NULL,'511986297192185877','Minkarou','https://cdn.discordapp.com/avatars/511986297192185877/703c8a2b11e841ad12e24c392b9881b6.webp?size=1024','2020-04-26 04:22:32',NULL,'PC',500,NULL,NULL,NULL);
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-27 14:32:53
