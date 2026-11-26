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