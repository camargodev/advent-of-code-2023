PALINDROME_NOT_FOUND = -1

class InputExtractor:
    def extract_grids(self, lines):
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


class MirrorFinder:
    def __init__(self):
        self.input_extractor = InputExtractor()

    def find(self, lines, allowed_diffences):
        grids = self.input_extractor.extract_grids(lines)
        total_grid_value = 0
        for grid_idx, grid in enumerate(grids):
            grid_value = self.find_mirror_by_column(grid, allowed_diffences)
            if grid_value != PALINDROME_NOT_FOUND:
                total_grid_value += grid_value
            transposed_grid = self.transpose_grid(grid)
            transposed_grid_value = self.find_mirror_by_column(transposed_grid, allowed_diffences)
            if transposed_grid_value != PALINDROME_NOT_FOUND:
                total_grid_value += 100 * transposed_grid_value
        return total_grid_value
    
    def find_mirror_by_column(self, grid, allowed_diffences):
        num_columns = len(grid[0])
        for col_idx in range(1, num_columns):
            if self.count_differences_when_slicing_at_column(grid, col_idx) == allowed_diffences:
                return col_idx
        return PALINDROME_NOT_FOUND
    
    def count_differences_when_slicing_at_column(self, grid, col_idx):
        differences_count = 0
        for idx, line in enumerate(grid):
            first_part = line[:col_idx]
            second_part = line[col_idx:]
            min_size = min(len(first_part), len(second_part))
            if len(first_part) < len(second_part):
                second_part = second_part[:min_size][::-1]
            elif len(first_part) > len(second_part):
                first_part = first_part[::-1][:min_size]
            differences_count += sum(1 for a, b in zip(first_part, second_part) if a != b)
            # if differences_count > 0:
            #     return differences_count
        return differences_count
    
    def transpose_grid(self, grid):
        num_transposed_rows = len(grid[0])
        transposed_grid = ["" for _ in range(num_transposed_rows)]
        for line in grid:
            for char_idx, char in enumerate(line):
                transposed_grid[char_idx] += char
        return transposed_grid