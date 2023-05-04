try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

import pyautogui as p

import time

class Bot:
    def __init__(self, parent):

        self.dir="left"
        self.layer=0
        self.row=33
        self.stop=False

        self.startB=tk.Button(parent,text="Start",command=self.start)
        self.startB.grid(row=1,column=1)

        self.switch=tk.Button(parent,text="Switch",command=self.alternate)
        self.switch.grid(row=1,column=2)

        self.stopB=tk.Button(parent,text="Stop",command=self.abort)
        self.stopB.grid(row=1,column=3)

        self.timer = tk.Label(parent, text="Idle")
        self.timer.grid(row=2,column=2)

        self.dirDisplay=tk.Label(parent, text="Direction")
        self.dirDisplay.grid(row=3,column=1)

        self.rowDisplay=tk.Label(parent, text="Row")
        self.rowDisplay.grid(row=3,column=2)

        self.layerDisplay=tk.Label(parent, text="Layer")
        self.layerDisplay.grid(row=3,column=3)

    def start(self):
        self.seconds=3
        self.refresh_label()

    def refresh_label(self):

        if self.seconds==-1:
            self.timer.config(text="Running")
            self.farm()
        else:
            self.timer.configure(text="%i s" % self.seconds)
            self.timer.after(1000, self.refresh_label)
            self.seconds -= 1

    def farm(self):
        if self.stop:
            return
        self.row+=1
        self.rowDisplay.configure(text="R %i" % self.row)
        if self.row==34:
            self.row=0
            self.layer+=1
            self.layerDisplay.configure(text="L %i" % self.layer)
            if self.layer%4==0:
                p.keyDown("space")
                time.sleep(3)
                
        if self.layer%2==1:
            p.keyUp("s")
            p.keyDown("w")
        else:
            p.keyUp("w")
            p.keyDown("s")
        p.keyDown("space")
        if self.dir=="right":
            p.keyUp("a")
            p.keyDown("d")
        else:
            p.keyUp("d")
            p.keyDown("a")
        self.dirDisplay.after(35000,self.alternate)

    def alternate(self):
        if self.dir=="left":
            self.dir="right"
        else:
            self.dir="left"
        self.farm()
        self.dirDisplay.config(text="D: "+self.dir)

    def abort(self):
        self.stop=True
        p.keyUp("s")
        p.keyUp("w")
        p.keyUp("a")
        p.keyUp("d")
        p.keyUp("space")
if __name__ == "__main__":
    root = tk.Tk()
    macro = Bot(root)
    #root.
    root.attributes('-topmost',True)
    root.mainloop()
