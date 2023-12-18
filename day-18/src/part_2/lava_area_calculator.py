import math

LEFT="L"
RIGHT="R"
UP="U"
DOWN="D"

BORDER = "-"
CORNER = "X"

DIRECTION = {0: "R", 1: "D", 2: "L", 3: "U"}

class LavaAreaCalculator:
    def calculate(self, lines):
        instructions = self.extract_instructions(lines)
        corners, perimeter = self.trace_area_borders(instructions)

        total_area = 0
        border_set = set()
        for i in range(len(corners)):
            x_a, y_a = corners[i]
            x_b, y_b = corners[(i + 1) % len(corners)] 
            total_area += (x_a * y_b - x_b * y_a)

        # print(abs(total_area)//2, len(borders)//2)
        return abs(total_area)//2 + perimeter//2 + 1

    def trace_area_borders(self, instructions):
        current_x = 0
        current_y = 0
        corners =[(current_x, current_y)]
        perimeter = 0
        for direction, steps in instructions:
            # for i in range(steps):
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

    def extract_instructions(self, lines):
        instructions = []
        for line in lines:
            _, _, hex_instruction = line.split(" ")
            instruction = hex_instruction.replace("(#", "").replace(")", "")
            hex_number, hex_dir = instruction[:-1], instruction[-1] 
            direction = DIRECTION[int(hex_dir)]
            steps = int(hex_number, 16)
            # print((direction, steps))
            instructions.append((direction, steps))
        return instructions