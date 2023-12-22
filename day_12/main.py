from src.commons.working_spring_counter import WorkingSpringCounter
from src.part_2.cached_working_spring_counter import CachedWorkingSpringCounter
from src.commons.input_extractor import InputExtractor

if __name__ == "__main__":
    lines = [line for line in open("day_12/res/input.txt", "r")]
    input_extractor = InputExtractor()
    print(WorkingSpringCounter().count(input_extractor.extract(lines)))
    print(CachedWorkingSpringCounter().count(input_extractor.extract_with_repetition(lines, 4)))