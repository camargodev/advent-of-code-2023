ROLLING_STONE = "O"

class StoneLoopDetector:
    def __init__(self):
        self.stones_order = 1
        self.loop_start = None
        self.stone_states = dict()

    def is_loop_detected(self, stones):
        stones_tuple = self.to_tuple(stones)
        if stones_tuple in self.stone_states:
            self.loop_start, _ = self.stone_states[stones_tuple]
            return True
        self.stone_states[stones_tuple] = (self.stones_order, self.calculate_total(stones))
        self.stones_order += 1
        return False
    
    def calculate_total_after_iterations(self, iterations):
        loop_end = self.stones_order
        loop_size = (loop_end-self.loop_start)

        solution_index = self.loop_start + ((iterations-self.loop_start) % loop_size)
        for stone_order, stone_total in self.stone_states.values():
            if stone_order == solution_index:
                return stone_total
        return None

    def calculate_total(self, stones):
        total = 0
        max_points = len(stones)
        for line_idx, shifted_stone_line in enumerate(stones):
            numbers_of_rolling_stones = shifted_stone_line.count(ROLLING_STONE)
            line_points = max_points - line_idx
            total += numbers_of_rolling_stones * line_points
        return total


    def to_tuple(self, stones):
        stone_tuple = []
        for line in stones:
            stone_tuple.append(tuple(line))
        return tuple(stone_tuple)
