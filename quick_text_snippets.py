import tkinter as tk
from tkinter import ttk
import pyperclip

root = tk.Tk()
root.title("Quick Text Snippets")
# root.geometry("380x30")


def copy_btn_1():
    with open('one.txt', 'r') as f:
        data = f.read()
        pyperclip.copy(data)


def copy_btn_2():
    with open('two.txt', 'r') as f:
        data = f.read()
        pyperclip.copy(data)


def copy_btn_3():
    with open('three.txt', 'r') as f:
        data = f.read()
        pyperclip.copy(data)


def copy_btn_4():
    with open('four.txt', 'r') as f:
        data = f.read()
        pyperclip.copy(data)


btn = ttk.Button(root, text="Course Template...", command=copy_btn_1)
btn.pack(side=tk.LEFT, pady=3)

btn2 = ttk.Button(root, text="SME Email Template...", command=copy_btn_2)
btn2.pack(side=tk.LEFT, pady=3)

btn3 = ttk.Button(root, text="Snippet...", command=copy_btn_3)
btn3.pack(side=tk.LEFT, pady=3)

btn4 = ttk.Button(root, text="Text...", command=copy_btn_4)
btn4.pack(side=tk.LEFT, pady=3)

root.mainloop()
