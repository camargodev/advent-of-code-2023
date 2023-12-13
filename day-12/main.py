from src.part_1.working_spring_counter import WorkingSpringCounter

if __name__ == "__main__":
    lines = [line for line in open("day-12/res/input.txt", "r")]
    print(WorkingSpringCounter().count(lines))