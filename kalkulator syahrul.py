import tkinter as tk
from tkinter import messagebox
import math


# Fungsi untuk menangani penekanan tombol
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(value))

# Fungsi untuk menghitung hasil
def calculate():
    try:
        expression = entry.get().replace('×', '*').replace('÷', '/').replace('^', '**')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")

# Fungsi untuk menghapus layar
def clear():
    entry.delete(0, tk.END)

# Fungsi untuk mengubah tanda positif/negatif
def plus_minus():
    current_text = entry.get()
    if current_text:
        if current_text.startswith('-'):
            entry.delete(0, tk.END)
            entry.insert(0, current_text[1:])
        else:
            entry.delete(0, tk.END)
            entry.insert(0, '-' + current_text)

# Fungsi untuk menghitung persen
def percentage():
    current_text = entry.get()
    try:
        result = eval(current_text) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")

# Fungsi untuk menghitung akar kuadrat
def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")

# Fungsi untuk menghitung logaritma
def log():
    try:
        result = math.log10(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")

# Fungsi untuk mengatur tampilan fullscreen
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", True)

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)

# Inisialisasi jendela
root = tk.Tk()
root.title("Kalkulator Syahrul")
root.configure(bg="#f0f0f0")

# Input area
entry = tk.Entry(root, width=20, font=('Arial', 28), bd=0, insertwidth=4, bg="#fff", fg="black", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Tombol-tombol dan posisi mereka
buttons = [
    ('AC', 1, 0), ('+/-', 1, 1), ('%', 1, 2), ('÷', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('^', 5, 3),
    ('√', 6, 0), ('log', 6, 1), ('(', 6, 2), (')', 6, 3)
]

# Membuat tombol-tombol
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 20), bg="#fa8231", command=calculate)
    elif text == 'AC':
        btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 20), bg="#ff3b30", command=clear)
    elif text == '+/-':
        btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 20), command=plus_minus)
    elif text == '√':
        btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 20), bg="yellow",  command=sqrt)
    elif text == 'log':
        btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 20), command=log)
    elif text == '(' or text == ')':
        btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 20), command=lambda value=text: button_click(value))
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 20), command=lambda value=text: button_click(value))
    
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Membuat tombol yang bisa diperbesar secara otomatis
for i in range(1, 7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)  

# Menjalankan aplikasi
root.mainloop()
