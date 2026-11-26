import tkinter as tk

root = tk.Tk()
root.title("Straight Line Robot")

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

robot = canvas.create_oval(
    40, 190, 60, 210,
    fill="green"
)

def move():
    x1, y1, x2, y2 = canvas.coords(robot)

    if x2 < 450:
        canvas.move(robot, 5, 0)
        root.after(50, move)

move()

root.mainloop()