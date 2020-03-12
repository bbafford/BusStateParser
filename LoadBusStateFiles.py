import csv
import os
import pyodbc

def ImportFiles(strPath,strProcessedPath):
    conn = pyodbc.connect('DSN=BuswareLogs')
    c = conn.cursor()
    args=[]
    print (strPath)
    for filename in os.listdir(strPath):
        print (strPath + "\\" + filename)
        with open(strPath + "\\" + filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count==1:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:

                   # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    line_count += 1
                    args=(row[0],row[1],row[2],row[3],row[6],row[8],row[9],row[10],row[11],row[14],row[20],row[21])

                    print(f'Column names are {", ".join(args)}')
                   # c.callproc("busstatelogs.dbo.InsertBusStateEntry",args)
                    c.execute("{call buswarelogs.dbo.InsertBusStateEntry(?,?,?,?,?,?,?,?,?,?,?,?)}", (args))

            print(f'Processed {line_count} lines.')
            conn.commit()
            #when the file is done, move it to a processed directory
            csv_file.close()

            os.rename(strPath + "\\" + filename,strProcessedPath + "\\" + filename)

def ImportScheduleMDB():
    conn = pyodbc.connect('DSN=BWSchedule')
    c = conn.cursor()

    connLog = pyodbc.connect('DSN=BuswareLogs')
    cLog = connLog.cursor()

#Get all of the rows from the Schedule trip file
    c.execute ("select TripNo, PatternID, TripType, ScheduleType, Revenue, BlockNo, BlockID, Daymap, TripID, OrigTATripNo, OrigTABlockID from Trip")
    result = c.fetchall()
    cLog.executemany('insert into trip (TripNo,PatternID,TripType,ScheduleType,Revenue,BlockNo, BlockID,Daymap,TripID, OrigTATripNo,OrigTABlockID) values(?,?,?,?,?,?,?,?,?,?,?)', result)
    cLog.commit()

#Get all of the rows from Tripdetail
    c.execute("select TripNo, PassingTIme, TimepointID, RunID from TripDetail")
    result = c.fetchall()
    cLog.executemany('insert into tripdetail (TripNo, PassingTIme, TimepointID, RunID) values(?,?,?,?)', result)
    cLog.commit()

#Get all of the stops
    c.execute("select GeoID, GeoDescription, TAGeoID,Longitude,Latitude from Stops")
    result = c.fetchall()
    cLog.executemany('insert into Stops (GeoID, GeoDescription, TAGeoID,Longitude,Latitude) values(?,?,?,?,?)', result)
    cLog.commit()
#get all of the pattern data
    c.execute("select PatternID, TARoute, PatternName,Direction,CDRoute, CDVariation,TAPatternID from Pattern")
    result = c.fetchall()
    cLog.executemany('insert into Pattern (PatternID, TARoute, PatternName,Direction,CDRoute, CDVariation,TAPatternID ) values(?,?,?,?,?,?,?)', result)
    cLog.commit()
