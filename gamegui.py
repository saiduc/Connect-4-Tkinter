import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
matplotlib.use("TkAgg")

large_font = ("ComicSansMS", 20)


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

        # displays StartPage frame upon initialisation of app
        frame = StartPage(container, self)
        self.frames[StartPage] = frame   # adds StartPage to dictionary
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, page):

        frame = self.frames[page]
        frame.tkraise()


class StartPage(tk.Frame):
    """
    Start Page, contains welcome screen and coin toss
    """

    def __init__(self, window, controller):

        tk.Frame.__init__(self, window)
        label = tk.Label(self, text="Welcome", font=large_font)
        label.pack(pady=10, padx=10)


def runapp(app):
    try:
        app.mainloop()
    except UnicodeDecodeError:
        runapp()


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
