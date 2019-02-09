import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import connect4module as c4

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
        tk.Tk.wm_title(self, "Connect 4 Game")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # dictionary with all frames in the app listed
        self.frames = {}

        # creates each page and adds it to container
        for f in (StartPage, TossPage, BoardPageLose, BoardPageWin):
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

        button_continue = ttk.Button(self, text="Begin", command=lambda:
                                     controller.show_frame(TossPage))
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

        # makes buttons for heads and tails
        button_heads = ttk.Button(self, text="Heads", command=lambda:
                                  self.heads(outcome,
                                             nextstep,
                                             button_heads,
                                             button_tails,
                                             button_win,
                                             button_lose), width=6)
        button_tails = ttk.Button(self, text="Tails", command=lambda:
                                  self.tails(outcome,
                                             nextstep,
                                             button_heads,
                                             button_tails,
                                             button_win,
                                             button_lose), width=6)
        button_heads.grid(row=3, column=1)
        button_tails.grid(row=4, column=1)

        button_home = ttk.Button(self, text="Home", command=lambda:
                                 controller.show_frame(StartPage))
        button_home.grid(row=5, column=1)

        # empty labels that will be updated with outcome after user selects
        outcome = ttk.Label(self, text="", font=med)
        outcome.grid(row=6, column=1)
        nextstep = ttk.Label(self, text="", font=med)
        nextstep.grid(row=7, column=1)

        # Hidden buttons that becomes visible after user makes selection
        button_win = ttk.Button(self, text="Continue", command=lambda:
                                controller.show_frame(BoardPageWin))
        button_lose = ttk.Button(self, text="Continue", command=lambda:
                                 controller.show_frame(BoardPageLose))

    def heads(self, outcome, nextstep, button_heads, button_tails, button_win, button_lose):
        """
        Runs cointoss function in connect4module with chosen call = 1
        Updates buttons to have no function, so user cannot reselect
        Updates labels to show outcome of coin toss
        Makes relevant continue button visible
        """
        call = 1
        result = c4.cointoss(call)
        button_tails.configure(text="", command=self.donothing)
        button_heads.configure(command=self.donothing)
        if result == True:
            outcome.configure(text="You won the toss!")
            nextstep.configure(text="You will play first")
            button_win.grid(row=8, column=1)
        else:
            outcome.configure(text="You lost the toss!")
            nextstep.configure(text="The computer will play first")
            button_lose.grid(row=8, column=1)
        outcome.update()
        nextstep.update()
        button_heads.update()
        button_tails.update()
        return

    def tails(self, outcome, nextstep, button_heads, button_tails, button_win, button_lose):
        """
        Runs cointoss function in connect4module with chosen call = 0
        Updates buttons to have no function, so user cannot reselect
        Updates labels to show outcome of coin toss
        Makes relevant continue button visible
        """
        call = 0
        result = c4.cointoss(call)
        button_heads.configure(text="", command=self.donothing)
        button_tails.configure(command=self.donothing)
        if result == True:
            outcome.configure(text="You won the toss!")
            nextstep.configure(text="You will play first")
            button_win.grid(row=8, column=1)
        else:
            outcome.configure(text="You lost the toss!")
            nextstep.configure(text="The computer will play first")
            button_lose.grid(row=8, column=1)
        outcome.update()
        nextstep.update()
        button_heads.update()
        button_tails.update()
        return

    def donothing(self):
        """
        Function that does nothing.
        Makes a button useless if assigned to it
        """
        pass


class BoardPageLose(tk.Frame):
    """
    Board Page, contains main game
    If player lost toss
    """

    def __init__(self, window, controller):

        ttk.Frame.__init__(self, window)
        self.grid_columnconfigure(1, weight=1)

        title = ttk.Label(self, text="Computer will Play First!", font=large)
        title.grid(row=1, column=1)


class BoardPageWin(tk.Frame):
    """
    Board Page, contains main game
    If player won toss
    """

    def __init__(self, window, controller):

        ttk.Frame.__init__(self, window)
        self.grid_columnconfigure(1, weight=1)

        title = ttk.Label(self, text="You will Play First", font=large)
        title.grid(row=1, column=1)


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
