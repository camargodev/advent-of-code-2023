from src.part_1.loop_distance_calculator import LoopDistanceCalculator
from src.part_2.loop_inner_size_calculator import LoopInnerSizeCalculator

if __name__ == "__main__":
    lines = [line for line in open("day_10/res/input.txt", "r")]
    print(LoopDistanceCalculator().calculate(lines))
    print(LoopInnerSizeCalculator().calculate(lines))