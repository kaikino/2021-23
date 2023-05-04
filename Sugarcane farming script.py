try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

import pyautogui as p

import time
import random

class Bot:
    def __init__(self, parent):

        self.startB=tk.Button(parent,text="Start",command=self.start,bg="green",fg="white",font=10)
        self.startB.pack()

        self.seconds = 5
        self.timer = tk.Label(parent, text="Idle")
        self.timer.pack()

        self.dir="forwards"
        self.dirDisplay=tk.Label(parent, text="Directon")
        self.dirDisplay.pack()

    def start(self):

            self.seconds=5
            self.refresh_label()

    def refresh_label(self):

        if self.seconds==-1:
            self.timer.config(text="Running")
            self.farm()
            p.keyDown("space")
        else:
            self.timer.configure(text="%i s" % self.seconds)
            self.timer.after(1000, self.refresh_label)
            self.seconds -= 1

    def farm(self):
    
        
        if self.dir=="forwards":
            p.keyDown("d")
        else:
            p.keyDown("s")
        self.dirDisplay.after(16000+random.randint(300,800),self.alternate)

    def alternate(self):
        if self.dir=="forwards":
            p.keyUp("d")
            self.dir="backwards"
        else:
            p.keyUp("s")
            self.dir="forwards"
        time.sleep(random.randint(1,5)/10)
        self.farm()
        self.dirDisplay.config(text="Direction: "+self.dir)

if __name__ == "__main__":
    root = tk.Tk()
    macro = Bot(root)
    root.attributes('-topmost',True)
    root.mainloop()
