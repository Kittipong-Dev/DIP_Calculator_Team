import tkinter as tk

class MyCalculator:
    def __init__ (self):

        self.root = tk.Tk()

        self.root.geometry("320x580")
        self.root.title('My Calculator')

        # zero row
        self.label = tk.Label(self.root, text="PlaceHolder", font=('Arial', 18))
        self.label.grid(row=0, column=0, columnspan=4, pady=(100, 20))

        # first row
        self.clear_btn = tk.Button(self.root, text="AC", width=10, height=5)
        self.clear_btn.grid(row=1, column=0)

        self.negativenum_btn = tk.Button(self.root, text="+/-", width=10, height=5)
        self.negativenum_btn.grid(row=1, column=1)

        self.percent_btn = tk.Button(self.root, text="%", width=10, height=5)
        self.percent_btn.grid(row=1, column=2)

        self.devide_btn = tk.Button(self.root, text="÷", width=10, height=5)
        self.devide_btn.grid(row=1, column=3)

        # second row
        self.seven_btn = tk.Button(self.root, text="7", width=10, height=5)
        self.seven_btn.grid(row=2, column=0)

        self.eight_btn = tk.Button(self.root, text="8", width=10, height=5)
        self.eight_btn.grid(row=2, column=1)

        self.nine_btn = tk.Button(self.root, text="9", width=10, height=5)
        self.nine_btn.grid(row=2, column=2)

        self.multiply_btn = tk.Button(self.root, text="X", width=10, height=5)
        self.multiply_btn.grid(row=2, column=3)

        # third row
        self.four_btn = tk.Button(self.root, text="4", width=10, height=5)
        self.four_btn.grid(row=3, column=0)

        self.five_btn = tk.Button(self.root, text="5", width=10, height=5)
        self.five_btn.grid(row=3, column=1)

        self.six_btn = tk.Button(self.root, text="6", width=10, height=5)
        self.six_btn.grid(row=3, column=2)

        self.plus_btn = tk.Button(self.root, text="+", width=10, height=5)
        self.plus_btn.grid(row=3, column=3)

        # fouth row
        self.one_btn = tk.Button(self.root, text="1", width=10, height=5)
        self.one_btn.grid(row=4, column=0)

        self.two_btn = tk.Button(self.root, text="2", width=10, height=5)
        self.two_btn.grid(row=4, column=1)

        self.third_btn = tk.Button(self.root, text="3", width=10, height=5)
        self.third_btn.grid(row=4, column=2)

        self.minus_btn = tk.Button(self.root, text="-", width=10, height=5)
        self.minus_btn.grid(row=4, column=3)

        # fifth row

        self.zero_btn = tk.Button(self.root, text="0", width=22, height=5)
        self.zero_btn.grid(row=5, column=0, columnspan=2)

        self.decimal_btn = tk.Button(self.root, text=".", width=10, height=5)
        self.decimal_btn.grid(row=5, column=2)

        self.equal_btn = tk.Button(self.root, text="=", width=10, height=5)
        self.equal_btn.grid(row=5, column=3)

        self.root.mainloop()

if __name__ == "__main__":
    MyCalculator()