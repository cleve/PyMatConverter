# -*- coding: utf-8 -*-
# generated by wxGlade HG on Tue Jan 25 16:54:38 2011

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class Acercade(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Acercade.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_2 = wx.Panel(self, -1)
        self.bitmap_1 = wx.StaticBitmap(self.panel_2, -1, wx.Bitmap("img/logo.png", wx.BITMAP_TYPE_ANY), style=wx.SIMPLE_BORDER)
        self.label_2 = wx.StaticText(self.panel_2, -1, "Version 1.0\n\nAplicacion generada con Python\n y Fedora Linux.\n\nMauricio Cleveland\n\nmauricio.cleveland@gmail.com\n\nwww.universodigital.cl ", style=wx.ALIGN_CENTRE)
        self.button_2 = wx.Button(self.panel_2, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.salir, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Acercade.__set_properties
        self.SetTitle("Acerca De")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("img/pulsar.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Acercade.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_4.Add(self.bitmap_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 10)
        sizer_4.Add(self.label_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 20)
        sizer_4.Add(self.button_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 10)
        self.panel_2.SetSizer(sizer_4)
        sizer_3.Add(self.panel_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def salir(self, event): # wxGlade: Acercade.<event_handler>
        self.Destroy()

# end of class Acercade


