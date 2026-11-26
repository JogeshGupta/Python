import tkinter as tk

root = tk.Tk()
root.title("Robot Control Panel")
root.geometry("500x400")
root.configure(bg="yellow")

root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Point")

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

canvas.create_oval(95, 95, 105, 105,
                   fill="black")

root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Robot Path")

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

points = [20, 50, 100, 120, 180, 90, 250, 150]

canvas.create_line(points,
                   fill="blue",
                   width=3)

root.mainloop()