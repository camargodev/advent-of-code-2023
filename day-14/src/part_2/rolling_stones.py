import copy
from functools import cache

CUBE_STONE = "#"
ROLLING_STONE = "O"
SPACE = "."

NUM_LOOPS = 1000000000

class StoneLoopDetector:
    def __init__(self):
        self.stones_order = 1
        self.loop_start = None
        self.stone_states = dict()

    def is_loop_detected(self, stones):
        stones_tuple = self.to_tuple(stones)
        if stones_tuple in self.stone_states:
            self.loop_start, _ = self.stone_states[stones_tuple]
            return True
        self.stone_states[stones_tuple] = (self.stones_order, self.calculate_total(stones))
        self.stones_order += 1
        return False
    
    def calculate_total_after_iterations(self, iterations):
        loop_end = self.stones_order
        loop_size = (loop_end-self.loop_start)

        solution_index = self.loop_start + ((iterations-self.loop_start) % loop_size)
        for stone_order, stone_total in self.stone_states.values():
            if stone_order == solution_index:
                return stone_total
        return None

    def calculate_total(self, stones):
        total = 0
        max_points = len(stones)
        for line_idx, shifted_stone_line in enumerate(stones):
            numbers_of_rolling_stones = shifted_stone_line.count(ROLLING_STONE)
            line_points = max_points - line_idx
            total += numbers_of_rolling_stones * line_points
        return total


    def to_tuple(self, stones):
        stone_tuple = []
        for line in stones:
            stone_tuple.append(tuple(line))
        return tuple(stone_tuple)



class RollingStone:
    def move_like_jeager(self, lines):
        stones = [[char for char in line] for line in lines]
        loop_detector = StoneLoopDetector()

        while not loop_detector.is_loop_detected(stones):
            stones = self.full_rotation(stones)

        return loop_detector.calculate_total_after_iterations(NUM_LOOPS)

    
    def full_rotation(self, stones):
        stones = list(stones)
        shifted_stones = self.shift_to_north(stones)
        shifted_stones = self.shift_to_west(shifted_stones)
        shifted_stones = self.shift_to_south(shifted_stones)
        shifted_stones = self.shift_to_east(shifted_stones)
        return shifted_stones
    
    def shift_to_west(self, stones):
        shifted_stones = []
        for stone_line_idx in range(len(stones)):
            shifted_parts = []
            str_stone_line = "".join(list(stones[stone_line_idx]))
            for part in str_stone_line.split(CUBE_STONE):
                grouped_stones = part.replace(SPACE, "")
                empty_size = len(part) - len(grouped_stones)
                shifted_parts.append(grouped_stones + (SPACE * empty_size))
            str_shifted_line = CUBE_STONE.join(shifted_parts)
            shifted_line = [char for char in str_shifted_line]
            shifted_stones.append(shifted_line)

        return shifted_stones
    
    def shift_to_east(self, stones):
        shifted_stones = []
        for stone_line_idx in range(len(stones)):
            shifted_parts = []
            str_stone_line = "".join(stones[stone_line_idx])
            for part in str_stone_line.split(CUBE_STONE):
                grouped_stones = part.replace(SPACE, "")
                empty_size = len(part) - len(grouped_stones)
                shifted_parts.append((SPACE * empty_size) + grouped_stones)
            str_shifted_line = CUBE_STONE.join(shifted_parts)
            shifted_line = [char for char in str_shifted_line]
            shifted_stones.append(shifted_line)

        return shifted_stones
    
    def shift_to_north(self, stones):
        shifted_stones = list(stones)
        for stone_col_idx in range(len(stones[0])):
            str_stone_col = "".join([stones[row_idx][stone_col_idx] for row_idx in range(len(stones))])
            shifted_parts = []
            for part in str_stone_col.split(CUBE_STONE):
                grouped_stones = part.replace(SPACE, "")
                empty_size = len(part) - len(grouped_stones)
                shifted_parts.append(grouped_stones + (SPACE * empty_size))
            str_shifted_col = CUBE_STONE.join(shifted_parts)
            for row_idx in range(len(stones)):
                shifted_stones[row_idx][stone_col_idx] = str_shifted_col[row_idx]
        return shifted_stones
    
    def shift_to_south(self, stones):
        shifted_stones = stones
        for stone_col_idx in range(len(stones[0])):
            str_stone_col = "".join([stones[row_idx][stone_col_idx] for row_idx in range(len(stones))])
            shifted_parts = []
            for part in str_stone_col.split(CUBE_STONE):
                grouped_stones = part.replace(SPACE, "")
                empty_size = len(part) - len(grouped_stones)
                shifted_parts.append((SPACE * empty_size) + grouped_stones)
            str_shifted_col = CUBE_STONE.join(shifted_parts)
            for row_idx in range(len(stones)):
                shifted_stones[row_idx][stone_col_idx] = str_shifted_col[row_idx]

        return shifted_stones
    
    
    def print_stones(self, stones):
        for stone_line in stones:
            print(stone_line)
        print()

