import tkinter as tk
import math
import sys

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
    
# 建立主視窗
root = tk.Tk()
root.title("Simple calculator")
root.geometry("300x400")

# 輸入框
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="groove", justify="right")
entry.pack(padx=10, pady=10, fill="both")

# 按鈕排版
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

for row in buttons:
    row_frame = tk.Frame(root)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), height=2, width=4)
        btn.pack(side="left", expand=True, fill="both")
        if btn_text == "C":
            btn.config(command=clear)
        elif btn_text == "=":
            btn.config(command=calculate)
        else:
            btn.config(command=lambda char=btn_text: on_click(char))
root.mainloop()