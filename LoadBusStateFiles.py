import csv
import os
import pyodbc
import zipfile

def ImportFiles(strPath,strProcessedPath,strUnzippedPath):
    conn = pyodbc.connect('DSN=BuswareLogs')
    c = conn.cursor()
    args=[]
    listProcessedFileNames = []
    print (strPath)
    listProcessedFileNames = PopulateProcessedFileNames()
    print (f'Previously processed files: {len(listProcessedFileNames)}')
 #   print (len(listProcessedFileNames))

    for filename in os.listdir(strPath):
        print (strPath + "\\" + filename)
        if boolFileProcessed(filename,listProcessedFileNames) ==0:
            #unzip the file to the local path
            with zipfile.ZipFile(strPath + "\\" + filename,"r") as zip_ref:
                zip_ref.extractall(strUnzippedPath)
            unzipped_filename = filename[:-4]

            with open(strUnzippedPath + unzipped_filename) as csv_file:
                try:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                except:
                    print ("Data not good")

                line_count = 0
                try:
                    for row in csv_reader:
                        if line_count == 0 or line_count==1:
                            #Get the column names.  We can discard these
                            #print(f'Column names are {", ".join(row)}')
                            line_count += 1
                        else:
                           # if row[24] == 3 or row[24] == 4 or row[24] ==5:
                            line_count += 1
                            #break apart the CSV into a list that we can insert into the database
                            args=(row[0],row[1],row[2],row[3],row[6],row[8],row[9],row[10],row[11],row[14],row[20],row[21], filename,row[24],row[32])

                            print(f'Column names are {", ".join(args)}')
                            c.execute("{call buswarelogs.dbo.InsertBusStateEntry(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}", args)
                except:
                    print ("punch out")
                print(f'Processed {line_count} lines.')
                c.execute("{call buswarelogs.dbo.InsertFileLogs(?)}",filename)

                conn.commit()
                #when the file is done, move it to a processed directory
                listProcessedFileNames.append(filename)
                csv_file.close()

           # os.rename(strPath + "\\" + filename,strProcessedPath + "\\" + filename)

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

def PopulateProcessedFileNames():
    conn = pyodbc.connect('DSN=BuswareLogs')
    c = conn.cursor()
    listProcessedFileNames =[]
    c.execute ("select ProcessedFileName from FileLog")
    for row in c.fetchall():
        listProcessedFileNames.append(row[0])

    return listProcessedFileNames

def boolFileProcessed(strFileName,listProcessedFileNames):
    for element in listProcessedFileNames:
        if element == strFileName:
            return 1
    return 0