import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500, bg='red')

ball = canvas.create_oval(200,20,300,120,fill='blue')
rectangle = canvas.create_rectangle(175,120,325,350,fill='yellow')
rectangle = canvas.create_rectangle(190,350,210,450,fill='blue')
rectangle = canvas.create_rectangle(290,350,310,450,fill='blue')
ball = canvas.create_oval(190,450,210,470,fill = 'yellow')
ball = canvas.create_oval(290,450,310,470,fill = 'yellow')
arm = canvas.create_line(175,120,100,200,fill='green')
# ball = canvas.create_oval(100,100,150,150,fill='blue')
# ball = canvas.create_oval(100,100,150,150,fill='blue')
# ball = canvas.create_oval(100,100,150,150,fill='blue')
# ball = canvas.create_oval(100,100,150,150,fill='blue')
# ball = canvas.create_oval(100,100,150,150,fill='blue')
canvas.pack()
window.mainloop()