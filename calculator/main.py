import tkinter as tk
from tkinter import ttk, Button
from comp_operations import CompOperations
from start_grid import StartGrid
import time


class CalculatorApp:
    def __init__(self, window):
        self.window = window
        self.window.title('Calculator')
        self.window.geometry('340x440')
        self.mode_label_inf = None
        self.num1lay = None
        self.num2lay = None
        self.anslay = None
        self.input_frame = None

        self.inam_qe = 3
        self.inam_ms = 4
        self.inam_distance = 4
        self.inam_slop = 4
        self.inam_fanc = 3
        self.inam_trig = 6

        self.ops = CompOperations()

        self.lay_qe = {
            1: 'a',
            2: 'b=',
            3: 'c='}
        self.lay_ms = {
            1: 'x1=',
            2: 'y1=',
            3: 'x2=',
            4: 'y2='}
        self.lay_distance = {
            1: 'x1=',
            2: 'y1=',
            3: 'x2=',
            4: 'y2='}
        self.lay_slop = {
            1: 'x1=',
            2: 'y1=',
            3: 'x2=',
            4: 'y2='}
        self.lay_fanc = {
            1: 'x=',
            2: 'y=',
            3: 'm='}
        self.lay_trig = {
            1: 'x1=',
            2: 'y1=',
            3: 'a=',
            4: 'x2=',
            5: 'y2=',
            6: 'b='}

        self.in1 = None
        self.in2 = None
        self.in3 = None
        self.in4 = None
        self.in5 = None
        self.in6 = None
        self.ans = None

        self.lay1 = None
        self.lay2 = None
        self.lay3 = None
        self.lay4 = None
        self.lay5 = None
        self.lay6 = None


        self.solve_button = None

        self.num1 = float(0)
        self.num2 = float(0)
        self.ans = float(0)
        self._1or2 = 1
        self.is_it_decimal1 = 0
        self.decimal_length1 = 0
        self.is_it_decimal2 = 0
        self.decimal_length2 = 0
        self.operation = None
        self.operations_list = {1: self.addition, 2: self.subtract, 3: self.multiply, 4: self.divide, }
        self.calculatormode = 1
        self.calculatormode_list = {
            1: 'Basic mode',
            2: 'Quadratic equation',
            3: 'Middle of segment',
            4: 'Distance',
            5: 'Slope',
            6: 'Function',
            7: 'Trigonometry'}

        self.window.bind("<Escape>", lambda esc: self.hide_menu())
        self.window.bind("<Button-1>", self.check_click_outside_menu)

        self.style = ttk.Style()
        self.style.configure('my.TButton', font=('Arial', 18))

        self.ipadx = 5
        self.ipady = 5
        self.button_width = 4

        self.mode_label_inf = ttk.Label(self.window, text=f"mode: {self.calculatormode_list[self.calculatormode]}",
                                        font=('arial', 10))
        self.mode_label_inf.pack(pady=2)

        self.num1lay = ttk.Label(window, text='', font=('arial', 18))
        self.num1lay.pack(pady=5)

        self.num2lay = ttk.Label(window, text='', font=('arial', 18))
        self.num2lay.pack(pady=5)

        self.anslay = ttk.Label(window, text='', font=('arial', 18))
        self.anslay.pack(pady=5)

        self.Button_frame = ttk.Frame(self.window)
        self.Button_frame.pack()

        grid = StartGrid(self)
        grid.start_grid()

        self.menu_open = False
        self.menu_button = ttk.Button(self.window, text="≡", command=self.toggle_menu, width=4)
        self.menu_button.place(x=10, y=10)

        # Side menu frame
        self.menu_frame = tk.Frame(self.window, width=150, height=420, bg="#eeeeee")
        self.menu_frame.place(x=-150, y=0)  # Hidden initially

        # Add buttons to menu
        self.mode_label = tk.Label(self.menu_frame, text="Modes", bg="#eeeeee", font=("Arial", 14))
        self.mode_label.pack(pady=10)

        self.basic_mode_btn = ttk.Button(self.menu_frame, text="Basic", command=self.set_to_basic)
        self.basic_mode_btn.pack(pady=5)

        self.quadratic_equation_mode_btn = ttk.Button(self.menu_frame, text="quadratic equation",
                                                      command=self.set_to_qe)
        self.quadratic_equation_mode_btn.pack(pady=5)

        self.mid_segment_mode_btn = ttk.Button(self.menu_frame, text="the middle of a segment", command=self.set_to_ms)
        self.mid_segment_mode_btn.pack(pady=5)

        self.distance_mode_btn = ttk.Button(self.menu_frame, text="distance", command=self.set_to_distance)
        self.distance_mode_btn.pack(pady=5)

        self.slop_mode_btn = ttk.Button(self.menu_frame, text="slop", command=self.set_to_slop)
        self.slop_mode_btn.pack(pady=5)

        self.function_mode_btn = ttk.Button(self.menu_frame, text="function", command=self.set_to_fanc)
        self.function_mode_btn.pack(pady=5)

        self.trigonometry_mode_btn = ttk.Button(self.menu_frame, text="trigonometry", command=self.set_to_trig)
        self.trigonometry_mode_btn.pack(pady=5)

    def clear(self):
        if self.Button_frame:
            for widget in self.Button_frame.winfo_children():
                widget.destroy()
            self.Button_frame.destroy()
            self.Button_frame = None

        if self.num1lay:
            self.num1lay.destroy()
            self.num1lay = None
        if self.num2lay:
            self.num2lay.destroy()
            self.num2lay = None
        if self.anslay:
            self.anslay.destroy()
            self.anslay = None

        if self.lay1:
            self.lay1.destroy()
            self.lay1 = None
        if self.lay2:
            self.lay2.destroy()
            self.lay2 = None
        if self.lay3:
            self.lay3.destroy()
            self.lay3 = None
        if self.lay4:
            self.lay4.destroy()
            self.lay4 = None
        if self.lay5:
            self.lay5.destroy()
            self.lay5 = None
        if self.lay6:
            self.lay6.destroy()
            self.lay6 = None


        if self.in1:
            self.in1.destroy()
            self.in1 = None
        if self.in2:
            self.in2.destroy()
            self.in2 = None
        if self.in3:
            self.in3.destroy()
            self.in3 = None
        if self.in4:
            self.in4.destroy()
            self.in4 = None
        if self.in5:
            self.in5.destroy()
            self.in5 = None
        if self.in6:
            self.in6.destroy()
            self.in6 = None
        if self.solve_button:
            self.solve_button.destroy()
            self.solve_button = None




        if self.mode_label_inf:
            self.mode_label_inf.destroy()
            self.mode_label_inf = None
            self.mode_label_inf = ttk.Label(self.window, text=f"mode: {self.calculatormode_list[self.calculatormode]}",
                                            font=('arial', 10))
            self.mode_label_inf.pack(pady=2)





    def solve_quadratic(self):
        try:
            a = float(self.in1.get())
            b = float(self.in2.get())
            c = float(self.in3.get())
            result = self.ops.qe(a, b, c)
            self.anslay.config(text=result)
        except ValueError:
            self.anslay.config(text="Invalid input")


    def set_to_qe(self):
        if self.calculatormode == 1:
            self.delete_all()
        self.calculatormode = 2
        self.clear()
        self.window.geometry('340x440')

        self.lay1 = ttk.Label(self.window, text='a=', font=('arial', 18))
        self.lay1.pack(pady=5)
        self.in1 = ttk.Entry(self.window, font=('arial', 18))
        self.in1.pack(pady=5)

        self.lay2 = ttk.Label(self.window, text='b=', font=('arial', 18))
        self.lay2.pack(pady=5)
        self.in2 = ttk.Entry(self.window, font=('arial', 18))
        self.in2.pack(pady=5)

        self.lay3 = ttk.Label(self.window, text='c=', font=('arial', 18))
        self.lay3.pack(pady=5)
        self.in3 = ttk.Entry(self.window, font=('arial', 18))
        self.in3.pack(pady=5)

        self.solve_button = ttk.Button(text="solve", command=self.solve_quadratic, style='my.TButton')
        self.solve_button.pack()

        self.anslay = ttk.Label(self.window, text="", font=('Arial', 18))
        self.anslay.pack(pady=10)



        self.mode_label_inf.config(text=f"Mode: {self.calculatormode_list[self.calculatormode]}", font=('arial', 10))
        self.menu_frame.place(x=0, y=0)
        self.menu_frame.tkraise()


    def solve_ms(self):
        try:
            x1 = float(self.in1.get())
            y1 = float(self.in2.get())
            x2 = float(self.in3.get())
            y2 = float(self.in4.get())
            result = self.ops.ms(x1, y1, x2, y2)
            self.anslay.config(text=result)
        except ValueError:
            self.anslay.config(text="Invalid input")

    def set_to_ms(self):
        if self.calculatormode == 1:
            self.delete_all()
        self.calculatormode = 3
        self.clear()
        self.window.geometry('340x460')

        self.lay1 = ttk.Label(self.window, text='x1=', font=('arial', 18))
        self.lay1.pack(pady=5)
        self.in1 = ttk.Entry(self.window, font=('arial', 18))
        self.in1.pack(pady=5)

        self.lay2 = ttk.Label(self.window, text='y1=', font=('arial', 18))
        self.lay2.pack(pady=5)
        self.in2 = ttk.Entry(self.window, font=('arial', 18))
        self.in2.pack(pady=5)

        self.lay3 = ttk.Label(self.window, text='x2=', font=('arial', 18))
        self.lay3.pack(pady=5)
        self.in3 = ttk.Entry(self.window, font=('arial', 18))
        self.in3.pack(pady=5)

        self.lay4 = ttk.Label(self.window, text='y2=', font=('arial', 18))
        self.lay4.pack(pady=5)
        self.in4 = ttk.Entry(self.window, font=('arial', 18))
        self.in4.pack(pady=5)

        self.solve_button = ttk.Button(text="solve", command=self.solve_ms, style='my.TButton')
        self.solve_button.pack()

        self.anslay = ttk.Label(self.window, text="", font=('Arial', 18))
        self.anslay.pack(pady=10)

        self.mode_label_inf.config(text=f"Mode: {self.calculatormode_list[self.calculatormode]}", font=('arial', 10))
        self.menu_frame.place(x=0, y=0)
        self.menu_frame.tkraise()



    def solve_distance(self):
        try:
            x1 = float(self.in1.get())
            y1 = float(self.in2.get())
            x2 = float(self.in3.get())
            y2 = float(self.in4.get())
            result = self.ops.distance(x1, y1, x2, y2)
            self.anslay.config(text=result)
        except ValueError:
            self.anslay.config(text="Invalid input")

    def set_to_distance(self):
        if self.calculatormode == 1:
            self.delete_all()
        self.calculatormode = 4
        self.clear()
        self.window.geometry('340x460')


        self.lay1 = ttk.Label(self.window, text='x1=', font=('arial', 18))
        self.lay1.pack(pady=5)
        self.in1 = ttk.Entry(self.window, font=('arial', 18))
        self.in1.pack(pady=5)

        self.lay2 = ttk.Label(self.window, text='y1=', font=('arial', 18))
        self.lay2.pack(pady=5)
        self.in2 = ttk.Entry(self.window, font=('arial', 18))
        self.in2.pack(pady=5)

        self.lay3 = ttk.Label(self.window, text='x2=', font=('arial', 18))
        self.lay3.pack(pady=5)
        self.in3 = ttk.Entry(self.window, font=('arial', 18))
        self.in3.pack(pady=5)

        self.lay4 = ttk.Label(self.window, text='y2=', font=('arial', 18))
        self.lay4.pack(pady=5)
        self.in4 = ttk.Entry(self.window, font=('arial', 18))
        self.in4.pack(pady=5)

        self.solve_button = ttk.Button(text="solve", command=self.solve_distance, style='my.TButton')
        self.solve_button.pack()

        self.anslay = ttk.Label(self.window, text="", font=('Arial', 18))
        self.anslay.pack(pady=10)

        self.mode_label_inf.config(text=f"Mode: {self.calculatormode_list[self.calculatormode]}", font=('arial', 10))
        self.menu_frame.place(x=0, y=0)
        self.menu_frame.tkraise()


    def solve_slop(self):
        try:
            x1 = float(self.in1.get())
            y1 = float(self.in2.get())
            x2 = float(self.in3.get())
            y2 = float(self.in4.get())
            result = self.ops.slop(x1, y1, x2, y2)
            self.anslay.config(text=result)
        except ValueError:
            self.anslay.config(text="Invalid input")


    def set_to_slop(self):
        if self.calculatormode == 1:
            self.delete_all()
        self.calculatormode = 5
        self.clear()
        self.window.geometry('340x460')

        self.lay1 = ttk.Label(self.window, text='x1=', font=('arial', 18))
        self.lay1.pack(pady=5)
        self.in1 = ttk.Entry(self.window, font=('arial', 18))
        self.in1.pack(pady=5)

        self.lay2 = ttk.Label(self.window, text='y1=', font=('arial', 18))
        self.lay2.pack(pady=5)
        self.in2 = ttk.Entry(self.window, font=('arial', 18))
        self.in2.pack(pady=5)

        self.lay3 = ttk.Label(self.window, text='x2=', font=('arial', 18))
        self.lay3.pack(pady=5)
        self.in3 = ttk.Entry(self.window, font=('arial', 18))
        self.in3.pack(pady=5)

        self.lay4 = ttk.Label(self.window, text='y2=', font=('arial', 18))
        self.lay4.pack(pady=5)
        self.in4 = ttk.Entry(self.window, font=('arial', 18))
        self.in4.pack(pady=5)

        self.solve_button = ttk.Button(text="solve", command=self.solve_slop, style='my.TButton')
        self.solve_button.pack()

        self.anslay = ttk.Label(self.window, text="", font=('Arial', 18))
        self.anslay.pack(pady=10)

        self.mode_label_inf.config(text=f"Mode: {self.calculatormode_list[self.calculatormode]}", font=('arial', 10))
        self.menu_frame.place(x=0, y=0)
        self.menu_frame.tkraise()


    def solve_fanc(self):
        try:
            x = float(self.in1.get())
            y = float(self.in2.get())
            m = float(self.in3.get())

            result = self.ops.fanc(x, y, m)
            self.anslay.config(text=result)
        except ValueError:
            self.anslay.config(text="Invalid input")

    def set_to_fanc(self):
        if self.calculatormode == 1:
            self.delete_all()
        self.calculatormode = 6
        self.clear()
        self.window.geometry('340x440')

        self.lay1 = ttk.Label(self.window, text='a=', font=('arial', 18))
        self.lay1.pack(pady=5)
        self.in1 = ttk.Entry(self.window, font=('arial', 18))
        self.in1.pack(pady=5)

        self.lay2 = ttk.Label(self.window, text='b=', font=('arial', 18))
        self.lay2.pack(pady=5)
        self.in2 = ttk.Entry(self.window, font=('arial', 18))
        self.in2.pack(pady=5)

        self.lay3 = ttk.Label(self.window, text='c=', font=('arial', 18))
        self.lay3.pack(pady=5)
        self.in3 = ttk.Entry(self.window, font=('arial', 18))
        self.in3.pack(pady=5)

        self.solve_button = ttk.Button(text="solve", command=self.solve_fanc, style='my.TButton')
        self.solve_button.pack()

        self.anslay = ttk.Label(self.window, text="", font=('Arial', 18))
        self.anslay.pack(pady=10)

        self.mode_label_inf.config(text=f"Mode: {self.calculatormode_list[self.calculatormode]}", font=('arial', 10))
        self.menu_frame.place(x=0, y=0)
        self.menu_frame.tkraise()


    def solve_trig(self):
        try:
            x1 = float(self.in1.get())
            z1 = float(self.in2.get())
            x2 = float(self.in3.get())
            z2 = float(self.in4.get())
            a = float(self.in5.get())
            b = float(self.in6.get())
            result = self.ops.trig(x1, z1, x2, z2, a, b)
            self.anslay.config(text=result)
        except ValueError:
            self.anslay.config(text="Invalid input")

    def set_to_trig(self):
        if self.calculatormode == 1:
            self.delete_all()
        self.calculatormode = 7
        self.clear()
        self.window.geometry('340x610')

        self.lay1 = ttk.Label(self.window, text='x1=', font=('arial', 18))
        self.lay1.pack(pady=5)
        self.in1 = ttk.Entry(self.window, font=('arial', 18))
        self.in1.pack(pady=5)

        self.lay2 = ttk.Label(self.window, text='y1=', font=('arial', 18))
        self.lay2.pack(pady=5)
        self.in2 = ttk.Entry(self.window, font=('arial', 18))
        self.in2.pack(pady=5)

        self.lay3 = ttk.Label(self.window, text='x2=', font=('arial', 18))
        self.lay3.pack(pady=5)
        self.in3 = ttk.Entry(self.window, font=('arial', 18))
        self.in3.pack(pady=5)

        self.lay4 = ttk.Label(self.window, text='y2=', font=('arial', 18))
        self.lay4.pack(pady=5)
        self.in4 = ttk.Entry(self.window, font=('arial', 18))
        self.in4.pack(pady=5)

        self.lay5 = ttk.Label(self.window, text='a=', font=('arial', 18))
        self.lay5.pack(pady=5)
        self.in5 = ttk.Entry(self.window, font=('arial', 18))
        self.in5.pack(pady=5)

        self.lay6 = ttk.Label(self.window, text='b=', font=('arial', 18))
        self.lay6.pack(pady=5)
        self.in6 = ttk.Entry(self.window, font=('arial', 18))
        self.in6.pack(pady=5)

        self.solve_button = ttk.Button(text="solve", command=self.solve_trig, style='my.TButton')
        self.solve_button.pack()

        self.anslay = ttk.Label(self.window, text="", font=('Arial', 18))
        self.anslay.pack(pady=10)

        self.mode_label_inf.config(text=f"Mode: {self.calculatormode_list[self.calculatormode]}", font=('arial', 10))
        self.menu_frame.place(x=0, y=0)
        self.menu_frame.tkraise()

    def set_to_basic(self):
        self.calculatormode = 1
        self.clear()
        self.window.geometry('340x440')

        self.num1lay = ttk.Label(self.window, text='', font=('arial', 18))
        self.num1lay.pack(pady=5)

        self.num2lay = ttk.Label(self.window, text='', font=('arial', 18))
        self.num2lay.pack(pady=5)

        self.anslay = ttk.Label(self.window, text='', font=('arial', 18))
        self.anslay.pack(pady=5)

        self.Button_frame = ttk.Frame(self.window)
        self.Button_frame.pack()

        grid = StartGrid(self)
        grid.start_grid()

        self.menu_frame.place(x=0, y=0)
        self.menu_frame.tkraise()

    def slide_menu_in(self):
        for x in range(-150, 1, 10):
            self.menu_frame.place(x=x, y=0)
            self.menu_frame.update()

    def slide_menu_out(self):
        for x in range(0, -151, -10):
            self.menu_frame.place(x=x, y=0)
            self.menu_frame.update()

    def slide_menu_out_and_reset(self):
        if self.menu_open:
            self.slide_menu_out()
            self.menu_open = False
            self.window.unbind("<Escape>")
            self.window.unbind("<Button-1>")

    def check_click_outside_menu(self, event):
        if self.menu_open:  # was self.menu_visible before
            x, y = event.x_root, event.y_root
            menu_x1 = self.menu_frame.winfo_rootx()
            menu_y1 = self.menu_frame.winfo_rooty()
            menu_x2 = menu_x1 + self.menu_frame.winfo_width()
            menu_y2 = menu_y1 + self.menu_frame.winfo_height()

            if not (menu_x1 <= x <= menu_x2 and menu_y1 <= y <= menu_y2):
                self.slide_menu_out_and_reset()

    def toggle_menu(self):
        if self.menu_open:
            self.slide_menu_out()
            self.window.unbind("<Escape>")
            self.window.unbind("<Button-1>")
        else:
            self.slide_menu_in()
            self.window.bind("<Escape>", lambda e: self.slide_menu_out_and_reset())
            self.window.bind("<Button-1>", self.check_click_outside_menu)
        self.menu_open = not self.menu_open

    def update_display1(self):
        if self.is_it_decimal1 == 0:
            # Show integer without decimal
            self.num1lay.config(text=f" {int(self.num1)}")
        else:
            # Format number with fixed decimal places and trim trailing zeros
            format_str = f"{{:.{self.decimal_length1}f}}"
            text = format_str.format(self.num1)
            # Remove trailing zeros and decimal if none remain, but keep decimal point if decimal mode ON
            if '.' in text:
                text = text.rstrip('0').rstrip('.')
            # If decimal mode ON but no decimals, add decimal point
            if self.decimal_length1 == 0:
                text += '.'
            self.num1lay.config(text=f" {text}")

    def update_display2(self):
        if self.is_it_decimal2 == 0:
            self.num2lay.config(text=f" {int(self.num2)}")
        else:
            format_str = f"{{:.{self.decimal_length2}f}}"
            text = format_str.format(self.num2)
            if '.' in text:
                text = text.rstrip('0').rstrip('.')
            if self.decimal_length2 == 0:
                text += '.'
            self.num2lay.config(text=f" {text}")

    def update_ans(self):
        if self.ans is None:
            self.anslay.config(text=" Error (÷0)")
        else:
            self.anslay.config(text=f"= {self.ans}")

    def add_digit1(self, digit):
        self.num1 = self.num1 * 10 + digit
        self.update_display1()

    def add_digit2(self, digit):
        self.num2 = self.num2 * 10 + digit
        self.update_display2()

    def add_digit1decimal(self):
        if self.is_it_decimal1 == 0:
            self.is_it_decimal1 = 1

    def add_digit2decimal(self):
        if self.is_it_decimal2 == 0:
            self.is_it_decimal2 = 1

    def make_it_decimal(self):
        if self._1or2 == 1:
            self.add_digit1decimal()
        else:
            self.add_digit2decimal()

    def switch(self):
        self._1or2 = 2 if self._1or2 == 1 else 1

    def add_digit_to(self, i):
        if self._1or2 == 1 and self.is_it_decimal1 == 0:
            self.add_digit1(i)
        elif self._1or2 == 2 and self.is_it_decimal2 == 0:
            self.add_digit2(i)
        elif self._1or2 == 1 and self.is_it_decimal1 == 1:
            self.add_decimal1(i)
        else:
            self.add_decimal2(i)

    def add_decimal1(self, digit):
        self.num1 = self.num1 + (digit / (10 ** (self.decimal_length1 + 1)))
        self.decimal_length1 += 1
        self.update_display1()

    def add_decimal2(self, digit):
        self.num2 = self.num2 + (digit / (10 ** (self.decimal_length2 + 1)))
        self.decimal_length2 += 1
        self.update_display2()

    def back_space_10r2(self):
        if self._1or2 == 1:
            if self.is_it_decimal1 == 0:
                # Integer part backspace
                self.num1 = int(self.num1)  # Ensure int type
                self.num1 = self.num1 // 10 if self.num1 >= 10 else 0
                self.update_display1()
            else:
                if self.decimal_length1 > 0:
                    self.decimal_length1 -= 1
                    factor = 10 ** self.decimal_length1
                    self.num1 = int(self.num1 * factor) / factor
                    self.update_display1()
                else:
                    # Remove decimal point and convert to int type
                    self.is_it_decimal1 = 0
                    self.decimal_length1 = 0
                    self.num1 = int(self.num1)
                    self.update_display1()

        else:
            if self.is_it_decimal2 == 0:
                self.num2 = int(self.num2)  # Ensure int type
                self.num2 = self.num2 // 10 if self.num2 >= 10 else 0
                self.update_display2()
            else:
                if self.decimal_length2 > 0:
                    self.decimal_length2 -= 1
                    factor = 10 ** self.decimal_length2
                    self.num2 = int(self.num2 * factor) / factor
                    self.update_display2()
                else:
                    self.is_it_decimal2 = 0
                    self.decimal_length2 = 0
                    self.num2 = int(self.num2)
                    self.update_display2()

    def delete_all(self):
        self.num1 = float(0)
        self.num2 = float(0)
        self.ans = float(0)
        self._1or2 = 1
        self.decimal_length1 = 0
        self.decimal_length2 = 0
        self.is_it_decimal1 = 0
        self.is_it_decimal2 = 0
        self.num1lay.config(text=f"")
        self.num2lay.config(text=f"")
        self.anslay.config(text=f"")

    def addition(self):
        if self._1or2 == 1:
            self._1or2 = 2
            self.operation = 'add'

    def subtract(self):
        if self._1or2 == 1:
            self._1or2 = 2
            self.operation = 'sub'

    def multiply(self):
        if self._1or2 == 1:
            self._1or2 = 2
            self.operation = 'mul'

    def divide(self):
        if self._1or2 == 1:
            self._1or2 = 2
            self.operation = 'div'

    def solve(self):
        if self.operation == 'add':
            self.ans = self.num1 + self.num2
        elif self.operation == 'sub':
            self.ans = self.num1 - self.num2
        elif self.operation == 'mul':
            self.ans = self.num1 * self.num2
        elif self.operation == 'div':
            if self.num2 != 0:
                self.ans = self.num1 / self.num2
            else:
                self.ans = None
        else:
            self.ans = None  # In case no operation is selected
        self.update_ans()


window = tk.Tk()
app = CalculatorApp(window)
window.mainloop()
