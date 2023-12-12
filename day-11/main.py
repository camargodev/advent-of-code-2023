from src.commons.galaxy_distance_calculator import GalaxyDistanceCalculator

if __name__ == "__main__":
    lines = [line for line in open("day-11/res/input.txt", "r")]
    distance_calculator = GalaxyDistanceCalculator() 
    print(distance_calculator.calculate(lines, 2))
    print(distance_calculator.calculate(lines, 1000000))

