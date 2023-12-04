import re
#551094
class Number:
    def __init__(self, id, value):
        self.id = id
        self.value = value

def find_number_by_index(line, line_index, regex):
    substrings_by_index = dict()
    standard_line = "."+line
    for substring in re.findall(regex, standard_line):
        pattern = '(?=[^0-9]'+substring+'[^0-9])'                   
        for index in [match.start() for match in re.finditer(pattern, standard_line)]:
            substrings_by_index[index] = substring
    return substrings_by_index

def find_symbol_by_index(line, regex):
    substrings_by_index = dict()
    for substring in re.findall(regex, line):
        for index in [match.start() for match in re.finditer(substring, line)]:
            substrings_by_index[index] = substring
    return substrings_by_index

def get_adjacent_cells(line, column):
    left = column-1
    right = column+1
    up = line-1
    down = line+1
    return [(up,left),   (up,column),   (up,right),
            (line,left),                (line,right),
            (down,left), (down,column), (down,right)]

def day_3(input):
    line_index = 0
    number_id = 1
    number_by_coords = dict()
    visited_ids = set()
    coords_touched_by_symbol = set()
    total_sum = 0
    for line in input:
        line = re.sub("[^0-9\.\n]", 'S', line)
        for column_index, _ in find_symbol_by_index(line, r'S').items():
            for coords in get_adjacent_cells(line_index, column_index):
                coords_touched_by_symbol.add(coords)
        for column_index, number in find_number_by_index(line, line_index, r'\d+').items():
            number_object = Number(number_id, int(number))
            for i in range(len(number)):
                number_by_coords[(line_index,column_index+i)] = number_object
            number_id += 1
        line_index += 1

    all_nums = []
    for coords in coords_touched_by_symbol:
        if coords not in number_by_coords:
            continue
        number = number_by_coords[coords]
        if number.id in visited_ids:
            continue
        all_nums.append(number.value)
        total_sum += number.value
        visited_ids.add(number.id)

    all_nums.sort()
    print(total_sum)



if __name__ == "__main__":
    input = open("day-3/input.txt", "r")
    day_3(input)