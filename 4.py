import tkinter as tk

root = tk.Tk()
root.title("Moving Point")

canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

point = canvas.create_oval(
    10, 140, 30, 160,
    fill="black"
)

def move():
    canvas.move(point, 5, 0)

    if canvas.coords(point)[2] < 500:
        root.after(50, move)

move()

root.mainloop()