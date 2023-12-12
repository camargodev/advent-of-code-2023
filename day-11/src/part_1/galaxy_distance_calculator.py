GALAXY = "#"
EMPTY = "."

class Galaxy:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class GalaxyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def calculate_distance(self, empty_rows, empty_cols, empty_space_multiplier):
        return self.calculate_base_distance() + self.calculate_empty_distance(empty_rows, empty_cols, empty_space_multiplier)

    def calculate_base_distance(self):
        return abs(self.first.row - self.second.row) + abs(self.first.col - self.second.col)
    
    def calculate_empty_distance(self, empty_rows, empty_cols, empty_space_multiplier):
        min_x, max_x = min(self.first.row, self.second.row), max(self.first.row, self.second.row)
        min_y, max_y = min(self.first.col, self.second.col), max(self.first.col, self.second.col)
        empty_rows_count = [row for row in range(min_x, max_x) if row in empty_rows]
        empty_cols_count = [row for row in range(min_y, max_y) if row in empty_cols]
        return (empty_space_multiplier-1)*len(empty_rows_count) + (empty_space_multiplier-1)*len(empty_cols_count)

class UniverseSizeCalculator:
    @staticmethod
    def calculate(lines):
        return len(lines), len(lines[0])

class Universe:
    def __init__(self):
        self.galaxies = []
        self.rows_with_galaxies = set()
        self.cols_with_galaxies = set()

    def add_galaxy_at_location(self, row, col):
        self.galaxies.append(Galaxy(row, col))
        self.rows_with_galaxies.add(row)
        self.cols_with_galaxies.add(col)

    def calculate_total_galaxy_distance(self, universe_size, empty_space_multiplier):
        num_rows, num_cols = universe_size
        empty_rows = set([idx for idx in range(num_rows)]) - self.rows_with_galaxies
        empty_cols = set([idx for idx in range(num_cols)]) - self.cols_with_galaxies
        return sum([galaxy_pair.calculate_distance(empty_rows, empty_cols, empty_space_multiplier) for galaxy_pair in self.get_galaxy_pairs()])

    def get_galaxy_pairs(self):
        pairs = []
        for galaxy_idx, galaxy in enumerate(self.galaxies): 
            for other_galaxy in self.galaxies[galaxy_idx+1:]:
                pairs.append(GalaxyPair(galaxy, other_galaxy))
        return pairs

class GalaxyDistanceCalculator:
    def calculate(self, lines, empty_space_multiplier):
        universe = Universe()
        universe_size = UniverseSizeCalculator.calculate(lines)
        for row_idx, row in enumerate(lines):
            for col_idx, cell in enumerate(row):
                if cell == GALAXY:
                    universe.add_galaxy_at_location(row_idx, col_idx)

        return universe.calculate_total_galaxy_distance(universe_size, empty_space_multiplier)