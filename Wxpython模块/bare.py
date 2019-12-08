'''
作者:lg
日期:2019/12/6
文件描述:
缺陷：
'''

import wx  # 1


class App(wx.App):  # 2
    def OnInit(self):  # 3
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True


app = App()  # 4
app.MainLoop()  # 5
