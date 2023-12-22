from src.part_1.cube_game_player import CubeGamePlayer as FirstCubeGamePlayer
from src.part_2.cube_game_player import CubeGamePlayer as SecondCubeGamePlayer

if __name__ == "__main__":
    lines = [line for line in open("day_2/res/input.txt", "r")]
    print(FirstCubeGamePlayer().play(lines))
    print(SecondCubeGamePlayer().play(lines))