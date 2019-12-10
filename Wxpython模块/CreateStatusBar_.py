'''
作者:lg
日期:2019/12/10
文件描述:
缺陷：
'''

import wx
import wx.py.images as images


class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',
                          size=(300, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()  # 1 创建状态栏
        toolbar = self.CreateToolBar()  # 2 创建工具栏
        toolbar.AddSimpleTool(wx.NewId(), images.getPyBitmap(), 'New', "Long help for 'New'")  # 3 给工具栏增加一个工具
        toolbar.Realize()  # 4 准备显示工具栏
        menuBar = wx.MenuBar()  # 创建菜单栏
        # 创建两个菜单
        menu1 = wx.Menu()
        menuBar.Append(menu1, '&File')
        menu2 = wx.Menu()
        # 6 创建菜单的项目
        menu2.Append(wx.NewId(), '&Copy', 'Copy in status bar')
        menu2.Append(wx.NewId(), 'C&ut', '剪切')

        menu2.Append(wx.NewId(), 'Paste', '粘贴')
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), '&Options...', 'Display Options')
        menuBar.Append(menu2, '& Edit')  # 在菜单栏上附上菜单

        # 自己加一些代码
        menu3 = wx.Menu()
        menu3.Append(wx.NewId(), 'version', 'version info')
        menu3.Append(wx.NewId(), 'register', 'register info')
        menuBar.Append(menu3, '& Version')

        self.SetMenuBar(menuBar)  # 在框架上附上菜单栏


if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
