
DROP TABLE IF EXISTS accounts;

CREATE TABLE accounts (
  Name varchar(200) NOT NULL,
  Email varchar(200) NOT NULL,
  Password varchar(200) NOT NULL,
  Accounttype varchar(50) NOT NULL,
  Datejoined date NOT NULL,
  Balance int NOT NULL DEFAULT '100',
  PRIMARY KEY (Email)
) 

-- Dumping data for table accounts

INSERT INTO accounts VALUES ('Admin','admin@mail.com','kjirmqhE','admin','2020-12-10',1000);
INSERT INTO accounts VALUES ('Nahush','email@mail.com','kjisppiL','admin','2020-12-10',999);
INSERT INTO accounts VALUES ('Praful','placeholder@mail.com','kjideU','student','2020-12-11',100);
INSERT INTO accounts VALUES ('test','test@test.com','jixwiX','student','2020-12-10');
INSERT INTO accounts VALUES ('test2','test2@test.com','jixwiX','student','2020-12-10');
