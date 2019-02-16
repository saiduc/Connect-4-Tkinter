import string
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
matplotlib.use("TkAgg")


def makegraphicalboard():
    """
    Makes an empty board with the required dimensions and labels.
    """
    fig = Figure(figsize=(7, 7), dpi=50)
    # a = fig.add_subplot(111)
    # a.plot()
    # these are the labels to make the board look nice
    # a.xaxis.set_ticks([1, 2, 3, 4, 5, 6, 7, 8], [
    # 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
    # a.yaxis.set_ticks([1, 2, 3, 4, 5, 6, 7], ['1', '2', '3', '4', '5', '6'])
    return fig


def makearrayboard():
    """
    Makes an array of zeroes on which to start the game
    """
    board = np.zeros([6, 7])
    return board


def cointoss(call):
    """
    Uses button input 0 or 1 and compares with randomly generated 0 or 1
    """
    coin = np.random.randint(0, 2)
    if coin == call:
        return True
    else:
        return False


def checkifvalid(board, column):
    """
    Takes input parameters board and column
    Checks if move is valid by checking for vacanciesin that column.
    Returns True if move is valid
    """
    valid = False  # just checks if there are any empty spaces in the column
    for j in range(6):
        if board[j][column] == 0:
            valid = True
    return valid


def dousermove(board, column):
    """
    Takes input parameters board and column and plays move
    """
    placed = False  # ensures counter isn't placed in every vacant space
    for i in range(5, -1, -1):
        if ((board[i][column] == 0) and (placed == False)):
            board[i][column] = 1
            placed = True
    return board


def checkgamestate(board):
    """
    Checks if computer or the player has won. It does this by:

    player won means the sum of the 4 counters is 4
    computer won means the sum of the 4 counters is 20

    If either has won, the winning discs are made into much larger numbers

    The function returns:
        0 if game is not over
        1 if player has won
        2 if computer has won
        3 if game is a draw
    """
    gamestate = 0

    for j in range(6):  # checks if player has won horizontally
        for i in range(4):
            if (board[j][i] + board[j][i+1]
                    + board[j][i+2] + board[j][i+3] == 4):

                # this is making the winning counters 100 instead of 1
                board[j][i] = 100
                board[j][i+1] = 100
                board[j][i+2] = 100
                board[j][i+3] = 100

                gamestate = 1

    for i in range(7):  # checks if player has won vertically
        for j in range(5, 2, -1):
            if (board[j][i] + board[j-1][i]
                    + board[j-2][i] + board[j-3][i] == 4):

                board[j][i] = 100
                board[j-1][i] = 100
                board[j-2][i] = 100
                board[j-3][i] = 100

                gamestate = 1

    for j in range(5, 2, -1):  # checks if player has won diagonally right
        for i in range(4):
            if (board[j][i] + board[j-1][i+1]
                    + board[j-2][i+2] + board[j-3][i+3] == 4):

                board[j][i] = 100
                board[j-1][i+1] = 100
                board[j-2][i+2] = 100
                board[j-3][i+3] = 100

                gamestate = 1

    for j in range(5, 2, -1):  # checks if player has won diagonally left
        for i in range(6, 2, -1):
            if (board[j][i] + board[j-1][i-1]
                    + board[j-2][i-2] + board[j-3][i-3] == 4):

                board[j][i] = 100
                board[j-1][i-1] = 100
                board[j-2][i-2] = 100
                board[j-3][i-3] = 100

                gamestate = 1

    for j in range(6):  # checks if computer has won horizontally
        for i in range(4):
            if (board[j][i] + board[j][i+1]
                    + board[j][i+2] + board[j][i+3] == 20):

                board[j][i] = 200
                board[j][i+1] = 200
                board[j][i+2] = 200
                board[j][i+3] = 200

                gamestate = 2

    for i in range(7):  # checks if computer has won vertically
        for j in range(5, 2, -1):
            if (board[j][i] + board[j-1][i]
                    + board[j-2][i] + board[j-3][i] == 20):

                board[j][i] = 200
                board[j-1][i] = 200
                board[j-2][i] = 200
                board[j-3][i] = 200

                gamestate = 2

    for j in range(5, 2, -1):  # checks if computer has won diagonally right
        for i in range(4):
            if (board[j][i] + board[j-1][i+1]
                    + board[j-2][i+2] + board[j-3][i+3] == 20):

                board[j][i] = 200
                board[j-1][i+1] = 200
                board[j-2][i+2] = 200
                board[j-3][i+3] = 200

                gamestate = 2

    for j in range(5, 2, -1):  # checks if player has won diagonally left
        for i in range(6, 2, -1):
            if (board[j][i] + board[j-1][i-1]
                    + board[j-2][i-2] + board[j-3][i-3] == 20):

                board[j][i] = 200
                board[j-1][i-1] = 200
                board[j-2][i-2] = 200
                board[j-3][i-3] = 200

                gamestate = 2

    # this is checking if there are any possible moves available to be played
    possiblemoves = False
    for i in range(0, 7, 1):
        if (board[0][i] == 0):
            possiblemoves = True
    # if there are no possible moves and noone has won, the game is a draw
    if ((possiblemoves == False) and (gamestate == 0)):
        gamestate = 3

    return gamestate


