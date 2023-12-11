GALAXY = "#"
EMPTY = "."

class GalaxyDistanceCalculator:
    def calculate(self, lines):
        galaxies = []
        rows_with_galaxies = set()
        cols_with_galaxies = set()
        for row_idx, row in enumerate(lines):
            for col_idx, cell in enumerate(row):
                if cell == GALAXY:
                    galaxies.append((row_idx, col_idx))
                    rows_with_galaxies.add(row_idx)
                    cols_with_galaxies.add(col_idx)
        
        empty_rows = set([idx for idx in range(len(lines))]) - rows_with_galaxies
        empty_cols = set([idx for idx in range(len(lines[0]))]) - cols_with_galaxies

        total_distance = 0 
        for galaxy_idx, galaxy in enumerate(galaxies):
            for other_galaxy_idx, other_galaxy in enumerate(galaxies[galaxy_idx+1:]):
                galaxy_x, galaxy_y = galaxy
                other_galaxy_x, other_galaxy_y = other_galaxy
                min_x, max_x = min(galaxy_x, other_galaxy_x), max(galaxy_x, other_galaxy_x)
                min_y, max_y = min(galaxy_y, other_galaxy_y), max(galaxy_y, other_galaxy_y)
                empty_rows_count = [row for row in range(min_x, max_x) if row in empty_rows]
                empty_cols_count = [row for row in range(min_y, max_y) if row in empty_cols]
                distance = (max_x - min_x + len(empty_rows_count)) + (max_y - min_y + len(empty_cols_count))
                total_distance += distance
                # print(galaxy, other_galaxy, distance)
        
        # print(galaxies, len(galaxies))
        # print(rows_with_galaxies, len(rows_with_galaxies))
        # print(cols_with_galaxies, len(cols_with_galaxies))
        # pass
        return total_distance