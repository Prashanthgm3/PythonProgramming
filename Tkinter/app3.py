import tkinter as tk

root= tk.Tk()

tk.Label(root, text="Label 1", bg="green").pack(side="left", fill="both", expand=True)
tk.Label(root, text="Label 1", bg="red").pack(side="top", fill="both")

root.mainloop()