from src.part_1.energized_tiles_counter import EnergizedTilesCounter as FirstEnergizedTilesCounter
from src.part_2.energized_tiles_counter import EnergizedTilesCounter as SecondEnergizedTilesCounter

if __name__ == "__main__":
     line = [line.replace("\n","") for line in open("day-16/res/input.txt", "r")]
     print(FirstEnergizedTilesCounter().count(line))
     print(SecondEnergizedTilesCounter().count(line))