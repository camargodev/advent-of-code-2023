from src.part_1.rolling_stones import RollingStone

if __name__ == "__main__":
     lines = [line for line in open("day-14/res/input.txt", "r")]
     print(RollingStone().move_like_jeager(lines))