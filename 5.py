import tkinter as tk

root = tk.Tk()
root.title("Simple Robot")

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

# Body
canvas.create_rectangle(
    180, 100, 320, 250,
    fill="gray"
)

# Left wheel
canvas.create_oval(
    160, 230, 220, 290,
    fill="black"
)

# Right wheel
canvas.create_oval(
    280, 230, 340, 290,
    fill="black"
)

root.mainloop()