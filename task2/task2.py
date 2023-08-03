'''
Task no. 2
language: Python

'''




from tkinter import *
from tkinter import ttk
from math import *


class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        self.expression = ""

        self.display = Entry(window, width=30, bd=5,
                             font=("Arial", 15, "bold"), justify="right", bg="light cyan", foreground="blue")
        self.display.grid(row=0, column=0, columnspan=5, pady=8)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('√', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('X', 4, 4),

        ]

        for btn_text, row, col in buttons:
            button = ttk.Button(window, text=btn_text, width=10, style="Beautiful.TButton",
                                command=lambda text=btn_text: self.on_button_click(text))
            button.grid(row=row, column=col, sticky="nsew")

            for i in range(5):
                window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            window.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == "=":
            try:

                self.expression = self.expression.replace('^', '**')
                result = eval(self.expression)
                self.expression = str(result)
            except Exception:
                self.expression = "Error"
        elif text == "C":
            self.expression = ""
        elif text == "x":
            self.expression = self.expression[:-1]
        else:
            self.expression += text

        self.update_display()

    def update_display(self):
        self.display.delete(0, END)
        self.display.insert(END, self.expression)


if __name__ == "__main__":
    window = Tk()
    window.title(" Calculator ")
    window.iconbitmap("icon.ico")
    window.configure(background="light grey")
    window.minsize(150, 200)
    style = ttk.Style()
    style.configure(
        "Beautiful.TButton",
        font=("Arial", 15, "bold"),
        foreground="black",
        background="black",
        relief=GROOVE,
        borderwidth=2,
        padx=10,
        pady=10
    )
    calculator = Calculator(window)
    f1 = Frame(window)
    f1.grid(sticky="ew", columnspan=5)
    copyright_label = Label(f1, text="© 2023 CodSoft. All rights reserved.",
                            font=("Arial", 10), fg="gray")
    copyright_label.pack(side=BOTTOM, pady=1, fill=BOTH)
    window.mainloop()
