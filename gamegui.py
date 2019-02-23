import platform
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
        button_tails.configure(text="", command=donothing)
        button_heads.configure(command=donothing)
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
        button_heads.configure(text="", command=donothing)
        button_tails.configure(command=donothing)
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


class BoardPageLose(tk.Frame):
    """
    Board Page, contains main game
    If player lost toss
    """

    def __init__(self, window, controller):

        ttk.Frame.__init__(self, window)

        title = ttk.Label(
            self, text="Connect 4 Game", font=large)
        title.grid(row=1, column=1)
        board = c4.makearrayboard()
        computercolumn = c4.decidecomputermove(board)
        while c4.checkifvalid(board, computercolumn) != True:
            computercolumn = c4.decidecomputermove(board)
        c4.docomputermove(board, computercolumn)
        graph = c4.plotgraphicalboard(board)
        canvas = FigureCanvasTkAgg(graph, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=1)

        separator = ttk.Label(self, text=" ", font=small)
        separator.grid(row=3, column=1)
        statement = ttk.Label(self, text="Choose a column", font=med)
        statement.grid(row=4, column=1)

        button_a = ttk.Button(self, text="a", command=lambda:
                              self.choose_a(board, buttons, statement), width=1)
        button_b = ttk.Button(self, text="b", command=lambda:
                              self.choose_b(board, buttons, statement), width=1)
        button_c = ttk.Button(self, text="c", command=lambda:
                              self.choose_c(board, buttons, statement), width=1)
        button_d = ttk.Button(self, text="d", command=lambda:
                              self.choose_d(board, buttons, statement), width=1)
        button_e = ttk.Button(self, text="e", command=lambda:
                              self.choose_e(board, buttons, statement), width=1)
        button_f = ttk.Button(self, text="f", command=lambda:
                              self.choose_f(board, buttons, statement), width=1)
        button_g = ttk.Button(self, text="g", command=lambda:
                              self.choose_g(board, buttons, statement), width=1)

        if platform.system() == "Windows":
            button_a.place(x=68, y=410)
            button_b.place(x=111, y=410)
            button_c.place(x=154, y=410)
            button_d.place(x=197, y=410)
            button_e.place(x=240, y=410)
            button_f.place(x=283, y=410)
            button_g.place(x=327, y=410)
        else:
            button_a.place(x=25, y=410)
            button_b.place(x=68, y=410)
            button_c.place(x=111, y=410)
            button_d.place(x=154, y=410)
            button_e.place(x=197, y=410)
            button_f.place(x=240, y=410)
            button_g.place(x=283, y=410)

        buttons = [button_a, button_b, button_c,
                   button_d, button_e, button_f, button_g]

    def choose_a(self, board, buttons, statement):
        usercolumn = 0
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 0)
            self.continuegame(board, buttons, statement)

    def choose_b(self, board, buttons, statement):
        usercolumn = 1
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 1)
            self.continuegame(board, buttons, statement)

    def choose_c(self, board, buttons, statement):
        usercolumn = 2
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 2)
            self.continuegame(board, buttons, statement)

    def choose_d(self, board, buttons, statement):
        usercolumn = 3
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 3)
            self.continuegame(board, buttons, statement)

    def choose_e(self, board, buttons, statement):
        usercolumn = 4
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 4)
            self.continuegame(board, buttons, statement)

    def choose_f(self, board, buttons, statement):
        usercolumn = 5
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 5)
            self.continuegame(board, buttons, statement)

    def choose_g(self, board, buttons, statement):
        usercolumn = 6
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 6)
            self.continuegame(board, buttons, statement)

    def continuegame(self, board, buttons, statement):
        """
        Main game function. Checks the gamestate to see if game is over
        If game is not over, makes the computer move and checks again
        If game is still not over, allows player to make another move
        If game is over, displays the appropriate labels
        Makes all buttons useless game is over
        """
        gamestate = c4.checkgamestate(board)

        if gamestate == 0:
            computercolumn = c4.decidecomputermove(board)
            while c4.checkifvalid(board, computercolumn) != True:
                computercolumn = c4.decidecomputermove(board)
            c4.docomputermove(board, computercolumn)
            gamestate = c4.checkgamestate(board)
            graph = c4.plotgraphicalboard(board)
            canvas = FigureCanvasTkAgg(graph, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=1)

        if gamestate == 1:
            graph = c4.plotgraphicalboard(board)
            canvas = FigureCanvasTkAgg(graph, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=1)
            buttons[0].configure(command=donothing)
            buttons[1].configure(command=donothing)
            buttons[2].configure(command=donothing)
            buttons[3].configure(command=donothing)
            buttons[4].configure(command=donothing)
            buttons[5].configure(command=donothing)
            buttons[6].configure(command=donothing)
            buttons[0].update()
            buttons[1].update()
            buttons[2].update()
            buttons[3].update()
            buttons[4].update()
            buttons[5].update()
            buttons[6].update()
            statement.configure(text="You Won!")
            statement.update()
            print("You win")

        if gamestate == 2:
            buttons[0].configure(command=donothing)
            buttons[1].configure(command=donothing)
            buttons[2].configure(command=donothing)
            buttons[3].configure(command=donothing)
            buttons[4].configure(command=donothing)
            buttons[5].configure(command=donothing)
            buttons[6].configure(command=donothing)
            buttons[0].update()
            buttons[1].update()
            buttons[2].update()
            buttons[3].update()
            buttons[4].update()
            buttons[5].update()
            buttons[6].update()
            statement.configure(text="You Lost!")
            statement.update()
            print("You lose")

        if gamestate == 3:
            graph = c4.plotgraphicalboard(board)
            canvas = FigureCanvasTkAgg(graph, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=1)
            statement.configure(text="It's a draw!")
            statement.update()
            print("You draw")


