from src.commons.galaxy import Galaxy
from src.commons.galaxy import GalaxyPair

class UniverseSizeCalculator:
    @staticmethod
    def calculate(lines):
        return len(lines), len(lines[0])

class Universe:
    def __init__(self, universe_size):
        self.galaxies = []
        self.rows_with_galaxies = set()
        self.cols_with_galaxies = set()
        self.universe_size = universe_size

    @staticmethod
    def create(lines):
        universe_size = UniverseSizeCalculator.calculate(lines)
        return Universe(universe_size)

    def add_galaxy_at_location(self, row, col):
        self.galaxies.append(Galaxy(row, col))
        self.rows_with_galaxies.add(row)
        self.cols_with_galaxies.add(col)

    def calculate_total_galaxy_distance(self, empty_space_multiplier):
        num_rows, num_cols = self.universe_size
        empty_rows = set([idx for idx in range(num_rows)]) - self.rows_with_galaxies
        empty_cols = set([idx for idx in range(num_cols)]) - self.cols_with_galaxies
        return sum([galaxy_pair.calculate_distance(empty_rows, empty_cols, empty_space_multiplier) for galaxy_pair in self.get_galaxy_pairs()])

    def get_galaxy_pairs(self):
        pairs = []
        for galaxy_idx, galaxy in enumerate(self.galaxies): 
            for other_galaxy in self.galaxies[galaxy_idx+1:]:
                pairs.append(GalaxyPair(galaxy, other_galaxy))
        return pairs