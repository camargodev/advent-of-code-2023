from src.commons.universe import Universe

GALAXY = "#"

class GalaxyDistanceCalculator:
    def calculate(self, lines, empty_space_multiplier):
        universe = Universe.create(lines)
        for row_idx, row in enumerate(lines):
            for col_idx, cell in enumerate(row):
                if cell == GALAXY:
                    universe.add_galaxy_at_location(row_idx, col_idx)

        return universe.calculate_total_galaxy_distance(empty_space_multiplier)