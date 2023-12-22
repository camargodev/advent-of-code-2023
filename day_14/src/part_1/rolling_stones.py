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
        max_possible_points = len(lines)
        stones = GridTransposer.transpose(lines)

        total = 0
        for stone_line in stones:
            line_total = 0
            current_max_points = max_possible_points
            for stone_idx, stone in enumerate(stone_line):
                if stone == SPACE:
                    continue
                if stone == ROLLING_STONE:
                    line_total += current_max_points
                elif stone == CUBE_STONE:
                    current_max_points = (max_possible_points - stone_idx)
                current_max_points -= 1
            total += line_total
        return total
