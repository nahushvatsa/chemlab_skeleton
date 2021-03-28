DROP TABLE IF EXISTS totalequipment;

CREATE TABLE totalequipment (
  EquipmentName varchar(150) NOT NULL,
  TotalStock int DEFAULT NULL,
  AvailibleStock int DEFAULT NULL,
  Price int DEFAULT NULL
) 

LOCK TABLES `totalequipment` WRITE;

INSERT INTO `totalequipment` VALUES ('Beaker',25,25,10),('Test Tube',30,30,5),('Watchglass',15,15,5),('Flask',20,20,10),('Funnel',15,15,7),('Burette',10,10,15),('Pipette',10,10,15);
