"""
    Recursove algorithm for solving the sudoku puzzle.
    Board is a nested list with length 16
"""
import time
import board_templates
from position import Position
from board import Board



class Sudoku:
    def __init__(self, board):
        self.board = board
        self.q = board.getSize()
        self.qs = int(self.q**(1/2))
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "o"] if self.q == 16 else [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.max_pos = Position(0, 0)  # only used in backtracking algorithm

    def place_atomic_values(self, pv):
        for pos in pv.keys():
            if len(pv[pos]) == 1:
                self.board.setValueAt(pos, pv[pos][0])

    def is_on_same_row(self, positions):
        return all([positions[i].row == positions[i+1].row for i in range(len(positions)-1)])

    def is_on_same_col(self, positions):
        return all([positions[i].col == positions[i+1].col for i in range(len(positions)-1)])

    def is_on_same_square(self, positions):
        return all([self.board.get_square_of_pos(positions[i]) == self.board.get_square_of_pos(positions[i + 1]) for i in range(len(positions) - 1)])

    def unique_check_col(self, pv):
        for col in range(self.q):
            all_pos_in_row = []
            for row in range(self.q):
                if Position(col, row) in pv:
                    for i in pv[Position(col, row)]:
                        all_pos_in_row.append(i)
            for value in self.values:
                count = all_pos_in_row.count(value)
                if count == 1:
                    for row in range(self.q):
                        if Position(col, row) in pv and value in pv[Position(col, row)]:
                            # print("col placement")
                            self.board.setValueAt(Position(col, row), value)

    def unique_check_row(self, pv):
        for row in range(self.q):
            all_pos_in_col = []
            for col in range(self.q):
                if Position(col, row) in pv:
                    for i in pv[Position(col, row)]:
                        all_pos_in_col.append(i)
            for value in self.values:
                count = all_pos_in_col.count(value)
                if count == 1:
                    for col in range(self.q):
                        if Position(col, row) in pv and value in pv[Position(col, row)]:
                            # print("row placement")
                            self.board.setValueAt(Position(col, row), value)

    def unique_check_square(self, pv):
        positions = [Position(col, row) for col in [0, 4, 8, 12] for row in [0, 4, 8, 12]]
        for positionsquare in positions:
            all_pos_in_square = []
            for row in range((positionsquare.row // self.qs) * self.qs, (positionsquare.row // self.qs) * self.qs + self.qs):
                for col in range((positionsquare.col // self.qs) * self.qs, (positionsquare.col // self.qs) * self.qs + self.qs):
                    if Position(col, row) in pv:
                        for i in pv[Position(col, row)]:
                            all_pos_in_square.append(i)
            for value in self.values:
                count = all_pos_in_square.count(value)
                if count == 1:
                    for row in range((positionsquare.row // self.qs) * self.qs, (positionsquare.row // self.qs) * self.qs + self.qs):
                        for col in range((positionsquare.col // self.qs) * self.qs, (positionsquare.col // self.qs) * self.qs + self.qs):
                            if Position(col, row) in pv and value in pv[Position(col, row)]:
                                # print("square placement")
                                self.board.setValueAt(Position(col, row), value)

    def reduce_pv_row(self, pv, positions, pvlist):
        if self.is_on_same_row(positions):  # remove all the values in pvlist from the other positions in the same row
            row_of_positions = positions[0].row
            for col in range(self.q):
                pos = Position(col, row_of_positions)
                if pos in pv.keys() and pos not in positions:
                    pv[pos] = [x for x in pv[pos] if x not in pvlist]

    def reduce_pv_col(self, pv, positions, pvlist):
        if self.is_on_same_col(positions):
            col_of_positions = positions[0].col
            for row in range(self.q):
                pos = Position(col_of_positions, row)
                if pos in pv.keys() and pos not in positions:
                    pv[pos] = [x for x in pv[pos] if x not in pvlist]

    def reduce_pv_square(self, pv, positions, pvlist):
        if self.is_on_same_square(positions):
            square_of_positions = positions[0]
            for row in range((square_of_positions.row // self.qs) * self.qs, (square_of_positions.row // self.qs) * self.qs + self.qs):
                for col in range((square_of_positions.col // self.qs) * self.qs, (square_of_positions.col // self.qs) * self.qs + self.qs):
                    pos = Position(col, row)
                    if pos in pv.keys() and pos not in positions:
                        pv[pos] = [x for x in pv[pos] if x not in pvlist]

    def solve(self):
        """
        solves the sudoku on the given board using Crook's algorithm
        - mutates board
        - Uses backtrack algorithm when Crook didn't do the job
        """
        print("Solving sudoku...")
        j = 0
        while not self.board.isSolved() and j < 150:
            j += 1
            pv = {}
            for row in range(self.q):
                for col in range(self.q):
                    pos = Position(col, row)
                    if self.board.getValueAt(pos) == 0:
                        pv[pos] = [value for value in self.values if self.board.can_place_at(value, pos)]

            for pvlist in pv.values():
                count = list(pv.values()).count(pvlist)
                if count == len(pvlist):
                    positions = [key for key in pv if pv[key] == pvlist]
                    self.reduce_pv_row(pv, positions, pvlist)
                    self.reduce_pv_col(pv, positions, pvlist)
                    self.reduce_pv_square(pv, positions, pvlist)

            self.place_atomic_values(pv)
            self.unique_check_col(pv)
            self.unique_check_row(pv)
            self.unique_check_square(pv)
        if j == 150:  # return True when solved else False
            print("Sudoku was too hard for Crook, let's brute force!")
            self.solve_backtrack()
        print("Sudoku solved!")
        return True

    def solve_backtrack(self):
        """
        solves the sudoku on the given board using brute force method
        - mutates board
        - returns True when done
        """
        if self.board.isSolved():
            return True
        emptypos = self.board.emptySpot()
        for value in self.values:
            if self.board.can_place_at(value, emptypos):
                if emptypos.greater_than(self.max_pos):
                    self.max_pos = emptypos
                    # print(self.max_pos)
                self.board.setValueAt(emptypos, value)
                if self.solve_backtrack():
                    return True
                self.board.setValueAt(emptypos, 0)
        return False


if __name__ == "__main__":
    starttime = time.perf_counter()  # start timer

    board = Board(board_templates.board_normal_medium)
    sudoku = Sudoku(board)

    print("Sudoku unsolved with %s unfilled squares." % sudoku.board.get_unfilled_squares())
    print(board)

    sudoku.solve()  # where the magic happens

    timedelta = time.perf_counter()-starttime  # stop counter and measure difference (in seconds)
    print("elapsed time: %ssec" % timedelta)
    print(board)


#################################
# convention for notation:      #
# position: COL, ROW            #
# board: board[row][col]        #
#################################
