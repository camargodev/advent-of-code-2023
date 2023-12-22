from src.commons.energized_path_finder import EnergizedPathFinder
from src.commons.energized_path_finder import RIGHT
from src.commons.tile import Tile

class EnergizedTilesCounter:
    def __init__(self):
        self.path_finder = EnergizedPathFinder()
        
    def count(self, grid):
        energized_path = self.path_finder.find(grid, Tile(RIGHT, 0, 0))
        return len(energized_path)