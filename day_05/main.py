from src.part_1.location_finder import LowestLocationFinder as FirstLowestLocationFinder
from src.part_2.location_finder import LowestLocationFinder as SecondLowestLocationFinder

if __name__ == "__main__":
    lines = [line for line in open("day_5/res/input.txt", "r")]
    print(FirstLowestLocationFinder().find(lines))
    print(SecondLowestLocationFinder().find(lines))