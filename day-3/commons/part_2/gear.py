from commons.adjacent_cells_calculator import AdjacentCellsCalculator

class Gear:
    def __init__(self, row, column):
        self.numbers = []
        self.row = row
        self.column = column
    
    def get_product(self):
        if len(self.numbers) == 2:
            return self.numbers[0] * self.numbers[1]
        return 0
    
    def touches_number(self, number):
        cells_touched_by_gear = AdjacentCellsCalculator.calculate(self.column, self.row)
        for cell in number.get_cells():
            if cell in cells_touched_by_gear:
                return True
        return False