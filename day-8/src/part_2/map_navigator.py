import re
from math import lcm

LEFT = "L"
RIGHT = "R"

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

class PathInfo:
    def __init__(self, current):
        self.current = current
        self.path_until_first_end = [current]
        self.loop_path = []
        self.completed_loop = False

    def already_found_loop(self):
        return len(self.loop_path) > 0

class MapNavigator:
    def __init__(self):
        self.input_extractor = InputExtractor()

    def count_steps_to_goal(self, lines):
        direction_manager, coordinate_manager = self.input_extractor.extract(lines)
        
        paths = [PathInfo(start) for start in self.extract_starts(coordinate_manager)]
        
        all_paths_arrived_at_goal = False
        while not all_paths_arrived_at_goal:
            next_direction = direction_manager.next()
            all_paths_arrived_at_goal = True
            for path_info in paths:
                if path_info.completed_loop == True:
                    continue
                all_paths_arrived_at_goal = False
                current = path_info.current
                next_step = coordinate_manager.coordinates[current][next_direction]

                if not self.is_end(next_step):
                    if not path_info.already_found_loop():
                        path_info.path_until_first_end.append(next_step)
                    else:
                        path_info.loop_path.append(next_step)
                else:
                    if not path_info.already_found_loop():
                        path_info.loop_path.append(next_step)
                    else:
                        path_info.completed_loop = True
                path_info.current = next_step

        return lcm(*[len(path.loop_path) for path in paths])
    
    def extract_starts(self, coordinate_manager):
        starts = []
        for source in coordinate_manager.coordinates.keys():
            if source[-1] == "A":
                starts.append(source)
        return starts
    
    def arrived_at_goal(self, current_steps):
        for current in current_steps:
            if current[-1] != "Z":
                return False
        return True
    
    def is_end(self, step):
        return step[-1] == "Z"