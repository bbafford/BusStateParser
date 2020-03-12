use buswarelogs
go
IF EXISTS ( SELECT *
            FROM   sysobjects
            WHERE  id = object_id(N'[dbo].[InsertTrip]')
                   and OBJECTPROPERTY(id, N'IsProcedure') = 1 )
BEGIN
    DROP PROCEDURE [dbo].[InsertTrip]
END
go


create procedure InsertTrip
(	
@TripNo varchar(15),
@PatternID int,
@TripType varchar(50),
@ScheduleType varchar(50),
@Revenue bit,
@BlockNo bigint,
@BlockID varchar(30),
@Daymap varchar(70),
@TripID varchar(30),
@OrigTATripNo varchar(30),
@OrigTABlockID varchar(30))
As
begin
	insert into [dbo].Trip (
	TripNo,
PatternID,
TripType ,
ScheduleType ,
Revenue ,
BlockNo ,
BlockID,
Daymap ,
TripID ,
OrigTATripNo ,
OrigTABlockID 
	)
	values(
@TripNo ,
@PatternID ,
@TripType ,
@ScheduleType ,
@Revenue ,
@BlockNo,
@BlockID,
@Daymap ,
@TripID ,
@OrigTATripNo ,
@OrigTABlockID 
	)
end
go