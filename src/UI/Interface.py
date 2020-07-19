import tkinter as tk
from tkinter import *
import tkinter.font as tk_font


class Display(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.display_value = StringVar()
        self.display_value.set(0.0)
        self.display = Label(self, justify=LEFT, anchor='e', textvariable=self.display_value)
        self.display.grid(row=0, column=0, columnspan=3, padx=40, pady=10)
        font_style = tk_font.Font(family="Times", size=12)
        self.display.config(fg='black', bg='grey', width=40, height=3, borderwidth=5, relief="sunken", font=font_style)
        self.pack()

    def update_display(self, value):
        self.display_value.set(value)

    def configure_label_colors(self, fg, bg):
        self.display.config(fg=fg, bg=bg)


class ButtonsGrid(tk.Frame):
    def __init__(self, master=None, pressed_value=None, bfc='white', bbg='black', **kw, ):
        super().__init__(master, **kw)
        self.pressed_value = pressed_value
        self.bfc = bfc
        self.bbg = bbg
        # BUTTON NUMBERS CREATION
        self.number_buttons = []
        for number in range(0, 10):
            self.number_buttons.append(tk.Button(self))
        # BUTTON ADD, DOT, MINUS, EQUALS, DIVISION, MULTIPLICATION
        self.button_add = tk.Button(self)
        self.button_subtract = tk.Button(self)
        self.button_multiply = tk.Button(self)
        self.button_divide = tk.Button(self)
        self.button_equals = tk.Button(self)
        self.button_clear = tk.Button(self)
        self.button_dot = tk.Button(self)

        self.config_buttons()
        self.config_function()
        self.position_buttons()
        self.pack()

    # configure buttons with color, and text, and size
    def config_buttons(self):
        for number in range(1, 10):
            self.number_buttons[number].config(text=number, padx=40, pady=20, bg=self.bbg, fg=self.bfc)
        self.number_buttons[0].config(text='0', padx=88, pady=20, bg=self.bbg, fg=self.bfc)

        self.button_dot.config(text='.', padx=42, pady=20, bg=self.bbg, fg=self.bfc)
        self.button_subtract.config(text='-', padx=40, pady=20, bg=self.bbg, fg=self.bfc)
        self.button_divide.config(text='/', padx=40, pady=20, bg=self.bbg, fg=self.bfc)
        self.button_multiply.config(text='*', padx=40, pady=20, bg=self.bbg, fg=self.bfc)
        self.button_clear.config(text='Clear', padx=28, pady=20, bg=self.bbg, fg=self.bfc)
        self.button_equals.config(text='=', padx=39, pady=55, bg=self.bbg, fg=self.bfc)
        self.button_add.config(text='+', padx=39, pady=55, bg=self.bbg, fg=self.bfc)

    # position buttons
    def position_buttons(self):
        # position numbers
        row = 5
        column = 0
        # position number 0
        self.number_buttons[0].grid(row=row, column=column, columnspan=2)
        row = 4
        # position number 1-9
        for number in range(1, 10):
            self.number_buttons[number].grid(row=row, column=column)
            if number % 3:
                column += 1
            else:
                column = 0
                row -= 1
        # position all other buttons
        self.button_clear.grid(row=1, column=0)
        self.button_divide.grid(row=1, column=1)
        self.button_multiply.grid(row=1, column=2)
        self.button_subtract.grid(row=1, column=3)
        self.button_add.grid(row=2, column=3, rowspan=2)
        self.button_equals.grid(row=4, column=3, rowspan=2)
        self.button_dot.grid(row=5, column=2)

    def config_function(self):
        self.number_buttons[0].config(command=lambda: self.pressed_value(0))
        self.number_buttons[1].config(command=lambda: self.pressed_value(1))
        self.number_buttons[2].config(command=lambda: self.pressed_value(2))
        self.number_buttons[3].config(command=lambda: self.pressed_value(3))
        self.number_buttons[4].config(command=lambda: self.pressed_value(4))
        self.number_buttons[5].config(command=lambda: self.pressed_value(5))
        self.number_buttons[6].config(command=lambda: self.pressed_value(6))
        self.number_buttons[7].config(command=lambda: self.pressed_value(7))
        self.number_buttons[8].config(command=lambda: self.pressed_value(8))
        self.number_buttons[9].config(command=lambda: self.pressed_value(9))
        self.button_clear.config(command=lambda: self.pressed_value(-1))
        self.button_divide.config(command=lambda: self.pressed_value(-2))
        self.button_multiply.config(command=lambda: self.pressed_value(-3))
        self.button_subtract.config(command=lambda: self.pressed_value(-4))
        self.button_add.config(command=lambda: self.pressed_value(-5))
        self.button_equals.config(command=lambda: self.pressed_value(-6))
        self.button_dot.config(command=lambda: self.pressed_value(-7))
