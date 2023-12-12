from src.commons.galaxy_distance_calculator import GalaxyDistanceCalculator

EACH_EMPTY_COUNTING_AS_2 = 2
EACH_EMPTY_COUNTING_AS_A_MILLION = 1000000

if __name__ == "__main__":
    lines = [line for line in open("day-11/res/input.txt", "r")]
    distance_calculator = GalaxyDistanceCalculator() 
    print(distance_calculator.calculate(lines, EACH_EMPTY_COUNTING_AS_2))
    print(distance_calculator.calculate(lines, EACH_EMPTY_COUNTING_AS_A_MILLION))

