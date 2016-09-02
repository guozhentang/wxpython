# -*- coding: utf-8 -*-



"""
��д��frame,һ��Ҫ���ø���ĳ�ʼ���������ң�һ��Ҫ������ȷ�Ĳ���
frame,panel�Ǵ��ڣ�panel�Ǹ��߼����õ�frame. ע�����˳�򣬶��� 1�������ڣ�2��ID,  ѧ���Ĺؼ��ֲ���  size, pos,��û�и����ڣ���ΪNone,  ����ϵͳ����ID������д-1
wx.EVT_MOTION ������ƶ��¼�����һ�Σ�����һ�Σ�ͬʱ��event.GetPosition()��ȡ�����������ڴ��ڵ�����
wx.StaticText��������tkinter���labelһ����дһЩtext.�����������ڣ�ID,�ַ���
wx.TextCtrl,�൱��tkinter�е�entry, ���Զ�̬д�����ݡ�
"""

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,-1,"My frame",size=(400,800))
        self.panel=wx.Panel(self,-1,size=(400,400))
        self.panel.Bind(wx.EVT_MOTION, self.OnMove)
        self.text=wx.TextCtrl(self.panel, -1, "hello",pos=(40, 20))
        
       



        self.static_text=wx.StaticText(self.panel, -1,"pos:",pos=(10,20))
    
    
    def OnMove(self,event):
        pos=event.GetPosition()
        print(pos)
        self.text.SetValue("%s %s" %(pos.x, pos.y))


if __name__ == '__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()