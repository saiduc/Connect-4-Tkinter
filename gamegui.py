import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
matplotlib.use("TkAgg")

large = ("ComicSansMS", 40)
med = ("ComicSansMS", 30)
small = ("ComicSansMS", 20)


class Connect4App(tk.Tk):
    """
    Controller class, will control whole application
    """

    def __init__(self):

        # create window that will display all the frames
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # dictionary with all frames in the app listed
        self.frames = {}

        # creates each page and adds it to container
        for f in (StartPage, TossPage):
            frame = f(container, self)
            self.frames[f] = frame   # adds pages to dictionary
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(StartPage)

    # raises necessary page to top to see
    def show_frame(self, page):

        frame = self.frames[page]
        frame.tkraise()


class StartPage(tk.Frame):
    """
    Start Page, contains welcome screen and button to start
    """

    def __init__(self, window, controller):

        ttk.Frame.__init__(self, window)
        self.grid_columnconfigure(1, weight=1)

        title = ttk.Label(self, text="Welcome to Connect 4!", font=large)
        title.grid(row=1, column=1)

        button_continue = ttk.Button(self, text="Begin",
                                     command=lambda: controller.show_frame(TossPage))
        button_continue.grid(row=2, column=1)


class TossPage(tk.Frame):
    """
    Toss Page, contains coin toss function
    """

    def __init__(self, window, controller):
        ttk.Frame.__init__(self, window)
        self.grid_columnconfigure(1, weight=1)

        title = ttk.Label(self, text="Coin Toss", font=large)
        title.grid(row=1, column=1)

        toss = ttk.Label(self, text="Choose heads or tails", font=med)
        toss.grid(row=2, column=1)

        button_heads = ttk.Button(self, text="Heads", command=heads, width=6)
        button_tails = ttk.Button(self, text="Tails", command=tails, width=6)
        button_heads.grid(row=3, column=1)
        button_tails.grid(row=4, column=1)


def runapp(app):
    try:
        app.mainloop()
    except UnicodeDecodeError:
        runapp()


def heads():
    result = 1
    return


def tails():
    result = 0
    return


app = Connect4App()
runapp(app)


# window = tk.Tk()
# window.title('Connect 4')
# window.geometry('1000x800')

# Label(window, text='Connect 4', font='ComicSansMS 30 bold underline').place(
#     relx=0.5, rely=0.03, anchor=CENTER)

# # Placeholder Plot
# f = Figure(figsize=(5, 5), dpi=100)
# a = f.add_subplot(111)
# a.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# canvas = FigureCanvasTkAgg(f, window)
# canvas.draw()
# canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER)

# # Have to do this to prevent closing on scroll


# def mainloop():
#     try:
#         window.mainloop()
#     except UnicodeDecodeError:
#         mainloop()


# mainloop()
