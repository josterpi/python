
import wx
from datetime import datetime

pop_time = 0
pop_last = datetime.now()
oneten_time = 0
oneten_last = None

def work_pop(event):
    global pop_last
    global pop_time
    global oneten_last
    global oneten_time
    now = datetime.now()
    if oneten_last is None:
        oneten_last = now
        return
    else:
        oneten_time += (now - oneten_last).seconds
        pop_last = now
        oneten_last = None
        filename2.SetValue(str(oneten_time))

def work_oneten(event):
    global pop_last
    global pop_time
    global oneten_last
    global oneten_time
    now = datetime.now()
    if pop_last is None:
        pop_last = now
        return
    else:
        pop_time += (now - pop_last).seconds
        oneten_last = now
        pop_last = None
        filename.SetValue(str(pop_time))

app = wx.App()
win = wx.Frame(None, title="Chess Clock", size=(300,300))

bkg = wx.Panel(win)

popButton = wx.Button(bkg, label="PoP")
popButton.Bind(wx.EVT_BUTTON, work_pop)

onetenButton = wx.Button(bkg, label="1:10")
onetenButton.Bind(wx.EVT_BUTTON, work_oneten)

filename = wx.TextCtrl(bkg)
filename2 = wx.TextCtrl(bkg)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(filename, proportion=0)
vbox.Add(popButton, proportion=1)

vbox2 = wx.BoxSizer(wx.VERTICAL)
vbox2.Add(filename2, proportion=0)
vbox2.Add(onetenButton, proportion=1)

hbox = wx.BoxSizer()
hbox.Add(vbox, proportion=0)
hbox.Add(vbox2, proportion=1)
#hbox.Add(filename, proportion=1, flag=wx.EXPAND)
#hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)

bkg.SetSizer(hbox)
win.Show()

app.MainLoop()
