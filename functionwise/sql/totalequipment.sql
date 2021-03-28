DROP TABLE IF EXISTS totalequipment;

CREATE TABLE totalequipment (
  EquipmentName varchar(150) NOT NULL,
  TotalStock int DEFAULT NULL,
  AvailibleStock int DEFAULT NULL,
  Price int DEFAULT NULL
) 

-- Dumping data for table totalequipment

INSERT INTO totalequipment VALUES ('Beaker',25,25,10);
INSERT INTO totalequipment VALUES ('Test Tube',30,30,5);
INSERT INTO totalequipment VALUES ('Funnel',15,15,7);
INSERT INTO totalequipment VALUES ('Burette',10,10,15);
INSERT INTO totalequipment VALUES ('Pipette',10,10,15);
INSERT INTO totalequipment VALUES ('Watchglass',15,15,5)
INSERT INTO totalequipment VALUES ('Flask',20,20,10);
