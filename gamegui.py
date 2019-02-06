from tkinter import *

window = Tk()
window.title('Connect 4')
window.geometry('1000x800')

board = PhotoImage(file='placeholder.gif')
board.zoom(1)
Label(window, image=board).place(relx=0.5, rely=0.5, anchor=CENTER)

Label(window, text='Connect 4', font='ComicSansMS 30 bold underline').place(
    relx=0.5, rely=0.03, anchor=CENTER)

window.mainloop()
