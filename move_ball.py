import tkinter as tk
import random

WIDTH, HEIGHT = 500, 500
SIZE = 40  # square side length

window = tk.Tk()
window.title("Bouncing Square")
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

# random start position and random direction
x = random.randint(0, WIDTH - SIZE)
y = random.randint(0, HEIGHT - SIZE)
dx = random.choice([-1, 1]) * random.randint(2, 5)
dy = random.choice([-1, 1]) * random.randint(2, 5)

square = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill='white', outline='')

def random_color():
    return "#%06x" % random.randint(0x333333, 0xFFFFFF)

def move():
    global dx, dy
    canvas.move(square, dx, dy)
    x1, y1, x2, y2 = canvas.coords(square)

    hit = False
    if x1 <= 0 or x2 >= WIDTH:
        dx = -dx
        hit = True
    if y1 <= 0 or y2 >= HEIGHT:
        dy = -dy
        hit = True

    if hit:
        canvas.itemconfig(square, fill=random_color())

    window.after(16, move)

move()
window.mainloop()