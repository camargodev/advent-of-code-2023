from src.part_1.hash_calculator import HashCalculator

if __name__ == "__main__":
    lines = [line for line in open("day-15/res/input.txt", "r")]
    print(HashCalculator().calculate(lines[0]))
