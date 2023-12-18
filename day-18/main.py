from src.part_1.lava_area_calculator import LavaAreaCalculator as FirstLavaAreaCalculator
from src.part_2.lava_area_calculator import LavaAreaCalculator as SecondLavaAreaCalculator

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day-18/res/input.txt", "r")]
    print(FirstLavaAreaCalculator().calculate(lines))
    print(SecondLavaAreaCalculator().calculate(lines))