class BoardPageWin(tk.Frame):
    """
    Board Page, contains main game
    If player won toss
    """

    def __init__(self, window, controller):

        ttk.Frame.__init__(self, window)

        title = ttk.Label(self, text="Connect 4 Game", font=large)
        title.grid(row=1, column=1)
        board = c4.makearrayboard()
        graph = c4.plotgraphicalboard(board)

        canvas = FigureCanvasTkAgg(graph, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=1)

        separator = ttk.Label(self, text=" ", font=small)
        separator.grid(row=3, column=1)
        statement = ttk.Label(self, text="Choose a column", font=med)
        statement.grid(row=4, column=1)

        button_a = ttk.Button(self, text="a", command=lambda:
                              self.choose_a(board, buttons, statement), width=1)
        button_b = ttk.Button(self, text="b", command=lambda:
                              self.choose_b(board, buttons, statement), width=1)
        button_c = ttk.Button(self, text="c", command=lambda:
                              self.choose_c(board, buttons, statement), width=1)
        button_d = ttk.Button(self, text="d", command=lambda:
                              self.choose_d(board, buttons, statement), width=1)
        button_e = ttk.Button(self, text="e", command=lambda:
                              self.choose_e(board, buttons, statement), width=1)
        button_f = ttk.Button(self, text="f", command=lambda:
                              self.choose_f(board, buttons, statement), width=1)
        button_g = ttk.Button(self, text="g", command=lambda:
                              self.choose_g(board, buttons, statement), width=1)

        if platform.system() == "Windows":
            button_a.place(x=68, y=410)
            button_b.place(x=111, y=410)
            button_c.place(x=154, y=410)
            button_d.place(x=197, y=410)
            button_e.place(x=240, y=410)
            button_f.place(x=283, y=410)
            button_g.place(x=327, y=410)
        else:
            button_a.place(x=25, y=410)
            button_b.place(x=68, y=410)
            button_c.place(x=111, y=410)
            button_d.place(x=154, y=410)
            button_e.place(x=197, y=410)
            button_f.place(x=240, y=410)
            button_g.place(x=283, y=410)

        buttons = [button_a, button_b, button_c,
                   button_d, button_e, button_f, button_g]

    def choose_a(self, board, buttons, statement):
        usercolumn = 0
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 0)
            self.continuegame(board, buttons, statement)

    def choose_b(self, board, buttons, statement):
        usercolumn = 1
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 1)
            self.continuegame(board, buttons, statement)

    def choose_c(self, board, buttons, statement):
        usercolumn = 2
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 2)
            self.continuegame(board, buttons, statement)

    def choose_d(self, board, buttons, statement):
        usercolumn = 3
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 3)
            self.continuegame(board, buttons, statement)

    def choose_e(self, board, buttons, statement):
        usercolumn = 4
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 4)
            self.continuegame(board, buttons, statement)

    def choose_f(self, board, buttons, statement):
        usercolumn = 5
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 5)
            self.continuegame(board, buttons, statement)

    def choose_g(self, board, buttons, statement):
        usercolumn = 6
        if c4.checkifvalid(board, usercolumn) == True:
            c4.dousermove(board, 6)
            self.continuegame(board, buttons, statement)

    def continuegame(self, board, buttons, statement):
        """
        Main game function. Checks the gamestate to see if game is over
        If game is not over, makes the computer move and checks again
        If game is still not over, allows player to make another move
        If game is over, displays the appropriate labels
        Makes all buttons useless game is over
        """

        gamestate = c4.checkgamestate(board)

        if gamestate == 0:
            computercolumn = c4.decidecomputermove(board)
            while c4.checkifvalid(board, computercolumn) != True:
                computercolumn = c4.decidecomputermove(board)
            c4.docomputermove(board, computercolumn)
            gamestate = c4.checkgamestate(board)
            graph = c4.plotgraphicalboard(board)
            canvas = FigureCanvasTkAgg(graph, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=1)

        if gamestate == 1:
            graph = c4.plotgraphicalboard(board)
            canvas = FigureCanvasTkAgg(graph, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=1)
            buttons[0].configure(command=donothing)
            buttons[1].configure(command=donothing)
            buttons[2].configure(command=donothing)
            buttons[3].configure(command=donothing)
            buttons[4].configure(command=donothing)
            buttons[5].configure(command=donothing)
            buttons[6].configure(command=donothing)
            buttons[0].update()
            buttons[1].update()
            buttons[2].update()
            buttons[3].update()
            buttons[4].update()
            buttons[5].update()
            buttons[6].update()
            statement.configure(text="You Won!")
            statement.update()
            print("You win")

        if gamestate == 2:
            buttons[0].configure(command=donothing)
            buttons[1].configure(command=donothing)
            buttons[2].configure(command=donothing)
            buttons[3].configure(command=donothing)
            buttons[4].configure(command=donothing)
            buttons[5].configure(command=donothing)
            buttons[6].configure(command=donothing)
            buttons[0].update()
            buttons[1].update()
            buttons[2].update()
            buttons[3].update()
            buttons[4].update()
            buttons[5].update()
            buttons[6].update()
            statement.configure(text="You Lost!")
            statement.update()
            print("You lose")

        if gamestate == 3:
            graph = c4.plotgraphicalboard(board)
            canvas = FigureCanvasTkAgg(graph, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=1)
            statement.configure(text="It's a draw!")
            statement.update()
            print("You draw")


def donothing():
    """
    Function that does nothing.
    Makes a button useless if assigned to it
    """
    pass


# Stops program crashing on mac due to UnicodeDecodeError
def runapp(app):
    try:
        app.mainloop()
    except UnicodeDecodeError:
        runapp(app)


app = Connect4App()
runapp(app)
