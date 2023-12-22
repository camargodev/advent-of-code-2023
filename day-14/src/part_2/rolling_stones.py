from src.part_2.stone_loop_detector import StoneLoopDetector

CUBE_STONE = "#"
ROLLING_STONE = "O"
SPACE = "."

NUM_LOOPS = 1000000000

class RollingStone:
    def move_like_jeager(self, lines):
        stones = [[char for char in line] for line in lines]
        loop_detector = StoneLoopDetector()

        while not loop_detector.is_loop_detected(stones):
            stones = self.full_rotation(stones)

        return loop_detector.calculate_total_after_iterations(NUM_LOOPS)

    
    def full_rotation(self, stones):
        group_stones_to_the_start = lambda empty_size, grouped_stones: grouped_stones + (SPACE * empty_size)
        group_stones_to_the_end = lambda empty_size, grouped_stones: (SPACE * empty_size) + grouped_stones
        shifted_stones = self.shift_vertically(stones, group_stones_to_the_start)
        shifted_stones = self.shift_horizontally(shifted_stones, group_stones_to_the_start)
        shifted_stones = self.shift_vertically(shifted_stones, group_stones_to_the_end)
        shifted_stones = self.shift_horizontally(shifted_stones, group_stones_to_the_end)
        return shifted_stones
    
    def shift_horizontally(self, stones, grouping_function):
        shifted_stones = []
        for stone_line_idx in range(len(stones)):
            shifted_parts = []
            str_stone_line = "".join(stones[stone_line_idx])
            for part in str_stone_line.split(CUBE_STONE):
                grouped_stones = part.replace(SPACE, "")
                empty_size = len(part) - len(grouped_stones)
                shifted_parts.append(grouping_function(empty_size, grouped_stones))
            str_shifted_line = CUBE_STONE.join(shifted_parts)
            shifted_line = [char for char in str_shifted_line]
            shifted_stones.append(shifted_line)

        return shifted_stones
    
    def shift_vertically(self, stones, grouping_function):
        shifted_stones = stones
        for stone_col_idx in range(len(stones[0])):
            str_stone_col = "".join([stones[row_idx][stone_col_idx] for row_idx in range(len(stones))])
            shifted_parts = []
            for part in str_stone_col.split(CUBE_STONE):
                grouped_stones = part.replace(SPACE, "")
                empty_size = len(part) - len(grouped_stones)
                shifted_parts.append(grouping_function(empty_size, grouped_stones))
            str_shifted_col = CUBE_STONE.join(shifted_parts)
            for row_idx in range(len(stones)):
                shifted_stones[row_idx][stone_col_idx] = str_shifted_col[row_idx]

        return shifted_stones