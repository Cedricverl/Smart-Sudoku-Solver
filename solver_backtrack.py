"""
    Recursive algorithm for solving 4x4 sudoku puzzle.
    Board is a nested list with for each row a different list with length 9
"""
import math
import time
from position import position
from board import board

bw=10
q = 16
qs = int(math.sqrt(q))
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "o"]
print("values: {}\n".format(values))
max_pos = position(0, 0)

def solve_sudoku(board):
    """
    solves the sudoku on the given board
    - mutates board
    - returns True when done
    """
    global max_pos
    if board.isFilled():
        return True

    emptypos = board.emptySpot()
    for value in values:
        if board.can_place_at(value, emptypos):
            if emptypos.greater_than(max_pos):
                max_pos = emptypos
                print(max_pos)
            board.setValueAt(emptypos, value)
            if solve_sudoku(board):
                return True
            board.setValueAt(emptypos, 0)

    return False


if __name__ == "__main__":
    starttime = time.perf_counter()
    # board_given = [[0]*q for i in range(q)]  # empty board
    board_given =  [[0, 3, 0, 6, 0, 0, 8, 9, 0],
                    [0, 0, 0, 0, 4, 0, 0, 0, 0],
                    [0, 0, 0, 8, 0, 0, 5, 0, 7],
                    [0, 9, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 6, 4, 0, 5],
                    [3, 0, 0, 0, 0, 4, 0, 1, 0],
                    [0, 6, 0, 0, 1, 0, 0, 3, 0],
                    [0, 0, 1, 0, 0, 0, 2, 0, 0],
                    [4, 0, 0, 0, 2, 0, 0, 0, 0]]
    # board_given = [[0, 2, 0, 0, 0, 7, 0,"a", 0, 9, 0, 0, 0, "c", 0, 0],
    #                ["e", 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 6, "f", "d", 0, 7],
    #                [0, 0, 0, 0, 6, 9, 3, 0, 0, 0, 0, 0, 0, 0, 2, "o"],
    #                [5, "b", 0, 0, 0, 0, 0, 0, "o", 0, 7, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, "a", 0, 0, 0, "c"],
    #                [0, 9, 0, 0, "o", 0, 0, 0, 0, 6, 0, 1, "b", 0, 5, 0],
    #                [0, 0, 0, "o", 7, 0, 0, 8, 0, 0, 2, 0, 0, "a", 3, 0],
    #                [0, 7, 6, 1, 0, 0, "a", "f", 0, 8, 0, 4, 0, 0, 0, 0],
    #                [4, 0, "d", 0, 5, 0, 0, "b", 0, 0, 6, 0, "e", 0, "a", 2],
    #                [0, 0, 0, 0, "e", 0, 0, 7, 8, 0, 4, "c", 0, 0, "d", 0],
    #                [0, 3, 0, 0, 0, 0, 1, "d", 5, 7, 0, 0, 0, 0, 0, 6],
    #                [0, "o", 0, 0, "c", 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    #                [0, 0, 0, "d", 3, 0, 0, "o", "c", "f", 0, 0, "a", 0, 0, 0],
    #                [8, 0, 0, 3, "b", "a", 0, 0, 0, 0, "o", 0, "c", 6, 0, 1],
    #                [0, 0, "c", "b", 0, "f", 0, 2, 0, 0, 9, 5, 0, 0, "e", 0],
    #                [0, 0, 0, 0, 9, 1, 0, 0, 0, "b", 3, 0, 5, 4, 7, 0]]
    board_given_partially_solved = [[0, 2, 0, 0, 0, 7, 0, 'a', 0, 9, 0, 0, 0, 'c', 0, 0],
                                    ['e', 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 6, 'f', 'd', 0, 7],
                                    [0, 0, 0, 0, 6, 9, 3, 0, 0, 0, 0, 0, 0, 0, 2, 'o'],
                                    [5, 'b', 0, 0, 0, 'd', 0, 0, 'o', 0, 7, 0, 0, 3, 0, 'a'],
                                    [0, 0, 0, 0, 1, 0, 0, 4, 0, 'o', 0, 'a', 7, 0, 6, 'c'],
                                    [0, 9, 0, 0, 'o', 0, 0, 3, 7, 6, 0, 1, 'b', 0, 5, 0],
                                    [0, 0, 0, 'o', 7, 0, 0, 8, 0, 0, 2, 0, 1, 'a', 3, 0],
                                    [0, 7, 6, 1, 'd', 0, 'a', 'f', 0, 8, 0, 4, 2, 0, 'o', 0],
                                    [4, 0, 'd', 0, 5, 8, 0, 'b', 0, 0, 6, 0, 'e', 0, 'a', 2],
                                    [0, 0, 0, 0, 'e', 0, 0, 7, 8, 0, 4, 'c', 0, 0, 'd', 0],
                                    [0, 3, 0, 0, 'a', 4, 1, 'd', 5, 7, 0, 0, 0, 0, 'c', 6],
                                    [0, 'o', 0, 0, 'c', 2, 0, 9, 0, 0, 0, 0, 3, 0, 0, 0],
                                    [0, 0, 0, 'd', 3, 0, 7, 'o', 'c', 'f', 0, 0, 'a', 2, 0, 0],
                                    [8, 0, 0, 3, 'b', 'a', 'd', 0, 0, 0, 'o', 7, 'c', 6, 0, 1],
                                    [7, 0, 'c', 'b', 4, 'f', 8, 2, 6, 0, 9, 5, 'd', 'o', 'e', 3],
                                    [0, 0, 0, 0, 9, 1, 'c', 6, 0, 'b', 3, 0, 5, 4, 7, 0]]
    board = board(board_given_partially_solved)
    print(board)
    print("Solving sudoku...")

    solve_sudoku(board)

    stoptime = time.perf_counter()
    timedelta = stoptime-starttime
    print("elapsed time: ", timedelta)
    print(board)
#################################
# convention for notation:      #
# position: COL, ROW            #
# board: board[row][col]        #
#################################

