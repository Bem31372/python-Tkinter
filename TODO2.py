import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry.get()
    messagebox.showinfo("Result", "Hello " + name)

def cancel():
    window.destroy()

window = tk.Tk()
window.title("Name Program")
window.geometry("300x180")

label = tk.Label(window, text="What's your name?")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

ok_button = tk.Button(window, text="OK", command=submit)
ok_button.pack(side="left", padx=30, pady=20)

cancel_button = tk.Button(window, text="Cancel", command=cancel)
cancel_button.pack(side="right", padx=30)

window.mainloop()
