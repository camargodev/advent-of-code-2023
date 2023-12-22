from src.commons.pipe_loop_finder import PipeLoopFinder

class LoopDistanceCalculator:
    def __init__(self):
        self.pipe_loop_finder = PipeLoopFinder()
    
    def calculate(self, lines):
        loop_nodes = set(self.pipe_loop_finder.find(lines))
        return len(loop_nodes)//2