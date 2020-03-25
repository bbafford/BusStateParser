use buswarelogs
go
IF EXISTS ( SELECT *
            FROM   sysobjects
            WHERE  id = object_id(N'[dbo].[InsertBusStateEntry]')
                   and OBJECTPROPERTY(id, N'IsProcedure') = 1 )
BEGIN
    DROP PROCEDURE [dbo].[InsertBusStateEntry]
END
go


create procedure InsertBusStateEntry
(	@BusToolsVersion varchar(21),
	@RouteID varchar(10),
	@StopSequence int,
	@BusID varchar (8),
	@EventTIme varchar(20),
	@Backdoorentry int,
	@FrontDoorEntry int,
	@FrontDoorExit int,
	@BackDoorExit int,
	@operatorid varchar(8),
	@Latitude decimal(10,8),
	@Longitude decimal (10,8),
	@Filename varchar(50))
As
begin


	insert into [dbo].BusState (BusToolsVersion,
	RouteID ,
	StopSequence ,
	BusID ,
	EventTIme ,
	Backdoorentry ,
	FrontDoorEntry ,
	FrontDoorExit ,
	BackDoorExit ,
	operatorid,
	Latitude ,
	Longitude,
	BusStateFile
	)
	values
	(@BusToolsVersion,
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
	@Longitude,
	@filename
	)
end
go