from commons.numbers_finder import NumbersFinder
from commons.part_2.gear import Gear

GEAR = '*'
DIGITS = [str(num) for num in range(10)]

def day_3(lines):
    gears = set()
    for row_index in range(len(lines)):
        line = lines[row_index]
        for column_index in range(len(line)):
            if line[column_index] != GEAR:
                continue
            gears.add(Gear(row_index, column_index))

    numbers = NumbersFinder().find(lines)

    for gear in gears:
        for number in numbers:
            if gear.touches_number(number):
                gear.numbers.append(number.value)

    total_sum = sum([gear.get_product() for gear in gears])
    print(total_sum)


if __name__ == "__main__":
    input = open("day-3/res/input.txt", "r")
    lines = [line for line in input]
    day_3(lines)