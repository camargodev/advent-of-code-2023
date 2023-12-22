from src.commons.grid_coords_calculator import GridCoordsCalculator
from src.commons.minimal_heat_finder import MinimalHeatFinder

if __name__ == "__main__":
    grid = [[int(char) for char in line.replace("\n","")] for line in open("day-17/res/input.txt", "r")]
    start, end = GridCoordsCalculator.calculate_start_and_end(grid)
    minimal_heat_finder = MinimalHeatFinder(grid, start, end)
    print(minimal_heat_finder.find(min_steps=1, max_steps=3))
    print(minimal_heat_finder.find(min_steps=4, max_steps=10))