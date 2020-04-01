go
IF EXISTS ( SELECT *
            FROM   sysobjects
            WHERE  id = object_id(N'[dbo].[InsertFileLogs]')
                   and OBJECTPROPERTY(id, N'IsProcedure') = 1 )
BEGIN
    DROP PROCEDURE [dbo].[InsertFileLogs]
END
go


create procedure InsertFileLogs
(	@ProcessedFileName varchar(100)
	)
As
begin
	insert into [dbo].FileLog(
	ProcessedFileName
	)
	values
	(@ProcessedFileName
	)
end
go