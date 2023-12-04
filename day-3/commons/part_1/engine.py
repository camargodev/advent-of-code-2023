import re
from commons.numbers_finder import NumbersFinder
from commons.adjacent_cells_calculator import AdjacentCellsCalculator

SYMBOL = 'S'

class Engine:
    def run(self, lines):
        symbol_coords = set()
        for line_index in range(len(lines)):
            line = re.sub("[^0-9\.\n]", SYMBOL, lines[line_index])
            for column_index in range(len(line)):
                if line[column_index] != SYMBOL:
                    continue
                for adjacent_coord in AdjacentCellsCalculator.calculate(column_index, line_index):
                    symbol_coords.add(adjacent_coord)

        numbers = NumbersFinder().find(lines)
    
        return sum([self.calculate_value_for_number(number, symbol_coords) for number in numbers])
      
    def calculate_value_for_number(self, number, coords_touched_by_symbol):
        for cell in number.get_cells():
            if cell in coords_touched_by_symbol:
                return number.value
        return 0
