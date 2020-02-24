from CreateDatabase import InitalizedDB
from LoadBusStateFiles import ImportFiles

InitalizedDB()
strPath = "C:\\Users\\BBafford\\PycharmProjects\\BusState Parser\\BusStateFiles"
print(strPath)
ImportFiles(strPath)