def plotgraphicalboard(board):
    """
    Takes input parameters array board and splits the array into:
    2 lists of x and y coordinates where the user has a counter
    2 lists of x and y coordinates where the computer has a counter
    2 lists of x and y coordinates of the winning counter for the user
    2 lists of x and y coordinates of the winning counters for the computer

    Plots user and computer counters

    A line is drawn through the winning discs
    """

    userx = []
    usery = []
    userwonx = []
    userwony = []
    computerx = []
    computery = []
    computerwonx = []
    computerwony = []

    for j in range(6):
        for i in range(7):
            if board[j][i] == 1:
                userx.append(i)
                usery.append(j)

            elif board[j][i] == 5:
                computerx.append(i)
                computery.append(j)

            elif board[j][i] == 100:
                userwonx.append(i)
                userwony.append(j)

            elif board[j][i] == 200:
                computerwonx.append(i)
                computerwony.append(j)

    # have to make it into an array so its easier to do calculations on it
    userx = np.array(userx) + 1
    usery = np.array(usery) - 1
    # corrects y coordinates since graph counts y up but arrays count y down
    usery = ((usery * -1) + 5)
    userwonx = np.array(userwonx) + 1
    userwony = np.array(userwony) - 1
    userwony = ((userwony * -1) + 5)

    # add 1 so the counter is in the right place on the diagram
    computerx = np.array(computerx) + 1
    # subtract 1 so the counter is in the right place on the diagram
    computery = np.array(computery) - 1
    computery = ((computery * -1) + 5)
    computerwonx = np.array(computerwonx) + 1
    computerwony = np.array(computerwony) - 1
    computerwony = ((computerwony * -1) + 5)

    f = makegraphicalboard()
    a = f.add_subplot(111)
    f.subplots_adjust(left=0.01, bottom=0.01, right=0.99, top=0.99)
    a.axis([0, 8, 0, 7])
    # f.subplots_adjust(left=0, bottom=0, right=1, top=1)
    a.plot()
    # a.xaxis.set_ticks([1, 2, 3, 4, 5, 6, 7, 8], [
    # 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
    # a.yaxis.set_ticks([1, 2, 3, 4, 5, 6, 7], ['1', '2', '3', '4', '5', '6'])

    # a.axis([0, 8, 0, 7])
    a.plot(userx, usery, marker='o', markersize=50,
           linestyle=' ', color='red')
    a.plot(computerx, computery, marker='o',
           markersize=50, linestyle=' ', color='yellow')
    a.plot(computerwonx, computerwony, marker='o', markersize=50,
           linestyle='-', linewidth=20, color='yellow')
    a.plot(userwonx, userwony, marker='o', markersize=50,
           linestyle='-', linewidth=20, color='red')
    a.grid(b=True, which='major', color='black', linestyle='-')
    # a.xticks([1, 2, 3, 4, 5, 6, 7, 8], ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    # ylabels = [item.get_text() for item in ]
    # a.yaxis.set_ticks([' ', '1', '2', '3', '4', '5', '6'])

    return f


