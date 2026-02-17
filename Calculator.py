import tkinter as tk


def calculate(operator):
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    result_label.config(text="Result: " + str(result))


window = tk.Tk()
window.title("Calculator")
window.geometry("300x250")


tk.Label(window, text="Number 1:").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Number 2:").pack()
entry2 = tk.Entry(window)
entry2.pack()


tk.Button(window, text="+", command=lambda: calculate("+")).pack()
tk.Button(window, text="-", command=lambda: calculate("-")).pack()
tk.Button(window, text="*", command=lambda: calculate("*")).pack()
tk.Button(window, text="/", command=lambda: calculate("/")).pack()


result_label = tk.Label(window, text="Result:")
result_label.pack(pady=10)

window.mainloop()
