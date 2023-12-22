EMPTY="."
HORIZONTAL_SPLIT="-"
VERTICAL_SPLIT="|"
DIAGONAL="\\"
INVERSE_DIAGIONAL="/"

class Tile:
    def __init__(self, direction, row, col):
        self.direction = direction
        self.row = row
        self.col = col

    def __str__(self):
        return f"Tile(row={self.row}, col={self.col}, direction='{self.direction}')"

    def __hash__(self):
        return hash((self.row, self.col, self.direction))

    def __eq__(self, other):
        if not isinstance(other, Tile):
            return False
        return (
            self.row == other.row
            and self.col == other.col
            and self.direction == other.direction
        )