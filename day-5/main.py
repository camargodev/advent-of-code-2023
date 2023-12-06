from src.part_2.location_finder import LowestLocationFinder

if __name__ == "__main__":
    lines = [line for line in open("day-5/res/input.txt", "r")]
    print(LowestLocationFinder().find(lines))