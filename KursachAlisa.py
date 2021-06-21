from tkinter import *
import numpy as np


canvas_width = 1000
canvas_height = 1000
brush_size = 3
color = "black"



def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    c.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def brish_size_change(new_size):
    global brush_size
    brush_size = new_size


def color_change(new_color):
    global color
    color = new_color


def plotting_graphs(func):
    global func_line
    func = func.get()
    func_line.delete(0, END)
    c.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
    c.create_line(0, 500, 1000, 500, width=2, arrow=LAST)
    First_x = -500
    for i in range(16000):
        if (i % 800 == 0):
            k = First_x + (1 / 16) * i
            c.create_line(k + 500, -3 + 500, k + 500, 3 + 500, width=0.5, fill='black')
            c.create_text(k + 515, -10 + 500, text=str(k), fill="purple", font=("Helvectica", "10"))
            if (k != 0):
                c.create_line(-3 + 500, k + 500, 3 + 500, k + 500, width=0.5, fill='black')
                c.create_text(20 + 500, k + 500, text=str(k), fill="purple", font=("Helvectica", "10"))
        try:
            x = First_x + (1 / 16) * i
            new_f = func.replace('x', str(x))
            new_f = new_f.replace('^', '**')
            new_f = new_f.replace('sin', 'np.sin')
            new_f = new_f.replace('cos', 'np.cos')
            y = -eval(new_f) + 500
            x += 500
            c.create_oval(x, y, x + 1, y + 1, fill='black')
        except:
            pass


root = Tk()
root.title("Графический редактор")
# root.iconbitmap("logic.ico")

c = Canvas(root, width=canvas_width, height=canvas_height, bg="white")

c.bind("<B1-Motion>", paint)


message = StringVar()
func_line = Entry(textvariable=message)

black_btn = Button(text="Чёрный", width=7,
                 command=lambda: color_change("black"))
red_btn = Button(text="Красный", width=7,
                 command=lambda: color_change("red"))
yellow_btn = Button(text="Желтый", width=7,
                 command=lambda: color_change("yellow"))
blue_btn = Button(text="Синий", width=7,
                 command=lambda: color_change("blue"))
green_btn = Button(text="Зеленый", width=7,
                 command=lambda: color_change("green"))
white_btn = Button(text="Ластик", width=7,
                 command=lambda: color_change("white"))
clear_btn = Button(text="Удалить всё", width=10,
                 command=lambda: c.delete("all"))


agree_btn = Button(text="Построить", width=10,
                   command=lambda: plotting_graphs(func_line))
three_btn = Button(text="3", width=7,
                  command=lambda: brish_size_change(3))
five_btn = Button(text="5", width=7,
                  command=lambda: brish_size_change(5))
ten_btn = Button(text="10", width=7,
                  command=lambda: brish_size_change(10))
twelve_btn = Button(text="12", width=7,
                  command=lambda: brish_size_change(12))
seventeen_btn = Button(text="17", width=7,
                  command=lambda: brish_size_change(17))
twenty_btn = Button(text="20", width=7,
                  command=lambda: brish_size_change(20))
twentyfive_btn = Button(text="25", width=10,
                  command=lambda: brish_size_change(25))


c.grid(row=2, column=0, columnspan=9, padx=5, pady=5, sticky=E+W+S+N)
c.columnconfigure (8, weight=1)
c.rowconfigure(2, weight=1)

func_line.grid(row=0, column=1)
black_btn.grid(row=0, column=2)
red_btn.grid(row=0, column=3)
yellow_btn.grid(row=0, column=4)
blue_btn.grid(row=0, column=5)
green_btn.grid(row=0, column=6)
white_btn.grid(row=0, column=7)
clear_btn.grid(row=0, column=8)

agree_btn.grid(row=1, column=1)
three_btn.grid(row=1, column=2)
five_btn.grid(row=1, column=3)
ten_btn.grid(row=1, column=4)
twelve_btn.grid(row=1, column=5)
seventeen_btn.grid(row=1, column=6)
twenty_btn.grid(row=1, column=7)
twentyfive_btn.grid(row=1, column=8)


root.mainloop()

