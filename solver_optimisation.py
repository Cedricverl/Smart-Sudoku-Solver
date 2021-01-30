"""
    Recursove algorithm for solving the sudoku puzzle.
    Board is a nested list with length 16
"""
import math
import time
from position import position
from board import board
import pprint

bw = 10
q = 16
qs = int(math.sqrt(q))
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # , "a", "b", "c", "d", "e", "f", "o"]
print("values: {}\n".format(values))
max_pos = (0, 0)

def place_atomic_values(board, pv):
    for pos in pv.keys():
        if len(pv[pos]) == 1:
            board.setValueAt(pos, pv[pos][0])

def is_on_same_row(positions):
    for i in range(len(positions)-1):
        if not positions[i].row == positions[i+1].row:
            return False
    return True
# assert is_on_same_row([position(4, 2), position(6, 2), position(8, 2)])
# assert not is_on_same_row([position(5, 3), position(4, 4)])

def is_on_same_col(positions):
    for i in range(len(positions)-1):
        if not positions[i].col == positions[i+1].col:
            return False
    return True

def is_on_same_square(positions):
    for i in range(len(positions)-1):
        if not board.get_square_of_pos(positions[i]) == board.get_square_of_pos(positions[i+1]):
            return False
    return True

def getKeysWithValues(dict, value):
    result = []
    for key in dict:
        if dict[key] == value:
            result.append(key)
    return result

def unique_check_col(board, pv):
    for col in range(q):
        all_pos_in_row = []
        for row in range(q):
            if position(col, row) in pv:
                for i in pv[position(col, row)]:
                    all_pos_in_row.append(i)
        # print(list(set(all_pos_in_row)))
        for value in values:
            count = all_pos_in_row.count(value)
            if count == 1:
                for row in range(q):
                    if position(col, row) in pv and value in pv[position(col, row)]:
                        # print("POS WITH ONE THING: {} with value {}".format(position(col, row), value))
                        print("col placement")
                        board.setValueAt(position(col, row), value)


def unique_check_row(board, pv):
    for row in range(q):
        all_pos_in_col = []
        for col in range(q):
            if position(col, row) in pv:
                for i in pv[position(col, row)]:
                    all_pos_in_col.append(i)
        # print(list(all_pos_in_col))
        for value in values:
            count = all_pos_in_col.count(value)
            if count == 1:
                # print("GOTCHA")
                for col in range(q):
                    if position(col, row) in pv and value in pv[position(col, row)]:
                        # print("POS WITH ONE THING: {} with value {}".format(position(col, row), value))
                        print("row placement")
                        board.setValueAt(position(col, row), value)


