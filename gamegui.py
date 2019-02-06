from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("TkAgg")

window = Tk()
window.title('Connect 4')
window.geometry('1000x800')

Label(window, text='Connect 4', font='ComicSansMS 30 bold underline').place(
    relx=0.5, rely=0.03, anchor=CENTER)

# Placeholder Plot
f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)
a.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
canvas = FigureCanvasTkAgg(f, window)
canvas.draw()
canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()
