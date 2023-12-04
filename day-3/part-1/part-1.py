import re

SYMBOL = 'S'
DIGITS = [str(num) for num in range(10)]

class Number:
    def __init__(self, column, line_start, line_end, value):
        self.column = column
        self.line_start = line_start
        self.line_end = line_end
        self.value = value

def get_adjacent_cells(line, column):
    left = column-1
    right = column+1
    up = line-1
    down = line+1
    return [(up,left),   (up,column),   (up,right),
            (line,left),                (line,right),
            (down,left), (down,column), (down,right)]

def day_3(lines):
    symbol_coords = set()
    for line_index in range(len(lines)):
        line = re.sub("[^0-9\.\n]", SYMBOL, lines[line_index])
        for column_index in range(len(line)):
            if line[column_index] != SYMBOL:
                continue
            for adjacent_coord in get_adjacent_cells(line_index, column_index):
                symbol_coords.add(adjacent_coord)

    numbers = []
    for line_index in range(len(lines)):
        line = lines[line_index]
        last_was_digit = False

        start = 0
        for column_index in range(len(line)):
            value = line[column_index]
            if value not in DIGITS:
                if last_was_digit == True:
                    end = column_index
                    numbers.append(Number(line_index, start, end, int(line[start:end])))
                last_was_digit = False
                continue
            if last_was_digit == True:
                continue
            start = column_index
            last_was_digit = True
 
    total_sum = 0
    for number in numbers:
        valid_number = False
        for line_index in range(number.line_start, number.line_end):
            if (number.column, line_index) in symbol_coords:
                valid_number = True
        if valid_number:
            total_sum += number.value
    print(total_sum)


if __name__ == "__main__":
    input = open("day-3/input.txt", "r")
    lines = [line for line in input]
    day_3(lines)