from src.part_1.map_navigator import MapNavigator as FirstMapNavigator
from src.part_2.map_navigator import MapNavigator as SecondMapNavigator

if __name__ == "__main__":
    lines = [line for line in open("day_8/res/input.txt", "r")]
    print(FirstMapNavigator().count_steps_to_goal(lines))
    print(SecondMapNavigator().count_steps_to_goal(lines))