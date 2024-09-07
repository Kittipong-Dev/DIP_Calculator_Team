import tkinter as tk
from Calculator import *
class DisplayCalculator:
    def __init__ (self):
    
        self.root = tk.Tk()
        self.cal = Calculator()

        self.root.geometry("320x580")
        self.root.title('DIP_CALCULATOR_TEAM')

        # zero row
        self.label = tk.Label(self.root, text="0", font=('Arial', 18))
        self.label.grid(row=0, column=0, columnspan=4, pady=(100, 20))

        # first row
        self.clear_btn = tk.Button(self.root, text="AC", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("0")))
        self.clear_btn.grid(row=1, column=0,)

        self.negativenum_btn = tk.Button(self.root, text="+/-", width=10, height=5, command=lambda: self.update_display(self.cal.negate()))
        self.negativenum_btn.grid(row=1, column=1)

        self.percent_btn = tk.Button(self.root, text="%", width=10, height=5, command=lambda: self.update_display(self.cal.percent()))
        self.percent_btn.grid(row=1, column=2)

        self.divide_btn = tk.Button(self.root, text="÷", width=10, height=5, command=lambda: self.update_display(self.cal.divide()))
        self.divide_btn.grid(row=1, column=3)

        # second row
        self.seven_btn = tk.Button(self.root, text="7", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("7")))
        self.seven_btn.grid(row=2, column=0)

        self.eight_btn = tk.Button(self.root, text="8", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("8")))
        self.eight_btn.grid(row=2, column=1)

        self.nine_btn = tk.Button(self.root, text="9", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("9")))
        self.nine_btn.grid(row=2, column=2)

        self.multiply_btn = tk.Button(self.root, text="X", width=10, height=5, command=lambda: self.update_display(self.cal.multiply()))
        self.multiply_btn.grid(row=2, column=3)

        # third row
        self.four_btn = tk.Button(self.root, text="4", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("4")))
        self.four_btn.grid(row=3, column=0)

        self.five_btn = tk.Button(self.root, text="5", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("5")))
        self.five_btn.grid(row=3, column=1)

        self.six_btn = tk.Button(self.root, text="6", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("6")))
        self.six_btn.grid(row=3, column=2)

        self.plus_btn = tk.Button(self.root, text="+", width=10, height=5, command=lambda: self.update_display(self.cal.plus()))
        self.plus_btn.grid(row=3, column=3)

        # fouth row
        self.one_btn = tk.Button(self.root, text="1", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("1")))
        self.one_btn.grid(row=4, column=0)

        self.two_btn = tk.Button(self.root, text="2", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("2")))
        self.two_btn.grid(row=4, column=1)

        self.third_btn = tk.Button(self.root, text="3", width=10, height=5, command=lambda: self.update_display(self.cal.add_number("3")))
        self.third_btn.grid(row=4, column=2)

        self.minus_btn = tk.Button(self.root, text="-", width=10, height=5, command=lambda: self.update_display(self.cal.minus()))
        self.minus_btn.grid(row=4, column=3)

        # fifth row

        self.zero_btn = tk.Button(self.root, text="0", width=22, height=5, command=lambda: self.update_display(self.cal.add_number("0")))
        self.zero_btn.grid(row=5, column=0, columnspan=2)

        self.decimal_btn = tk.Button(self.root, text=".", width=10, height=5, command=lambda: self.update_display(self.cal.decimal()))
        self.decimal_btn.grid(row=5, column=2)

        self.equal_btn = tk.Button(self.root, text="=", width=10, height=5, command=lambda: self.update_display(self.cal.get_result()))
        self.equal_btn.grid(row=5, column=3)

        self.root.mainloop()

    def update_display(self, value):
        self.label.config(text=value)
if __name__ == "__main__":
    DisplayCalculator()