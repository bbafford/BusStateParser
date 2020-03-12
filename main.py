import wx

from CreateDatabase import InitalizedDB
from LoadBusStateFiles import ImportFiles
from LoadBusStateFiles import ImportScheduleMDB
#InitalizedDB()
strPath = "C:\\Users\\BBafford\\PycharmProjects\\BusState Parser\\BusStateFiles"
strProcessedPath = "C:\\Users\\BBafford\\PycharmProjects\\BusState Parser\\processed"
print(strPath)
#ImportFiles(strPath, strProcessedPath)
#ImportScheduleMDB();
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)


        butImportBusState = wx.Button(panel, label='Import Bus State Files', pos=(5, 55))
        butImportScheduleFiles = wx.Button(panel, label='Import Schedule Files', pos=(5, 15))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()