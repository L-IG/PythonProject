'''
作者:lg
日期:2019/12/8
文件描述:
缺陷：
'''

'''Spare.py is a starting point for a wxPython program.'''  # 2
import wx


class Frame(wx.Frame):  # 3
    pass


class App(wx.App):


    def OnInit(self):
        self.frame = Frame(parent=None, title='Spare')  # 4
        self.frame.Show()
        self.SetTopWindow(self.frame)  # 5
        return True


if __name__ == '__main__':  # 6
    app = App()
    app.MainLoop()
