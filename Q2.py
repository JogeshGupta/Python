import tkinter as tk

root = tk.Tk()
root.title("Point")

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

canvas.create_oval(95, 95, 105, 105,
                   fill="black")

root.mainloop()