def decidecomputermove(board):
    """
    Takes input parameter board and decides computer move.
    The computer will actively block near wins for players.
    It will also actively complete its near wins.

    When blocking or completing near wins, the computer will check the disc
    underneath the empty slot in the near win configuration. It will only block
    or complete if this slot is full. The prevents the computer from trying to
    block a slot but playing into the one underneath it.

    The computer will also play the middle if possible or the one next to the
    middle if this is not possible. This is a popular Connect 4 strategy
    """
    column = np.random.randint(0, 7)
    if board[5][3] == 0:  # plays in centre if possible
        column = 3

    elif board[5][2] == 0:
        column = 2  # stops player from going for one particular type of win

    for j in range(6):  # if player will win horizontally, plays in empty spot
        for i in range(4):
            if (board[j][i] + board[j][i+1]
                    + board[j][i+2] + board[j][i+3] == 3):

                if j == 5:  # if on the lowest row, ignores check underneath
                    if (board[j][i] == 0):
                        column = i

                    if (board[j][i+1] == 0):
                        column = i + 1

                    if (board[j][i+2] == 0):
                        column = i + 2

                    if (board[j][i+3] == 0):
                        column = i + 3

                else:
                    if ((board[j][i] == 0) and (board[j+1][i] != 0)):
                        column = i

                    if ((board[j][i+1] == 0) and (board[j+1][i+1] != 0)):
                        column = i + 1

                    if ((board[j][i+2] == 0) and (board[j+1][i+2] != 0)):
                        column = i + 2

                    if ((board[j][i+3] == 0) and (board[j+1][i+3] != 0)):
                        column = i + 3

    for i in range(7):  # if player will win vertically, plays in empty spot
        for j in range(5, 2, -1):
            if (board[j][i] + board[j-1][i]
                    + board[j-2][i] + board[j-3][i] == 3):
                column = i

    # if player will win diagonally right, plays in empty spot
    for j in range(5, 2, -1):
        for i in range(4):
            if (board[j][i] + board[j-1][i+1]
                    + board[j-2][i+2] + board[j-3][i+3] == 3):

                if j == 5:
                    if(board[j][i] == 0):
                        column = i

                    if ((board[j-1][i+1] == 0) and (board[j][i+1] != 0)):
                        column = i + 1

                    if ((board[j-2][i+2] == 0) and (board[j-1][i+2] != 0)):
                        column = i + 2

                    if ((board[j-3][i+3] == 0) and (board[j-2][i+3] != 0)):
                        column = i + 3

                else:
                    if ((board[j][i] == 0) and board[j+1][i] != 0):
                        column = i

                    if ((board[j-1][i+1] == 0) and (board[j][i+1] != 0)):
                        column = i + 1

                    if ((board[j-2][i+2] == 0) and (board[j-1][i+2] != 0)):
                        column = i + 2

                    if ((board[j-3][i+3] == 0) and (board[j-2][i+3] != 0)):
                        column = i + 3

    # if player will win diagonally left, plays in empty spot
    for j in range(5, 2, -1):
        for i in range(6, 2, -1):
            if (board[j][i] + board[j-1][i-1]
                    + board[j-2][i-2] + board[j-3][i-3] == 3):

                if j == 5:
                    if(board[j][i] == 0):
                        column = i

                    if ((board[j-1][i-1] == 0) and (board[j][i-1] != 0)):
                        column = i - 1

                    if ((board[j-2][i-2] == 0) and (board[j-1][i-2] != 0)):
                        column = i - 2

                    if ((board[j-3][i-3] == 0) and (board[j-2][i-3] != 0)):
                        column = i - 3

                else:
                    if ((board[j][i] == 0) and board[j+1][i] != 0):
                        column = i

                    if ((board[j-1][i-1] == 0) and (board[j][i-1] != 0)):
                        column = i - 1

                    if ((board[j-2][i-2] == 0) and (board[j-1][i-2] != 0)):
                        column = i - 2

                    if ((board[j-3][i-3] == 0) and (board[j-2][i-3] != 0)):
                        column = i - 3

    for j in range(6):  # if comp will win horizontally, plays in empty spot
        for i in range(4):
            if (board[j][i] + board[j][i+1]
                    + board[j][i+2] + board[j][i+3] == 15):

                if j == 5:
                    if (board[j][i] == 0):
                        column = i

                    if (board[j][i+1] == 0):
                        column = i + 1

                    if (board[j][i+2] == 0):
                        column = i + 2

                    if (board[j][i+3] == 0):
                        column = i + 3

                else:
                    if ((board[j][i] == 0) and (board[j+1][i] != 0)):
                        column = i

                    if ((board[j][i+1] == 0) and (board[j+1][i+1] != 0)):
                        column = i + 1

                    if ((board[j][i+2] == 0) and (board[j+1][i+2] != 0)):
                        column = i + 2

                    if ((board[j][i+3] == 0) and (board[j+1][i+3] != 0)):
                        column = i + 3

    for i in range(7):  # if comp will win vertically, plays in empty spot
        for j in range(5, 2, -1):
            if (board[j][i] + board[j-1][i]
                    + board[j-2][i] + board[j-3][i] == 15):

                column = i

    # if comp will win diagonally right, plays in empty spot
    for j in range(5, 2, -1):
        for i in range(4):
            if (board[j][i] + board[j-1][i+1]
                    + board[j-2][i+2] + board[j-3][i+3] == 15):

                if j == 5:
                    if(board[j][i] == 0):
                        column = i

                    if ((board[j-1][i+1] == 0) and (board[j][i+1] != 0)):
                        column = i + 1

                    if ((board[j-2][i+2] == 0) and (board[j-1][i+2] != 0)):
                        column = i + 2

                    if ((board[j-3][i+3] == 0) and (board[j-2][i+3] != 0)):
                        column = i + 3

                else:
                    if ((board[j][i] == 0) and board[j+1][i] != 0):
                        column = i

                    if ((board[j-1][i+1] == 0) and (board[j][i+1] != 0)):
                        column = i + 1

                    if ((board[j-2][i+2] == 0) and (board[j-1][i+2] != 0)):
                        column = i + 2

                    if ((board[j-3][i+3] == 0) and (board[j-2][i+3] != 0)):
                        column = i + 3

    # if computer will win diagonally left, plays in empty spot
    for j in range(5, 2, -1):
        for i in range(6, 2, -1):
            if (board[j][i] + board[j-1][i-1]
                    + board[j-2][i-2] + board[j-3][i-3] == 15):

                if j == 5:
                    if(board[j][i] == 0):
                        column = i

                    if ((board[j-1][i-1] == 0) and (board[j][i-1] != 0)):
                        column = i - 1

                    if ((board[j-2][i-2] == 0) and (board[j-1][i-2] != 0)):
                        column = i - 2

                    if ((board[j-3][i-3] == 0) and (board[j-2][i-3] != 0)):
                        column = i - 3

                else:
                    if ((board[j][i] == 0) and board[j+1][i] != 0):
                        column = i

                    if ((board[j-1][i-1] == 0) and (board[j][i-1] != 0)):
                        column = i - 1

                    if ((board[j-2][i-2] == 0) and (board[j-1][i-2] != 0)):
                        column = i - 2

                    if ((board[j-3][i-3] == 0) and (board[j-2][i-3] != 0)):
                        column = i - 3

    return column


def docomputermove(board, column):
    """
    Takes input parameters board and column
    This is almost identical to the dousermove function.
    Places the coin in the lowest unoccupied slot on the board.
    """
    placed = False
    for i in range(5, -1, -1):
        if ((board[i][column] == 0) and (placed == False)):
            board[i][column] = 5
            placed = True
    return board
