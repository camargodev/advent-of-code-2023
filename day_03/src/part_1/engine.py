import re
from src.commons.numbers_finder import NumbersFinder
from src.commons.adjacent_cells_calculator import AdjacentCellsCalculator

STANDARD_SYMBOL = 'S'
ANY_SYMBOL = "[^0-9\.\n]"

class EngineManager:
    def run(self, lines):
        symbol_coords = self.find_symbols_coords(lines)
        numbers = NumbersFinder().find(lines)
    
        return sum([self.calculate_value_for_number(number, symbol_coords) for number in numbers])
      
    def calculate_value_for_number(self, number, coords_touched_by_symbol):
        for cell in number.get_cells():
            if cell in coords_touched_by_symbol:
                return number.value
        return 0
    
    def find_symbols_coords(self, lines):
        symbol_coords = set()
        for row_index, raw_row in enumerate(lines):
            row = re.sub(ANY_SYMBOL, STANDARD_SYMBOL, raw_row)
            for column_index, cell in enumerate(row):
                if cell == STANDARD_SYMBOL:
                    symbol_coords.update(AdjacentCellsCalculator.calculate(column_index, row_index))
        return symbol_coords
