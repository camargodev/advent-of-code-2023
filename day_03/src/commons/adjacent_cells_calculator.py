class AdjacentCellsCalculator:
    @staticmethod
    def calculate(column, row):
        left = column-1
        right = column+1
        up = row-1
        down = row+1
        return [(up,  left), (up,  column), (up,  right),
                (row, left),                (row, right),
                (down,left), (down,column), (down,right)]
