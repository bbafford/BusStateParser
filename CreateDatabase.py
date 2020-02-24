import pyodbc


def InitalizedDB():

    CreateDatabase(".\sqlCreateBusState.sql")
    CreateStoredProcedures(".\sqlCreateStoredProcedures.sql")
    return 0

def CreateDatabase(SQLFile):
    executeScriptsFromFile(SQLFile)
    return 0

def CreateStoredProcedures(SQLFile):
  #  executeScriptsFromFile(SQLFile)
    return 0

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    conn = pyodbc.connect('DSN=BuswareLogs')
    c = conn.cursor()
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        print(command)
        c.execute(command)
    c.close()
