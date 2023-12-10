from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class PipeLoopPolygonManager:
    def __init__(self, loop_nodes):
        self.loop_nodes = loop_nodes
        self.loop_node_set = None
        self.loop_polygon = None
        self.boundaries_by_row = dict()
        self.board_size = 0

    def is_inside_pipe_loop(self, row_idx, col_idx):
        if (row_idx, col_idx) in self.loop_node_set:
            return False
        return self.loop_polygon.contains(Point(row_idx, col_idx))

    def get_rows_with_pipes(self):
        return [row_idx for row_idx in range(self.board_size) if row_idx in self.boundaries_by_row]
    
    def get_column_range_with_pipes(self, row_idx):
        min_col, max_col = self.boundaries_by_row[row_idx]
        return range(min_col, max_col)

class PipeLoopPolygonManagerFactory:
    @staticmethod
    def create(lines, loop_nodes):
        def create_boundaries_by_row_dict(loop_node_set):
            boundaries_by_row = dict()
            for pipe in loop_node_set:
                row, col = pipe
                if row not in boundaries_by_row:
                    boundaries_by_row[row] = col, col
                    continue
                min_col, max_col = boundaries_by_row[row]
                boundaries_by_row[row] = min(min_col, col), max(max_col, col)
            return boundaries_by_row

        pipe_polygon_manager = PipeLoopPolygonManager(loop_nodes)
        pipe_polygon_manager.loop_node_set = set(loop_nodes)
        pipe_polygon_manager.loop_polygon = Polygon(loop_nodes)
        pipe_polygon_manager.boundaries_by_row = create_boundaries_by_row_dict(pipe_polygon_manager.loop_node_set)
        pipe_polygon_manager.board_size = len(lines)
        return pipe_polygon_manager