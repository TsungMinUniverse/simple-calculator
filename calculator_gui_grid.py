import tkinter as tk
import math
import sys
from advanced_ops import square, sqrt, reciprocal, power, log10, ln

def on_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        
        entry.insert(tk.END, "error")

def on_ops(op):
    print(op)
    result = ""
    try:
        if op == "x²":
            result = square(float(entry.get()))
    except:
        result = "error"
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
    return None
    
# 建立主視窗
root = tk.Tk()
root.title("Simple calculator")
#root.geometry("300x400")

# 輸入框
entry = tk.Entry(root, width=20, borderwidth=4, font=("Arial", 20), justify='right')
entry.grid(row=0, column=0, columnspan=5)

# 按鈕排版
offset = 2
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('.', 4, 2)
]
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: on_click(t))
    button.grid(row=row+offset, column=col)

# 基本運算按鈕
offset = 1
basic_ops = [
    ('+', 4, 3), ('-', 3, 3), ('*', 2, 3), ('/', 1, 3)
]
for (text, row, col) in basic_ops:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: on_click(t))
    button.grid(row=row+offset, column=col)

# 進階運算按鈕
advanced_ops = [
    ('log10', 1, 0), ('ln', 1, 1), ('xʸ', 1, 2),
    ('1/x', 2, 0), ('x²', 2, 1), ('√x', 2, 2),
    ('<=X', 1, 3), ('C', 6, 0), ('=', 6, 3)
]

for (text, row, col) in advanced_ops:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: on_ops(t))
    button.grid(row=row, column=col)

root.mainloop()