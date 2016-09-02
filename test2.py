# -*- coding: utf-8 -*-


"""
wx.StaticBitmap  和wx.StaticText一样，两者可以互补成为tkinter里的label
wx.Image创建图像对象,参数是（路径，格式），并且对象可以自己转换格式，比如采用ConvertToBitmap()
"""

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,-1,"MyFrame",size=(800,400))
        self.panel=wx.Panel(self, -1)
        tmp_jpg=wx.Image(r"D:\wxpython\wxpython.jpg",wx.BITMAP_TYPE_JPEG)
        self.bitmap=tmp_jpg.ConvertToBitmap()
        self.staticbitmap=wx.StaticBitmap(self.panel, -1,self.bitmap)


class MyApp(wx.App):
    def OnInit(self):
        self.frame=MyFrame()
        
        self.frame.Show()
        return True

if __name__=="__main__":
    app=MyApp()
    app.MainLoop()