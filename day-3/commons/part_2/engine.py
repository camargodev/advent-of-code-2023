from commons.numbers_finder import NumbersFinder
from commons.part_2.gear import Gear

GEAR = '*'

class Engine:
    def run(self, lines):
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

        return sum([gear.get_product() for gear in gears])