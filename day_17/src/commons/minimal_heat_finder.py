import heapq as priority_queue

START="S"
UP="^"
DOWN="v"
LEFT="<"
RIGHT=">"

class MinimalHeatFinder:

    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end

    def find(self, min_steps, max_steps):
        queue = [(0, *self.start, START)]
        visited = set()

        while len(queue) > 0:
            heat, current_row, current_col, direction = priority_queue.heappop(queue)
            if (current_row, current_col) == self.end: 
                return heat
            if (current_row, current_col, direction) in visited: 
                continue
            visited.add((current_row, current_col, direction))

            for next_direction in self.get_next_directions(direction):
                next_row, next_col, total_heat = current_row, current_col, heat

                for step in range(1, max_steps+1):
                    next_row, next_col = self.get_next(next_row, next_col, next_direction)
                    if not self.is_inside_grid(next_row, next_col):
                        continue
                    total_heat += self.grid[next_row][next_col]
                    if step >= min_steps:
                        priority_queue.heappush(queue, (total_heat, next_row, next_col, next_direction))

    def get_next_directions(self, direction):
        if direction == START:
            return {UP, DOWN, LEFT, RIGHT}
        if direction in {UP, DOWN}:
            return {LEFT, RIGHT}
        return {UP, DOWN}

    def get_next(self, row, col, direction):
        if direction == UP:
            return row-1, col
        if direction == DOWN:
            return row+1, col
        if direction == LEFT:
            return row, col-1
        if direction == RIGHT:
            return row, col+1

    def is_inside_grid(self, row, col):
        return row >=0 and row < len(self.grid) and col >= 0 and col < len(self.grid[0])