from src.part_1.hash_calculator import HashCalculator
from src.part_2.hashmap_calculator import HashMapCalculator

if __name__ == "__main__":
    line = [line for line in open("day_15/res/input.txt", "r")][0]
    print(HashCalculator().calculate(line))
    print(HashMapCalculator().calculate(line))
