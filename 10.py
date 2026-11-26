import tkinter as tk

root = tk.Tk()
root.title("Robot Path Control")

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

# Initial position
x = 250
y = 200

robot = canvas.create_oval(
    x-10, y-10, x+10, y+10,
    fill="blue"
)

previous = (x, y)

def move(dx, dy):
    global x, y, previous

    x += dx
    y += dy

    # Draw path
    canvas.create_line(
        previous[0], previous[1],
        x, y,
        fill="red",
        width=2
    )

    # Move robot
    canvas.coords(
        robot,
        x-10, y-10,
        x+10, y+10
    )

    previous = (x, y)

def up(event):
    move(0, -5)

def down(event):
    move(0, 5)

def left(event):
    move(-5, 0)

def right(event):
    move(5, 0)

def reset():
    global x, y, previous

    canvas.delete("all")

    x = 250
    y = 200
    previous = (x, y)

    # Draw robot again
    global robot
    robot = canvas.create_oval(
        x-10, y-10, x+10, y+10,
        fill="blue"
    )

# Bind arrow keys
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)

# Allow keyboard input
root.focus_set()

# Reset button
tk.Button(
    root,
    text="RESET",
    command=reset
).pack()

root.mainloop()