import math

LEFT="L"
RIGHT="R"
UP="U"
DOWN="D"

BORDER = "-"
CORNER = "X"

class LavaAreaCalculator:
    def __init__(self, instructions_extractor):
        self.instructions_extractor = instructions_extractor

    def calculate(self, lines):
        instructions = self.instructions_extractor.extract(lines)
        corners, perimeter = self.trace_area_borders(instructions)

        total_area = 0
        for i in range(len(corners)):
            x_a, y_a = corners[i]
            x_b, y_b = corners[(i + 1) % len(corners)] 
            total_area += (x_a * y_b - x_b * y_a)

        return abs(total_area)//2 + perimeter//2 + 1

    def trace_area_borders(self, instructions):
        current_x = 0
        current_y = 0
        corners =[(current_x, current_y)]
        perimeter = 0
        for direction, steps in instructions:
            if direction == LEFT:
                current_y -= steps
            if direction == RIGHT:
                current_y += steps
            if direction == UP:
                current_x -= steps
            if direction == DOWN:
                current_x += steps
            perimeter += steps
            corners.append((current_x, current_y))
        return corners, perimeter