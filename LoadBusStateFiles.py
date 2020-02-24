import csv
import os
import pyodbc

def ImportFiles(strPath):
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
def ImportScheduleMDB(strMDBPath):
    conn = pyodbc.connect('DSN=BWSchedule')
    c = conn.cursor()

    connLog = pyodbc.connect('DSN=BuswareLogs')
    cLog = connLog.cursor()

    c.execute ("select TripNo, PatternID, TripType, ScheduleType, Revenue, BlockNo, BlockID, Daymap, TripID, OrigTATripNo, OrigTABlockID from Trip")
    result = c.fetchall()
    for row in result:
        print(row)
        #insert the values from the mdb into the sql database
        cLog.execute ('insert into ')


