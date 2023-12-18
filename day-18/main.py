from src.part_1.lava_area_calculator import LavaAreaCalculator

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day-18/res/input.txt", "r")]
    print(LavaAreaCalculator().calculate(lines))