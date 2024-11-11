import tkinter as tk

# Fungsi untuk menangani penekanan tombol
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(value))

# Fungsi untuk menghitung hasil
def calculate():
    try:
        result = eval(entry.get().replace('×', '*').replace('÷', '/').replace('^', '**'))  # Mengganti simbol dengan operator
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Fungsi untuk menghapus layar
def clear():
    entry.delete(0, tk.END)

# Fungsi untuk menghapus satu karakter (seperti tombol delete)
def delete():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])  # Menghapus karakter terakhir

# Fungsi untuk menghitung persen
def percentage():
    current_text = entry.get()
    try:
        result = eval(current_text) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Inisialisasi jendela
root = tk.Tk()
root.title("Kalkulator Syahrul")

# Mengatur background utama dan jendela kalkulator menjadi abu-abu
root.configure(bg="#bdc3c7")

# Fungsi untuk membuat kalkulator fullscreen
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", True)

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)

# Input area
entry = tk.Entry(root, width=17, font=('Arial', 28), bd=0, insertwidth=2, bg="#f4f4f4", fg="black", justify='right', relief="flat")
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

# Warna untuk tombol
button_color = {
    'orange': '#ff9500',    # Warna tombol operasi
    'gray': '#f1f2f6',      # Warna tombol fungsi biasa
    'light_gray': '#dcdcdc',  # Warna tombol angka (abu-abu muda)
    'blue': '#3498db',       # Warna biru untuk tombol tertentu
    'red': '#e74c3c',        # Warna merah untuk tombol penting
    'white': '#ffffff'       # Warna putih untuk tombol normal
}

# Tombol kalkulator
buttons = [
    ('AC', clear, button_color['red']),
    ('Delete', delete, button_color['blue']),  # Ganti tombol +/-, menjadi Delete
    ('%', percentage, button_color['blue']),
    ('÷', lambda: button_click('÷'), button_color['orange']),  # Menggunakan ÷

    ('7', lambda: button_click(7), button_color['light_gray']),
    ('8', lambda: button_click(8), button_color['light_gray']),
    ('9', lambda: button_click(9), button_color['light_gray']),
    ('×', lambda: button_click('×'), button_color['orange']),  # Menggunakan ×

    ('4', lambda: button_click(4), button_color['light_gray']),
    ('5', lambda: button_click(5), button_color['light_gray']),
    ('6', lambda: button_click(6), button_color['light_gray']),
    ('-', lambda: button_click('-'), button_color['orange']),

    ('1', lambda: button_click(1), button_color['light_gray']),
    ('2', lambda: button_click(2), button_color['light_gray']),
    ('3', lambda: button_click(3), button_color['light_gray']),
    ('+', lambda: button_click('+'), button_color['orange']),

    ('0', lambda: button_click(0), button_color['light_gray']),
    ('.', lambda: button_click('.'), button_color['light_gray']),
    ('=', calculate, button_color['orange']),

    ('^', lambda: button_click('^'), button_color['red']),  # Tombol Pangkat (^) dipindah ke samping bawah "="
]

# Penempatan tombol
row_val = 1
col_val = 0
button_refs = []  # List untuk menyimpan referensi tombol

for (text, func, color) in buttons:
    if text == '0':  # Membuat tombol "0" lebih besar
        btn = tk.Button(root, text=text, font=('Arial', 24), bg=color, fg="black", bd=0,
                        command=func, padx=80, pady=20, relief="flat")
        btn.grid(row=row_val, column=col_val, columnspan=2, padx=5, pady=5, sticky="nsew")
        col_val += 2
    else:
        btn = tk.Button(root, text=text, font=('Arial', 24), bg=color, fg="black", bd=0,
                        command=func, padx=40, pady=20, relief="flat")
        btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
        col_val += 1

    button_refs.append(btn)  # Menyimpan referensi tombol

    if col_val > 3:
        col_val = 0
        row_val += 1

# Membuat tombol agar meregang
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Menambahkan efek hover (feedback visual) pada tombol
def on_enter(event, color):
    event.widget.config(bg=color)

def on_leave(event, original_color):
    event.widget.config(bg=original_color)

# Menerapkan efek hover pada semua tombol
for btn in button_refs:
    original_color = btn.cget('bg')  # Menyimpan warna asli tombol
    btn.bind("<Enter>", lambda event, color='#e67e22': on_enter(event, color))  # Warna saat hover
    btn.bind("<Leave>", lambda event, original_color=original_color: on_leave(event, original_color))  # Kembalikan warna

# Bind key F11 untuk masuk dan keluar dari fullscreen
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)

# Jalankan aplikasi
root.mainloop()
