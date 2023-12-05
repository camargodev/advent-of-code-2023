from commons.numbers_finder import NumbersFinder
from commons.part_2.gear import Gear

GEAR = '*'

class EngineManager:
    def run(self, lines):
        gears = self.find_gears(lines)
        numbers = NumbersFinder().find(lines)

        for gear in gears:
            for number in numbers:
                if gear.touches_number(number):
                    gear.numbers.append(number.value)

        return sum([gear.get_product() for gear in gears])
    
    def find_gears(self, lines):
        gears = set()
        for row_index, row in enumerate(lines):
            for column_index, cell in enumerate(row):
                if cell == GEAR:
                    gears.add(Gear(row_index, column_index))
        return gears
