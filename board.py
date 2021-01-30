from position import position
q = 16
qs = 4
class board:
    def __init__(self, board):
        assert len(board) == q
        self.board = board #  nested list

    def getValueAt(self, position):
        return self.board[position.row][position.col]

    def setValueAt(self, position, value):
        # print("Setting value {} at position {}".format(value, position))
        self.board[position.row][position.col] = value

    def __repr__(self):
        return ',\n'.join(str(row) for row in self.board)


    def emptySpot(self):
        for row in range(q):
            for col in range(q):
                if self.board[row][col] == 0:
                    return position(col, row)

    def isFilled(self):
        for col in range(q):
            for row in range(q):
                if self.board[row][col] == 0:
                    return False
        return True

    def can_place_horizontally(self, value, position):
        for col in range(q):
            if self.board[position.row][col] == value:
                return False
        return True

    def can_place_vertically(self, value, position):
        for row in range(q):
            if self.board[row][position.col] == value:
                return False
        return True

    def can_place_in_local_square(self, value, position):
        for row in range((position.row // qs) * qs, (position.row // qs) * qs + qs):
            for col in range((position.col // qs) * qs, (position.col // qs) * qs + qs):
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
        return position(pos.col//qs, pos.row//qs)