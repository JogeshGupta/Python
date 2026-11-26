import tkinter as tk

root = tk.Tk()
root.title("Bouncing Ball")

width = 400
height = 300
radius = 15

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

ball = canvas.create_oval(
    185, 135, 215, 165,
    fill="red"
)

dx = 4
dy = 3

def move():
    global dx, dy

    canvas.move(ball, dx, dy)

    x1, y1, x2, y2 = canvas.coords(ball)

    if x1 <= 0 or x2 >= width:
        dx = -dx

    if y1 <= 0 or y2 >= height:
        dy = -dy

    root.after(20, move)

move()

root.mainloop()