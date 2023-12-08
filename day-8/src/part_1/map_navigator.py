import re
LEFT = "L"
RIGHT = "R"
GOAL = "ZZZ"
START = "AAA"

class DirectionManager:
    def __init__(self, directions):
        self.directions = directions
        self.current = 0
    
    def next(self):
        instruction = self.directions[self.current]
        self.current = (self.current + 1) % len(self.directions)
        return instruction

class CoordinateManager:
    def __init__(self):
        self.coordinates = dict()

    def add_coordinate(self, source, left, right):
        target_map = {LEFT: left, RIGHT: right}
        self.coordinates[source] = target_map

class InputExtractor:
    def extract(self, lines):
        direction_manager = DirectionManager(lines[0].replace("\n", ""))
        coordinate_manager = CoordinateManager()
        for line in lines[2:]:
            found = re.search('(.+?) = \((.+?), (.+?)\)', line)
            source, left, right = found.group(1), found.group(2), found.group(3)
            coordinate_manager.add_coordinate(source, left, right)
        return direction_manager, coordinate_manager

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