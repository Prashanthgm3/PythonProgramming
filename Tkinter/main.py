import tkinter as tk

root = tk.Tk()

tk.title("Hello WOrld")

def add(x, y):
    total = x + y
    return total

print(add(5,10))

root.mainloop()