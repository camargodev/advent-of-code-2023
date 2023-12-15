PALINDROME_NOT_FOUND = -1

class InputExtractor:
    def extract_grids(self, lines):
        grids = []
        current_grid = []
        for raw_line in lines:
            line = [char for char in raw_line.replace("\n", "")]
            if line == "":
                grids.extend(self.create_all_possible_grids(current_grid))
                current_grid = []
                continue
            current_grid.append(line)
        grids.extend(self.create_all_possible_grids(current_grid))
        return grids
    
    def create_all_possible_grids(self, grid):
        all_grids = []
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[row_idx])):
                value = grid[row_idx][col_idx]
                updated_value = "#" if value == "." else "."
                grid[row_idx][col_idx] = updated_value
                all_grids.append(grid)
                print(grid)
                grid[row_idx][col_idx] = value
        return all_grids

class MirrorFinder:
    def __init__(self):
        self.input_extractor = InputExtractor()

    def find(self, lines):
        grids = self.input_extractor.extract_grids(lines)
        total_grid_value = 0
        for grid_idx, grid in enumerate(grids):
            grid_value = self.find_mirror_by_column(grid)
            if grid_value != PALINDROME_NOT_FOUND:
                total_grid_value += grid_value
            transposed_grid = self.transpose_grid(grid)
            transposed_grid_value = self.find_mirror_by_column(transposed_grid)
            if transposed_grid_value != PALINDROME_NOT_FOUND:
                total_grid_value += 100 * transposed_grid_value
            # print(grid_idx, grid_value, transposed_grid_value)
        return total_grid_value
    
    def find_mirror_by_column(self, grid):
        num_columns = len(grid[0])
        for col_idx in range(1, num_columns):
            if self.is_palindrome_when_slicing_at_column(grid, col_idx):
                return col_idx
        return PALINDROME_NOT_FOUND
    
    def is_palindrome_when_slicing_at_column(self, grid, col_idx):
        for idx, line in enumerate(grid):
            first_part = line[:col_idx]
            second_part = line[col_idx:]
            min_size = min(len(first_part), len(second_part))
            if len(first_part) < len(second_part):
                second_part = second_part[:min_size][::-1]
            elif len(first_part) > len(second_part):
                first_part = first_part[::-1][:min_size]
            if first_part != second_part:
                return False
        return True
    
    def transpose_grid(self, grid):
        num_transposed_rows = len(grid[0])
        transposed_grid = ["" for _ in range(num_transposed_rows)]
        for line in grid:
            for char_idx, char in enumerate(line):
                transposed_grid[char_idx] += char
        return transposed_grid