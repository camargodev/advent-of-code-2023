import re

GEAR = '*'
DIGITS = [str(num) for num in range(10)]

class Gear:
    def __init__(self):
        self.numbers = []
    
    def get_product(self):
        if len(self.numbers) == 2:
            return self.numbers[0] * self.numbers[1]
        return 0

class Number:
    def __init__(self, column, line_start, line_end, value):
        self.column = column
        self.line_start = line_start
        self.line_end = line_end
        self.value = value

    def is_touched_by_gear(self, column, line):
        gear_adjacents = self.get_adjacent_cells(line, column)
        for line_index in range(self.line_start, self.line_end):
            if (self.column, line_index) in gear_adjacents:
                return True
        return False

    def get_adjacent_cells(self, line, column):
        left = column-1
        right = column+1
        up = line-1
        down = line+1
        return [(up,left),   (up,column),   (up,right),
                (line,left),                (line,right),
                (down,left), (down,column), (down,right)]

def day_3(lines):
    gear_by_coords = dict()
    for line_index in range(len(lines)):
        line = lines[line_index]
        for column_index in range(len(line)):
            if line[column_index] != GEAR:
                continue
            gear_by_coords[(line_index, column_index)] = Gear()

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
 
    for number in numbers:
        print("NUMBER", number.value, "AT", number.column, "IN CELLS(", number.line_start, number.line_end, ")")

    for coord, gear in gear_by_coords.items():
        line, column = coord
        print("GEAR AT", line, column, "REF:", gear)
        for number in numbers:
            if number.is_touched_by_gear(column, line):
                print("NUMBER", number.value, "IS TOUCHED BY GEAR")
                gear.numbers.append(number.value)
                print("NUMBER", number.value, "IS TOUCHED BY GEAR WITH NUMBERS", gear.numbers)

    total_sum = 0
    for _, gear in gear_by_coords.items():
        print("GEAR WITH NUMBERS", gear.numbers, "REF", gear)
        total_sum += gear.get_product()
    print(total_sum)


if __name__ == "__main__":
    input = open("day-3/input.txt", "r")
    lines = [line for line in input]
    day_3(lines)