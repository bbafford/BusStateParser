
IF (EXISTS (SELECT *
   FROM INFORMATION_SCHEMA.TABLES
   WHERE TABLE_SCHEMA = 'dbo'
   AND TABLE_NAME = 'FileLog'))
   BEGIN
      drop table FileLog
   END;

create table dbo.FileLog(
ProcessedFileName varchar(100)
)