from src.part_1.working_spring_counter import WorkingSpringCounter as FirstWorkingSpringCounter
from src.part_2.working_spring_counter import WorkingSpringCounter as SecondWorkingSpringCounter

if __name__ == "__main__":
    lines = [line for line in open("day-12/res/input.txt", "r")]
    # print(FirstWorkingSpringCounter().count(lines))
    print(SecondWorkingSpringCounter().count(lines))