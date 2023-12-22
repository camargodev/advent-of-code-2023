from src.part_1.rolling_stones import RollingStone as Rolling
from src.part_2.rolling_stones import RollingStone as Stone

if __name__ == "__main__":
     lines = [line.replace("\n", "") for line in open("day-14/res/input.txt", "r")]
     print(Rolling().move_like_jeager(lines))
     print(Stone().move_like_jeager(lines))