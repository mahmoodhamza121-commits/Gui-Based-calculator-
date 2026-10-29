import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.resizable(False, False)

        self.first_num = None
        self.operation = None
        self.reset_screen = False

        self.display = tk.Entry(root, font=("Arial", 18), justify="right", bd=8)
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for text, row, col in buttons:
            action = lambda t=text: self.on_button_click(t)
            tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col, padx=2, pady=2)

    def on_button_click(self, char):
        if char in '0123456789':
            if self.reset_screen:
                self.display.delete(0, tk.END)
                self.reset_screen = False
            self.display.insert(tk.END, char)

        elif char in '+-*/':
            try:
                self.first_num = float(self.display.get())
                self.operation = char
                self.reset_screen = True
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")

        elif char == '=':
            if self.first_num is not None and self.operation is not None:
                try:
                    second_num = float(self.display.get())

                  
                    if self.operation == '+':
                        result = add(self.first_num, second_num)
                    elif self.operation == '-':
                        result = subtract(self.first_num, second_num)
                    elif self.operation == '*':
                        result = multiply(self.first_num, second_num)
                    elif self.operation == '/':
                        result = divide(self.first_num, second_num)

                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                    self.first_num = None
                    self.operation = None
                except ValueError:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")

        elif char == 'C':
            self.display.delete(0, tk.END)
            self.first_num = None
            self.operation = None

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()