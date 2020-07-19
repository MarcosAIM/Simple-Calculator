from tkinter import Tk
from Application.App import Application

# display background color = dbg
# button background color = btg
# buttons foreground color = bfc
# buttons background color = bbg


if __name__ == '__main__':
    root = Tk()
    root.title('Calculator')
    root.iconbitmap("images/calculator_icon.ico")
    root.resizable(0, 0)
    app = Application(root, bg='black', btg='grey', dbg='black')
    root.mainloop()
