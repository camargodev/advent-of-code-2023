PALINDROME_NOT_FOUND = 0
TRANSPOSED_GRID_RATIO = 100

class InputGridExtractor:
    @staticmethod
    def extract(lines):
        grids = []
        current_grid = []
        for raw_line in lines:
            line = raw_line.replace("\n", "")
            if line == "":
                grids.append(current_grid)
                current_grid = []
                continue
            current_grid.append(line)
        grids.append(current_grid)
        return grids
    
class GridTransposer:
    @staticmethod
    def transpose(grid):
        num_transposed_rows = len(grid[0])
        transposed_grid = ["" for _ in range(num_transposed_rows)]
        for line in grid:
            for char_idx, char in enumerate(line):
                transposed_grid[char_idx] += char
        return transposed_grid

class MirrorFinder:
    def find(self, lines, allowed_diffences):
        grids = InputGridExtractor.extract(lines)
        return sum([self.calculate_grid_value(grid, allowed_diffences) for grid in grids])
    
    def calculate_grid_value(self, grid, allowed_diffences):
        grid_value = self.find_mirror_index(grid, allowed_diffences)
        transposed_grid_value = self.find_mirror_index(GridTransposer.transpose(grid), allowed_diffences)
        return grid_value + (TRANSPOSED_GRID_RATIO * transposed_grid_value)
    
    def find_mirror_index(self, grid, allowed_diffences):
        num_columns = len(grid[0])
        for col_idx in range(1, num_columns):
            if self.count_differences_when_slicing_at_column(grid, col_idx) == allowed_diffences:
                return col_idx
        return PALINDROME_NOT_FOUND
    
    def count_differences_when_slicing_at_column(self, grid, col_idx):
        differences_count = 0
        for line in grid:
            first_part = line[:col_idx]
            second_part = line[col_idx:]
            min_size = min(len(first_part), len(second_part))
            if len(first_part) < len(second_part):
                second_part = second_part[:min_size][::-1]
            elif len(first_part) > len(second_part):
                first_part = first_part[::-1][:min_size]
            differences_count += sum(1 for a, b in zip(first_part, second_part) if a != b)
        return differences_count
    
