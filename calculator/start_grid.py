import tkinter as tk
from tkinter import ttk, Button

class StartGrid:   
    def __init__(self, app):
        self.app = app
        self.Button_frame = app.Button_frame
        self.ipadx = app.ipadx
        self.ipady = app.ipady
        self.button_width = app.button_width
        self.add_digit_to = app.add_digit_to
        self.addition = app.addition
        self.subtract = app.subtract
        self.divide = app.divide
        self.multiply = app.multiply
        self.solve = app.solve
        self.make_it_decimal = app.make_it_decimal
        self.delete_all = app.delete_all
        self.back_space_10r2 = app.back_space_10r2
        self.window = app.window
        self.switch = app.switch

    def start_grid(self):
        for idx, i in enumerate(range(9,-1, -1)):
            btn = ttk.Button(self.Button_frame, text= str(i), style='my.TButton', command=lambda i=i: self.add_digit_to(i), width=self.button_width)
            if i == 0:
                btn.grid(row=4, column=1, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)
            else:
                btn.grid(row=idx // 3 + 1, column=2 - idx % 3, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.btn = ttk.Button(self.Button_frame, command=self.addition, style='my.TButton', text='+', width=self.button_width)
        self.btn.grid(row=4, column=3, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.btn = ttk.Button(self.Button_frame, command=self.subtract, style='my.TButton', text='-', width=self.button_width)
        self.btn.grid(row=3, column=3, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.btn = ttk.Button(self.Button_frame, command=self.divide, style='my.TButton', text='÷', width=self.button_width)
        self.btn.grid(row=1, column=3, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.btn = ttk.Button(self.Button_frame, command=self.multiply, style='my.TButton', text='x', width=self.button_width)
        self.btn.grid(row=2, column=3, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.btn = ttk.Button(self.Button_frame, command=self.solve, style='my.TButton', text='=', width=self.button_width)
        self.btn.grid(row=5, column=3, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.btn = ttk.Button(self.Button_frame, command=self.make_it_decimal, style='my.TButton', text='.', width=self.button_width)
        self.btn.grid(row=4, column=2, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.delete_btn = ttk.Button(self.Button_frame, text='Del', command=self.delete_all, style='my.TButton', width=self.button_width)
        self.delete_btn.grid(row=5, column=0, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.backspace_btn = ttk.Button(self.Button_frame, text='back', command=self.back_space_10r2, style='my.TButton', width=self.button_width)
        self.backspace_btn.grid(row=5, column=1, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.quit_btn = ttk.Button(self.Button_frame, text='quit', command=self.window.quit, style='my.TButton', width=self.button_width)
        self.quit_btn.grid(row=5, column=2, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)

        self.uord_btn = ttk.Button(self.Button_frame, text='1 or 2', command=self.switch, style='my.TButton', width=self.button_width)
        self.uord_btn.grid(row=4, column=0, padx=5, pady=5, ipadx=self.ipadx, ipady=self.ipady)