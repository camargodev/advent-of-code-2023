class GridCoordsCalculator:
    @staticmethod
    def calculate_start_and_end(grid):
        return (0, 0), (len(grid)-1, len(grid[0])-1)