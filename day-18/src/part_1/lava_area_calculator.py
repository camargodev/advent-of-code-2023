import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

LEFT="L"
RIGHT="R"
UP="U"
DOWN="D"

BORDER = "-"
CORNER = "X"

class LavaAreaCalculator:
    def calculate(self, lines):
        instructions = self.extract_instructions(lines)
        borders = self.trace_area_borders(instructions)
        min_x, max_x, min_y, max_y = self.get_boundaries(borders)

        polygon = Polygon(borders)

        count = 0
        for x in range(min_x, max_x+1):
            # line = ""
            for y in range(min_y, max_y+1):
                is_part_of_polygon = (x,y) in borders or polygon.contains(Point(x, y))
                if is_part_of_polygon:
                    # line += "X"
                    count += 1
                # else:
                #     line += "."
            # print(line)

        # shape = borders
        
        # for i in range(min_x, max_x+1):
        #     line = ""
        #     for j in range(min_y, max_y+1):
        #         if (i,j) in borders:
        #             line += "X"
        #         else:
        #             line += "."
        return count

    def trace_area_borders(self, instructions):
        current_x = 0
        current_y = 0
        borders =[(current_x, current_y)]
        for direction, steps in instructions:
            for i in range(steps):
                if direction == LEFT:
                    current_y -= 1
                if direction == RIGHT:
                    current_y += 1
                if direction == UP:
                    current_x -= 1
                if direction == DOWN:
                    current_x += 1
                borders.append((current_x, current_y))
        return borders
    
    def get_boundaries(self, borders):
        min_x, min_y = math.inf, math.inf
        max_x, max_y = 0, 0
        for x, y in borders:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        return min_x, max_x, min_y, max_y

    def extract_instructions(self, lines):
        instructions = []
        for line in lines:
            direction, steps, _ = line.split(" ")
            instructions.append((direction, int(steps)))
        return instructions