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
	@Longitude decimal (10,8))
As
begin

declare @BusToolsVersion varchar(21)
declare @RouteID varchar(10)

declare 	@StopSequence int
declare 	@BusID varchar (8)
declare 	@EventTIme datetime
declare 	@Backdoorentry int
declare 	@FrontDoorEntry int
declare 	@FrontDoorExit int
declare 	@BackDoorExit int
declare 	@operatorid varchar(8)
declare 	@Latitude decimal(10,8)
declare 	@Longitude decimal (10,8)


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
	Longitude
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
	@Longitude
	)
end
go