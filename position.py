class position:
    def __init__(self, col, row):
        self.row = row
        self.col = col

    def __repr__(self):
        return "({}, {})".format(self.col, self.row)

    def greater_than(self, other):
        if self.row > other.row:
            return True
        if self.row == other.row:
            if self.col > other.col:
                return True
        return False

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.row != other.row:
            return False
        if self.col != other.col:
            return False
        return True

    def __hash__(self) -> int:
        prime = 31
        result = 1
        result = prime * result + self.col
        result = prime * result + self.row
        return result


assert(position(1, 2) == position(1, 2))