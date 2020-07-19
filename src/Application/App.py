import tkinter as tk
from UI.Interface import Display, ButtonsGrid
from Application.Messenger import Messenger


class Application(tk.Frame):
    def __init__(self, master=None, btg='gray', dbg='white', bfc='white', bbg='black', **kw):
        super().__init__(master, **kw)
        self.dbg = dbg
        self.bfc = bfc
        self.bbg = bbg
        self.display = Display(self, bg=self.dbg)
        self.messenger = Messenger(self.display)
        self.buttons = ButtonsGrid(self, self.messenger.button_pressed, self.bfc, self.bbg, bg=btg)
        self.pack()
