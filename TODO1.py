import tkinter as tk

root = tk.Tk()
root.title("My First GUI App")
root.geometry("600x400")

root = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 18))
root.pack(pady=50)

root.mainloop()
