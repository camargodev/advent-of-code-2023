from src.commons.pipe_loop_finder import PipeLoopFinder
from src.commons.pipe_loop_finder import PIPE_TYPES
from src.commons.pipe_loop_finder import EMPTY

class LoopInnerSizeCalculator:
    def __init__(self):
        self.pipe_loop_finder = PipeLoopFinder()
    
    def calculate(self, lines):
        lines = [line.replace("\n", "") for line in lines]
        loop_nodes = self.pipe_loop_finder.find(lines)
        inner_part_size = 0
        for row_idx, row in enumerate(lines):
            row_str = ""
            for col_idx, col in enumerate(row):
                row_str += lines[row_idx][col_idx] if (row_idx, col_idx) in loop_nodes else " "
            print(row_str)
        total_inside_loop = 0
        for row_idx, row in enumerate(lines):
            inside_loop = 0
            for col_idx, col in enumerate(row):
                if not (row_idx, col_idx) in loop_nodes:
                    before_col = row[0:col_idx]
                    after_col = row[col_idx:len(row)]
                    num_of_pipes_before_col = self.count_pipes_before(row, row_idx, col_idx, loop_nodes)
                    num_of_pipes_after_col = self.count_pipes_after(row, row_idx, col_idx, loop_nodes)
                    if num_of_pipes_before_col == 0 or num_of_pipes_after_col == 0:
                        continue
                    # print(row_idx, col_idx, num_of_pipes_before_col, num_of_pipes_after_col)
                    if num_of_pipes_before_col%2 != 0 or num_of_pipes_after_col%2 != 0:
                        inside_loop += 1
            total_inside_loop += inside_loop
            print(inside_loop)
        print(total_inside_loop)

        for row_idx, row in enumerate(lines):
            first_pipe_index, last_pipe_index = self.calculate_boundaries(row)
            inner = False
            row_inner_part_size = 0
            pipe_count = 0
            for col_idx, col in enumerate(row):
                if (row_idx, col_idx) in loop_nodes:
                    inner = not inner
                    pipe_count += 1
                    continue
                if inner and (col_idx > first_pipe_index and col_idx < last_pipe_index):
                    row_inner_part_size += 1
            inner_part_size += row_inner_part_size
            # print(pipe_count, pipe_count % 2)

        # return inner_part_size

    def count_pipes_before(self, row, row_idx, max_col_idx, loop_nodes):
        pipes_before = 0
        for col_idx, col in enumerate(row):
            if col_idx >= max_col_idx:
                continue
            if (row_idx, col_idx) in loop_nodes:
                pipes_before +=1 
        return pipes_before
    
    def count_pipes_after(self, row, row_idx, min_col_idx, loop_nodes):
        pipes_after = 0
        for col_idx, col in enumerate(row):
            if col_idx <= min_col_idx:
                continue
            if (row_idx, col_idx) in loop_nodes:
                pipes_after +=1 
        return pipes_after
    
    def count_pipes(self, line):
        return len([True for col in line if col in PIPE_TYPES])
    
    def calculate_boundaries(self, line):
        first, last = None, None
        for col_idx, col in enumerate(line):
            if col not in PIPE_TYPES:
                continue
            if first == None:
                first = col_idx
            last = col_idx
        return first, last

