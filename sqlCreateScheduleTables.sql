IF (EXISTS (SELECT *
   FROM INFORMATION_SCHEMA.TABLES
   WHERE TABLE_SCHEMA = 'dbo'
   AND TABLE_NAME = 'Trip'))
   BEGIN
      drop table Trip
   END;

Create table dbo.Trip (
TripNo varchar(15),
PatternID int,
TripType varchar(50),
ScheduleType varchar(50),
Revenue bit,
BlockNo bigint,
BlockID varchar(30),
Daymap varchar(70),
TripID varchar(30),
OrigTATripNo varchar(30),
OrigTABlockID varchar(30))

IF (EXISTS (SELECT *
   FROM INFORMATION_SCHEMA.TABLES
   WHERE TABLE_SCHEMA = 'dbo'
   AND TABLE_NAME = 'TripDetail'))
   BEGIN
      drop table TripDetail
   END;

Create table dbo.TripDetail (
TripNo varchar(15),
PatternID int,
TripType varchar(50),
ScheduleType varchar(50),
Revenue bit,
BlockNo bigint,
BlockID varchar(30),
Daymap varchar(70),
TripID varchar(30),
OrigTATripNo varchar(30),
OrigTABlockID varchar(30))

IF (EXISTS (SELECT *
   FROM INFORMATION_SCHEMA.TABLES
   WHERE TABLE_SCHEMA = 'dbo'
   AND TABLE_NAME = 'Pattern'))
   BEGIN
      drop table Pattern
   END;

Create table dbo.Pattern (
TripNo varchar(15),
PatternID int,
TripType varchar(50),
ScheduleType varchar(50),
Revenue bit,
BlockNo bigint,
BlockID varchar(30),
Daymap varchar(70),
TripID varchar(30),
OrigTATripNo varchar(30),
OrigTABlockID varchar(30))

IF (EXISTS (SELECT *
   FROM INFORMATION_SCHEMA.TABLES
   WHERE TABLE_SCHEMA = 'dbo'
   AND TABLE_NAME = 'PatternDetail'))
   BEGIN
      drop table PatternDetail
   END;

Create table dbo.PatternDetail (
TripNo varchar(15),
PatternID int,
TripType varchar(50),
ScheduleType varchar(50),
Revenue bit,
BlockNo bigint,
BlockID varchar(30),
Daymap varchar(70),
TripID varchar(30),
OrigTATripNo varchar(30),
OrigTABlockID varchar(30))

IF (EXISTS (SELECT *
   FROM INFORMATION_SCHEMA.TABLES
   WHERE TABLE_SCHEMA = 'dbo'
   AND TABLE_NAME = 'Stops'))
   BEGIN
      drop table Stops
   END;

Create table dbo.Stops (
GeoID int,
GeoDescription varchar(50),
TAGeoID varchar(50),
Longitude decimal (10,8),
Latitude decimal (10,8)
)


