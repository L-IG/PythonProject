'''
作者:lg
日期:2019/12/10
文件描述:
缺陷：
'''

import wx


class InsertFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button', size=(300, 100))
        panel = wx.Panel(self)  # 创建画板
        button = wx.Button(panel, label='Close', pos=(125, 10),
                           size=(50, 50))  # 将按钮添加到画板
        # 绑定按钮的单击事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        # 绑定窗口的关闭事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    # app = wx.PySimpleApp()
    app = wx.App()
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
