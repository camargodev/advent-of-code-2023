from src.part_1.galaxy_distance_calculator import GalaxyDistanceCalculator

if __name__ == "__main__":
    lines = [line for line in open("day-11/res/input.txt", "r")]
    print(GalaxyDistanceCalculator().calculate(lines))