def unique_check_square(board, pv):
    # positions = [position(0, 0), position(3, 0), position(6, 0), position(0, 3), position(3, 3), position(6, 3),
                 # position(0, 6), position(3, 6), position(6, 6)]
    positions = [position(col, row) for col in [0, 4, 8, 12] for row in [0, 4, 8, 12]]
    for positionsquare in positions:
        all_pos_in_square = []
        for row in range((positionsquare.row // qs) * qs, (positionsquare.row // qs) * qs + qs):
            for col in range((positionsquare.col // qs) * qs, (positionsquare.col // qs) * qs + qs):
                if position(col, row) in pv:
                    for i in pv[position(col, row)]:
                        all_pos_in_square.append(i)
        # print("square {}, all pos in square: {}".format(positionsquare, all_pos_in_square))
        for value in values:
            count = all_pos_in_square.count(value)
            if count == 1:
                # print("GOTCHA")
                for row in range((positionsquare.row // qs) * qs, (positionsquare.row // qs) * qs + qs):
                    for col in range((positionsquare.col // qs) * qs, (positionsquare.col // qs) * qs + qs):
                        if position(col, row) in pv and value in pv[position(col, row)]:
                            # print("POS WITH ONE THING: {} with value {}".format(position(col, row), value))
                            print("square placement")
                            board.setValueAt(position(col, row), value)

def reduce_pv_row(pv, positions, pvlist):
    if is_on_same_row(positions):  # remove all the values in pvlist from the other positions in the same row
        row_of_positions = positions[0].row
        for col in range(q):
            pos = position(col, row_of_positions)
            if pos in pv.keys() and pos not in positions:
                # print("ROW removing from pos {} the values {} that are not in {}".format(pos, pv[pos], pvlist))
                pv[pos] = [x for x in pv[pos] if x not in pvlist]

def reduce_pv_col(pv, positions, pvlist):
    if is_on_same_col(positions):
        col_of_positions = positions[0].col
        for row in range(q):
            pos = position(col_of_positions, row)
            if pos in pv.keys() and pos not in positions:
                # print("COL removing from pos {} the values {} that are not in {}".format(pos, pv[pos], pvlist))

                pv[pos] = [x for x in pv[pos] if x not in pvlist]

def reduce_pv_square(pv, positions, pvlist):
    if is_on_same_square(positions):
        square_of_positions = positions[0]
        for row in range((square_of_positions.row // qs) * qs, (square_of_positions.row // qs) * qs + qs):
            for col in range((square_of_positions.col // qs) * qs, (square_of_positions.col // qs) * qs + qs):
                pos = position(col, row)
                if pos in pv.keys() and pos not in positions:
                    # print("SQUARE removing from pos {} the values {} that are not in {}".format(pos, pv[pos],pvlist))
                    pv[pos] = [x for x in pv[pos] if x not in pvlist]

def solve_sudoku(board):
    """
    solves the sudoku on the given board
    - mutates board
    - returns True when done
    """


    for i in range(5):
        print("################################")

        pv = {}
        for row in range(q):
            for col in range(q):
                pos = position(col, row)
                if board.getValueAt(pos) == 0:
                    pv[pos] = [value for value in values if board.can_place_at(value, pos)]

        # pp.pprint(pv)
        # print(board)
        for i in range(2):
            for pvlist in pv.values():
                count = list(pv.values()).count(pvlist)
                # print("COUNT: {} AND PVLIST: {} LEN PVLIST: {}".format(count, pvlist,  len(pvlist)))
                if count == len(pvlist):
                    print("SAME VALUES:  {}".format(pvlist))
                    positions = getKeysWithValues(pv, pvlist)
                    print("IN POSITIONS: {}".format(positions))
                    reduce_pv_row(pv, positions, pvlist)
                    reduce_pv_col(pv, positions, pvlist)
                    reduce_pv_square(pv, positions, pvlist)

        place_atomic_values(board, pv)
        unique_check_col(board, pv)
        unique_check_row(board, pv)
        unique_check_square(board, pv)
        pp.pprint(pv)


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=bw)
    starttime = time.perf_counter()
    # board_given = [[0]*q for i in range(q)]  # empty board
    # board_given =  [[0, 3, 0, 6, 0, 0, 8, 9, 0],
    #                 [0, 0, 0, 0, 4, 0, 0, 0, 0],
    #                 [0, 0, 0, 8, 0, 0, 5, 0, 7],
    #                 [0, 9, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 6, 4, 0, 5],
    #                 [3, 0, 0, 0, 0, 4, 0, 1, 0],
    #                 [0, 6, 0, 0, 1, 0, 0, 3, 0],
    #                 [0, 0, 1, 0, 0, 0, 2, 0, 0],
    #                 [4, 0, 0, 0, 2, 0, 0, 0, 0]]

    board_given = [[0, 2, 0, 0, 0, 7, 0,"a", 0, 9, 0, 0, 0, "c", 0, 0],
                   ["e", 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 6, "f", "d", 0, 7],
                   [0, 0, 0, 0, 6, 9, 3, 0, 0, 0, 0, 0, 0, 0, 2, "o"],
                   [5, "b", 0, 0, 0, 0, 0, 0, "o", 0, 7, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, "a", 0, 0, 0, "c"],
                   [0, 9, 0, 0, "o", 0, 0, 0, 0, 6, 0, 1, "b", 0, 5, 0],
                   [0, 0, 0, "o", 7, 0, 0, 8, 0, 0, 2, 0, 0, "a", 3, 0],
                   [0, 7, 6, 1, 0, 0, "a", "f", 0, 8, 0, 4, 0, 0, 0, 0],
                   [4, 0, "d", 0, 5, 0, 0, "b", 0, 0, 6, 0, "e", 0, "a", 2],
                   [0, 0, 0, 0, "e", 0, 0, 7, 8, 0, 4, "c", 0, 0, "d", 0],
                   [0, 3, 0, 0, 0, 0, 1, "d", 5, 7, 0, 0, 0, 0, 0, 6],
                   [0, "o", 0, 0, "c", 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
                   [0, 0, 0, "d", 3, 0, 0, "o", "c", "f", 0, 0, "a", 0, 0, 0],
                   [8, 0, 0, 3, "b", "a", 0, 0, 0, 0, "o", 0, "c", 6, 0, 1],
                   [0, 0, "c", "b", 0, "f", 0, 2, 0, 0, 9, 5, 0, 0, "e", 0],
                   [0, 0, 0, 0, 9, 1, 0, 0, 0, "b", 3, 0, 5, 4, 7, 0]]
    count = 0
    for row in board_given:
        for value in row:
            if value != 0:
                count += 1
    print("NOT solved with {} pos filled.".format(count))

    board = board(board_given)

    print(board)
    print("Solving sudoku...")

    solve_sudoku(board)
    count = 0
    for row in board_given:
        for value in row:
            if value != 0:
                count += 1
    print("solved with {} pos filled.".format(count))

    stoptime = time.perf_counter()
    timedelta = stoptime-starttime
    print("elapsed time: ", timedelta)
    print(board)
#################################
# convention for notation:      #
# position: COL, ROW            #
# board: board[row][col]        #
#################################