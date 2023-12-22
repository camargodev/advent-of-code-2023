class Number:
    def __init__(self, column, row_start, row_end, value):
        self.column = column
        self.row_start = row_start
        self.row_end = row_end
        self.value = value

    def get_cells(self):
        return [(self.column, row_index) for row_index in range(self.row_start, self.row_end)]