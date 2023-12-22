from src.commons.input_extractor import InputExtractor

GOAL = "ZZZ"
START = "AAA"

class MapNavigator:
    def __init__(self):
        self.input_extractor = InputExtractor()

    def count_steps_to_goal(self, lines):
        direction_manager, coordinate_manager = self.input_extractor.extract(lines)
        step_count = 0
        current = START
        while current != GOAL:
            current = coordinate_manager.coordinates[current][direction_manager.next()]
            step_count += 1
        return step_count