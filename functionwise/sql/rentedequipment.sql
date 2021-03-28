DROP TABLE IF EXISTS rentedequipment;

CREATE TABLE rentedequipment (
  email varchar(50) DEFAULT NULL,
  equipment varchar(100) DEFAULT NULL,
  quantity int DEFAULT NULL,
  datetime timestamp NULL DEFAULT NULL,
  datetime2 timestamp NULL DEFAULT NULL
);
