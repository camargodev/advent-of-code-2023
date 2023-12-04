import re
from commons.numbers_finder import NumbersFinder
from commons.adjacent_cells_calculator import AdjacentCellsCalculator

SYMBOL = 'S'
DIGITS = [str(num) for num in range(10)]

def calculate_value_for_number(number, coords_touched_by_symbol):
    for cell in number.get_cells():
        if cell in coords_touched_by_symbol:
            return number.value
    return 0

def day_3(lines):
    symbol_coords = set()
    for line_index in range(len(lines)):
        line = re.sub("[^0-9\.\n]", SYMBOL, lines[line_index])
        for column_index in range(len(line)):
            if line[column_index] != SYMBOL:
                continue
            for adjacent_coord in AdjacentCellsCalculator.calculate(column_index, line_index):
                symbol_coords.add(adjacent_coord)

    numbers = NumbersFinder().find(lines)
 
    total_sum = sum([calculate_value_for_number(number, symbol_coords) for number in numbers])
    print(total_sum)


if __name__ == "__main__":
    input = open("day-3/res/input.txt", "r")
    lines = [line for line in input]
    day_3(lines)