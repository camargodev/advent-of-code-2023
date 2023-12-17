from src.part_1.energized_tiles_counter import EnergizedTilesCounter

if __name__ == "__main__":
     line = [line.replace("\n","") for line in open("day-16/res/input.txt", "r")]
     print(EnergizedTilesCounter().count(line))