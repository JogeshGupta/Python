
import tkinter as tk
import math

root = tk.Tk()
root.title("Four-Bar Mechanism")
canvas = tk.Canvas(root, width=600, height=450, bg="white")
canvas.pack()

# Given dimensions
A = (150, 300)
D = (400, 300)

L2 = 120
L3 = 150
L4 = 130
theta = math.radians(30)

# Calculate point B
B = (
    A[0] + L2 * math.cos(theta),
    A[1] - L2 * math.sin(theta)
)

# Calculate point C using circle intersection
dx = D[0] - B[0]
dy = D[1] - B[1]

distance = math.sqrt(dx**2 + dy**2)

a = (L3**2 - L4**2 + distance**2) / (2 * distance)
h = math.sqrt(L3**2 - a**2)

xm = B[0] + a * dx / distance
ym = B[1] + a * dy / distance

C1 = (
    xm + h * dy / distance,
    ym - h * dx / distance
)

C2 = (
    xm - h * dy / distance,
    ym + h * dx / distance
)

# Select upper intersection
C = C1 if C1[1] < C2[1] else C2

# Draw ground link
canvas.create_line(A, D, fill="black", width=8)
canvas.create_line(150, 310, 400, 310, fill="gray", width=2)

# Draw ground hatching
for x in range(160, 400, 15):
    canvas.create_line(x, 310, x-8, 320, fill="gray")

# Draw moving links
canvas.create_line(A, B, fill="red", width=6)
canvas.create_line(B, C, fill="blue", width=6)
canvas.create_line(C, D, fill="green", width=6)

# Draw joints
for point in [A, B, C, D]:
    x, y = point
    canvas.create_oval(
        x-7, y-7, x+7, y+7,
        fill="white", outline="black", width=2
    )

# Joint labels
canvas.create_text(135, 300, text="A", font=("Arial", 14, "bold"))
canvas.create_text(255, 220, text="B", font=("Arial", 14, "bold"))
canvas.create_text(395, 155, text="C", font=("Arial", 14, "bold"))
canvas.create_text(415, 300, text="D", font=("Arial", 14, "bold"))

# Link labels
canvas.create_text(205, 260, text="Crank L2 = 120 px", fill="red")
canvas.create_text(315, 195, text="Coupler L3 = 150 px", fill="blue")
canvas.create_text(450, 230, text="Rocker L4 = 130 px", fill="green")
canvas.create_text(275, 335, text="Ground AD = 250 px")

# Input angle
canvas.create_arc(
    120, 270, 180, 330,
    start=0, extent=30,
    style="arc", outline="purple", width=2
)

canvas.create_text(190, 290, text="30°", fill="purple")

# Title
canvas.create_text(
    300, 30,
    text="FOUR-BAR MECHANISM",
    font=("Arial", 16, "bold")
)

# Display calculated coordinates
print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)

root.mainloop()
