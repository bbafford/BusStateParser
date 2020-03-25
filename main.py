import wx

from CreateDatabase import InitalizedDB
from LoadBusStateFiles import ImportFiles
from LoadBusStateFiles import ImportScheduleMDB
#InitalizedDB()
strPath = "C:\\Users\\BBafford\\PycharmProjects\\BusState Parser\\BusStateFiles"
strProcessedPath = "C:\\Users\\BBafford\\PycharmProjects\\BusState Parser\\processed"
print(strPath)
ImportFiles(strPath, strProcessedPath)
#ImportScheduleMDB();

# class MainFrame(wx.Frame):
#
#     def __init__(self):
#         super().__init__(parent=None, title='Hello World')
#         panel = wx.Panel(self)
#
#         butImportBusState = wx.Button(panel, label='Import Bus State Files', pos=(5, 55))
#
#         butImportScheduleFiles = wx.Button(panel, label='Import Schedule Files', pos=(5, 15))
#
#         menubar = wx.MenuBar()
#         fileMenu = wx.Menu()
#         fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
#
#         wx.StaticText(self, label='x:', pos=(50, 10))
#         wx.StaticText(self, label='y:', pos=(50, 30))
#         self.st1 = wx.StaticText(self, label='', pos=(30, 10))
#         self.st2 = wx.StaticText(self, label='', pos=(30, 30))
#
#         menubar.Append(fileMenu, '&File')
#         self.SetMenuBar(menubar)
#
#         self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
#         self.Bind(wx.EVT_MOVE,self.OnMove)
#         #self.SetSize((600, 400))
#         self.SetTitle('Simple menu')
#         self.Centre()
#
#       #  self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
#         self.Bind(wx.EVT_BUTTON,self.Button1,butImportBusState)
#         self.Show()
#
#     def OnQuit(self, e):
#             self.Close()
#
#     def OnMove(self, e):
#
#         x, y = e.GetPosition()
#         self.st1.SetLabel(str(x))
#         self.st2.SetLabel(str(y))
#
#     def Button1(self, e):
#         self.st1.SetLabel("PUSHED")
#
#
# def main():
#
#     app = wx.App()
#     frame = MainFrame()
#
#     app.MainLoop()
#
# if __name__ == '__main__':
#
#     main()

