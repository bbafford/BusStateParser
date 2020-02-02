use buswarelogs
go
create procedure InsertBusStateEntry
	@BusToolsVersion varchar(21),
	@RouteID varchar(10),
	@StopSequence int,
	@BusID varchar (8),
	@EventTIme datetime,
	@Backdoorentry int,
	@FrontDoorEntry int,
	@FrontDoorExit int,
	@BackDoorExit int,
	@operatorid varchar(8),
	@Latitude decimal(10,8),
	@Longitude decimal (10,8)
As
	insert into [dbo].BusState values
	(@BusToolsVersion ,
	@RouteID ,
	@StopSequence ,
	@BusID ,
	@EventTIme ,
	@Backdoorentry ,
	@FrontDoorEntry ,
	@FrontDoorExit ,
	@BackDoorExit ,
	@operatorid,
	@Latitude ,
	@Longitude
	)
