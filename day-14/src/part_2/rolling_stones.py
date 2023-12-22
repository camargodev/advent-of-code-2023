import copy
from functools import cache

CUBE_STONE = "#"
ROLLING_STONE = "O"
SPACE = "."

NUM_LOOPS = 1000000000

class GridTransposer:
     @staticmethod
     def transpose(grid):
        def clear_grid(grid):
             return [line.replace("\n", "") for line in grid]

        grid = clear_grid(grid)
        num_transposed_rows = len(grid[0])
        transposed_grid = ["" for _ in range(num_transposed_rows)]
        for line in grid:
            for char_idx, char in enumerate(line):
                transposed_grid[char_idx] += char
        return transposed_grid

class RollingStone:
    def move_like_jeager(self, lines):
        stones = [[char for char in line] for line in lines]
        stone_states = dict()

        stones_order = 1
        loop_start = None
        for _ in range(NUM_LOOPS):
            stones = self.full_rotation(stones)
            stone_tuple = []
            for line in stones:
                stone_tuple.append(tuple(line))
            if tuple(stone_tuple) in stone_states:
                loop_start, _ = stone_states[tuple(stone_tuple)]
                break
            stone_states[tuple(stone_tuple)] = (stones_order, self.calculate_total(stones))
            stones_order += 1

        loop_end = stones_order

        solution_index = loop_start+((NUM_LOOPS-loop_start) % (loop_end-loop_start))
        for stone_order, stone_total in stone_states.values():
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

