from position import Position
from tkinter import *

class Board:
    def __init__(self, board, GUI=False):
        self.q = len(board)
        self.qs = int(self.q ** (1 / 2))
        self.board = board  # nested list
        self.root = Tk() if GUI else None
        self.GUI = GUI

        # root.mainloop()
    def getSize(self):
        return len(self.board)

    def getValueAt(self, position):
        return self.board[position.row][position.col]

    def setValueAt(self, position, value, forsure=True):

        self.board[position.row][position.col] = value
        if not self.GUI:
            return
        else:
            if forsure:
                if self.board[position.row][position.col] == 0:
                    Label(self.root, text=value, relief=RIDGE,borderwidth=4, height=2,bg='white', width=5).grid(row=position.row, column=position.col)
                else:
                    Label(self.root, text=value, relief=RIDGE,borderwidth=4, height=2,bg='green', fg='blue',width=5).grid(row=position.row, column=position.col)
            else:
                if self.board[position.row][position.col] == 0:
                    Label(self.root, text=value, relief=RIDGE,borderwidth=4, height=2,bg='white', width=5).grid(row=position.row, column=position.col)
                else:
                    Label(self.root, text=value, relief=RIDGE,borderwidth=4, height=2,bg='blue', fg='white',width=5).grid(row=position.row, column=position.col)

            self.root.update()

    def __repr__(self):
        color = lambda n: "\033[0;32m%s\033[0;38m" % n if n != 0 else "\033[0;31m%s\033[0;38m" % n
        # return "\033[0;32mkakapipi\033[0;38m"
        return ',\n'.join(', '.join([color(n)for n in row]) for row in self.board)

    def emptySpot(self):
        for row in range(self.q):
            for col in range(self.q):
                if self.board[row][col] == 0:
                    return Position(col, row)

    def isSolved(self):
        for col in range(self.q):
            for row in range(self.q):
                if self.board[row][col] == 0:
                    return False
        return True

    def can_place_horizontally(self, value, position):
        for col in range(self.q):
            if self.board[position.row][col] == value:
                return False
        return True

    def can_place_vertically(self, value, position):
        for row in range(self.q):
            if self.board[row][position.col] == value:
                return False
        return True

    def can_place_in_local_square(self, value, position):
        for row in range((position.row // self.qs) * self.qs, (position.row // self.qs) * self.qs + self.qs):
            for col in range((position.col // self.qs) * self.qs, (position.col // self.qs) * self.qs + self.qs):
                if self.board[row][col] == value:
                    return False
        return True

    def can_place_at(self, value, position):
        if not self.can_place_horizontally(value, position):
            return False
        if not self.can_place_vertically(value, position):
            return False
        if not self.can_place_in_local_square(value, position):
            return False
        return True

    def get_square_of_pos(self, pos):
        return Position(pos.col // self.qs, pos.row // self.qs)

    def get_unfilled_squares(self):
        return sum([1 if value == 0 else 0 for row in self.board for value in row])
