from src.commons.pipe_loop_finder import PipeLoopFinder
from src.part_2.pype_loop_polygon_manager import PipeLoopPolygonManagerFactory

class LoopInnerSizeCalculator:
    def __init__(self):
        self.pipe_loop_finder = PipeLoopFinder()
    
    def calculate(self, lines):
        lines = [line.replace("\n", "") for line in lines]
        pipe_loop_nodes = self.pipe_loop_finder.find(lines)

        pipe_loop_manager = PipeLoopPolygonManagerFactory.create(lines, pipe_loop_nodes)

        pipe_loop_inner_size = 0
        for row_idx in pipe_loop_manager.get_rows_with_pipes():
            for col_idx in pipe_loop_manager.get_column_range_with_pipes(row_idx):
                if pipe_loop_manager.is_inside_pipe_loop(row_idx, col_idx):
                    pipe_loop_inner_size += 1
        return pipe_loop_inner_size