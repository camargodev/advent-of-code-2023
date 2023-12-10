NORTH = "NORTH"
SOUTH = "SOUTH"
WEST = "WEST"
EAST = "EAST"

SOURCE = "S"
EMPTY = "."

PIPE_TYPES = {"-", "|", "F", "7", "J", "L"}

PIPE_DIRECTIONS = {
    "-": {EAST, WEST},
    "|": {NORTH, SOUTH},
    "F": {SOUTH, EAST},
    "7": {SOUTH, WEST},
    "J": {NORTH, WEST},
    "L": {NORTH, EAST}
}

class PipeLoopFinder:
    def find(self, lines):
        source_location = self.find_source(lines)
        current_location, last_direction = self.get_starter_after_source(lines, source_location)
        loop_nodes = {source_location, current_location}
        while current_location != source_location:
            row_idx, col_idx = current_location
            current_pipe = lines[row_idx][col_idx]
            next_pipe_location, last_direction = self.find_next_pipe(current_pipe, current_location, last_direction)
            loop_nodes.add(next_pipe_location)
            current_location = next_pipe_location
        return loop_nodes

    def get_starter_after_source(self, lines, source_location):
        source_row_idx, source_col_idx = source_location
        adjacents = [(source_row_idx-1,source_col_idx,SOUTH), 
                     (source_row_idx+1,source_col_idx,NORTH), 
                     (source_row_idx,source_col_idx-1,EAST), 
                     (source_row_idx,source_col_idx+1,WEST)]
        for adjacent in adjacents:
            row_idx, col_idx, source_position_to_next = adjacent
            next_location = lines[row_idx][col_idx]
            if next_location != EMPTY and source_position_to_next in PIPE_DIRECTIONS[next_location]:
                return (row_idx, col_idx), source_position_to_next

    def find_source(self, lines):
        for row_idx, row in enumerate(lines):
            for col_idx, cell in enumerate(row):
                if cell == SOURCE:
                    return (row_idx, col_idx)
                
    def find_next_pipe(self, current_pipe, current_pipe_location, last_pipe_direction):
        [next_direction] = PIPE_DIRECTIONS[current_pipe] - {last_pipe_direction}
        return self.calculate_next_pipe_index_based_on_direction(current_pipe_location, next_direction)

    def calculate_next_pipe_index_based_on_direction(self, current_pipe, direction):
        row_idx, col_idx = current_pipe
        if direction == NORTH:
            return (row_idx-1, col_idx), SOUTH
        if direction == SOUTH:
            return (row_idx+1, col_idx), NORTH
        if direction == WEST:
            return (row_idx, col_idx-1), EAST
        if direction == EAST:
            return (row_idx, col_idx+1), WEST

