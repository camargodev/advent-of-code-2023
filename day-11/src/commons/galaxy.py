class Galaxy:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class GalaxyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def calculate_distance(self, empty_rows, empty_cols, empty_space_multiplier):
        return self.calculate_base_distance() + self.calculate_empty_distance(empty_rows, empty_cols, empty_space_multiplier)

    def calculate_base_distance(self):
        return abs(self.first.row - self.second.row) + abs(self.first.col - self.second.col)
    
    def calculate_empty_distance(self, empty_rows, empty_cols, empty_space_multiplier):
        min_x, max_x = min(self.first.row, self.second.row), max(self.first.row, self.second.row)
        min_y, max_y = min(self.first.col, self.second.col), max(self.first.col, self.second.col)
        empty_rows_count = [row for row in range(min_x, max_x) if row in empty_rows]
        empty_cols_count = [row for row in range(min_y, max_y) if row in empty_cols]
        return (empty_space_multiplier-1)*len(empty_rows_count) + (empty_space_multiplier-1)*len(empty_cols_count)