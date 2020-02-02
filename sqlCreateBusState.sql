
IF (EXISTS (SELECT *
   FROM INFORMATION_SCHEMA.TABLES
   WHERE TABLE_SCHEMA = 'dbo'
   AND TABLE_NAME = 'BusState'))
   BEGIN
      drop table BusState;
   END;

   Create table dbo.BusState (
	BusToolsVersion varchar(21),
	RouteID varchar(10),
	StopSequence int,
	BusID varchar (8),
	EventTIme datetime,
	Backdoorentry int,
	FrontDoorEntry int,
	FrontDoorExit int,
	BackDoorExit int,
	operatorid varchar(8),
	Latitude decimal(10,8),
	Longitude decimal (10,8)
)