from src.commons.input_extractor import InputExtractor
from math import lcm

GOAL_SUFFIX = "Z"
START_SUFFIX = "A"

class PathInfo:
    def __init__(self, current):
        self.current = current
        self.path_until_first_end = [current]
        self.loop_path = []
        self.completed_loop = False

    def already_found_loop(self):
        return len(self.loop_path) > 0
    
    def process_next_step(self, next_step):
        reached_end = next_step.endswith(GOAL_SUFFIX)
        loop_already_found = self.already_found_loop()
        if not reached_end and not loop_already_found:
            self.path_until_first_end.append(next_step)
        elif reached_end and loop_already_found:
            self.completed_loop = True
        else:
            self.loop_path.append(next_step)

class MapNavigator:
    def __init__(self):
        self.input_extractor = InputExtractor()

    def count_steps_to_goal(self, lines):
        direction_manager, coordinate_manager = self.input_extractor.extract(lines)
        
        sources = coordinate_manager.coordinates.keys()
        paths = [PathInfo(source) for source in sources if source.endswith(START_SUFFIX)]
        
        all_paths_completed_a_loop = False
        while not all_paths_completed_a_loop:
            next_direction = direction_manager.next()
            all_paths_completed_a_loop = True
            for path_info in paths:
                if path_info.completed_loop == True:
                    continue
                all_paths_completed_a_loop = False
                next_step = coordinate_manager.coordinates[path_info.current][next_direction]
                path_info.process_next_step(next_step)
                path_info.current = next_step

        return lcm(*[len(path.loop_path) for path in paths])