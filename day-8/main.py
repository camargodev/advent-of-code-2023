from src.part_1.map_navigator import MapNavigator as FirstMapNavigator

if __name__ == "__main__":
    lines = [line for line in open("day-8/res/input.txt", "r")]
    print(FirstMapNavigator().count_steps_to_goal(lines))