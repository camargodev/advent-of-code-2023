import copy
from functools import cache

CUBE_STONE = "#"
ROLLING_STONE = "O"
SPACE = "."



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
        stones = [tuple([char for char in line]) for line in lines]
        
        for _ in range(10000000):
            stones = self.full_rotation(tuple(stones))

        total = 0
        max_points = len(stones)
        for line_idx, shifted_stone_line in enumerate(stones):
            numbers_of_rolling_stones = shifted_stone_line.count(ROLLING_STONE)
            line_points = max_points - line_idx
            total += numbers_of_rolling_stones * line_points
        return total
    
    @cache
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

