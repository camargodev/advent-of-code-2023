from src.commons.working_spring_counter import WorkingSpringCounter
from src.commons.input_extractor import InputExtractor



if __name__ == "__main__":
    lines = [line for line in open("day-12/res/input.txt", "r")]
    input_extractor = InputExtractor()
    print(WorkingSpringCounter().count(input_extractor.extract(lines)))
    print(WorkingSpringCounter().count(input_extractor.extract_with_repetition(lines, 4)))