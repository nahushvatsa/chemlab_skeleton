
DROP TABLE IF EXISTS `accounts`;

CREATE TABLE `accounts` (
  `Name` varchar(200) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `Accounttype` varchar(50) NOT NULL,
  `Datejoined` date NOT NULL,
  `Balance` int NOT NULL DEFAULT '100',
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `accounts` WRITE;

INSERT INTO `accounts` VALUES ('Admin','admin@mail.com','kjirmqhE','admin','2020-12-10',100),('Nahush','email@mail.com','kjisppiL','student','2020-12-10',999),('Praful','placeholder@mail.com','kjideU','student','2020-12-11',90),('test','test@test.com','jixwiX','student','2020-12-10',-2026),('test2','test2@test.com','jixwiX','student','2020-12-10',55);
