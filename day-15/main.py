from src.part_1.hash_calculator import HashCalculator as FirstHashCalculator
from src.part_2.hash_calculator import HashCalculator as SecondHashCalculator

if __name__ == "__main__":
    lines = [line for line in open("day-15/res/input.txt", "r")]
    # print(FirstHashCalculator().calculate(lines[0]))
    print(SecondHashCalculator().calculate(lines[0]))
