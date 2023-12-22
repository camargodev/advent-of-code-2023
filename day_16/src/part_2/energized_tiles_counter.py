from src.commons.energized_path_finder import *
from src.commons.tile import Tile

class EnergizedTilesCounter:
    def __init__(self):
        self.path_finder = EnergizedPathFinder()

    def count(self, grid):
        starts = self.get_all_possible_starts(grid)
        return max([len(self.path_finder.find(grid, start)) for start in starts])
    
    def get_all_possible_starts(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        starts = []
        for row in range(num_rows):
            starts.append(Tile(RIGHT, row, 0))
            starts.append(Tile(LEFT, row, num_cols-1))
        for col in range(num_cols):
            starts.append(Tile(DOWN, 0, col))
            starts.append(Tile(UP, num_rows-1, col))
        return starts