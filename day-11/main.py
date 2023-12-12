from src.part_1.galaxy_distance_calculator import GalaxyDistanceCalculator as FirstGalaxyDistanceCalculator
from src.part_2.galaxy_distance_calculator import GalaxyDistanceCalculator as SecondGalaxyDistanceCalculator

if __name__ == "__main__":
    lines = [line for line in open("day-11/res/input.txt", "r")]
    print(FirstGalaxyDistanceCalculator().calculate(lines, 2))
    print(FirstGalaxyDistanceCalculator().calculate(lines, 1000000))

