from collections import defaultdict, deque

LEFT="LEFT"
RIGHT="RIGHT"
UP="UP"
DOWN="DOWN"

EMPTY="."
HORIZONTAL_SPLIT="-"
VERTICAL_SPLIT="|"
DIAGONAL="\\"
INVERSE_DIAGIONAL="/"

class Tile:
    def __init__(self, direction, row, col):
        self.direction = direction
        self.row = row
        self.col = col

    def __str__(self):
        return f"Tile(row={self.row}, col={self.col}, direction='{self.direction}')"

    def __hash__(self):
        # Using the hash of a tuple containing the attributes as a hash value
        return hash((self.row, self.col, self.direction))

    def __eq__(self, other):
        # Checking equality based on all attributes
        if not isinstance(other, Tile):
            return False
        return (
            self.row == other.row
            and self.col == other.col
            and self.direction == other.direction
        )


class EnergizedTilesCounter:
    def count(self, grid):
        visited = set()
        nodes = deque()
        nodes.append(Tile(RIGHT, 0, 0))
        print_matrix = [["." for x in range(len(grid[0]))] for y in range(len(grid))] 
        while len(nodes) > 0:
            node = nodes.popleft()
            # print("POPPED NODE", node)
            if node in visited:
                continue
            print_matrix[node.row][node.col] = "#"
            for line in print_matrix:
                str_line = "".join(line)
                count = len(str_line.replace(".",""))
                # print(str_line, count)
            visited.add(node)
            next_nodes = self.calculate_next_nodes(node, grid)
            nodes.extend(next_nodes)
        
        for line in print_matrix:
            str_line = "".join(line)
            count = len(str_line.replace(".",""))
            # print(str_line, count)
        unique_coords = set([(node.row, node.col) for node in visited])
        # print("")
        total_count = 0
        for i in range(len(grid)):
            line = ""
            count = 0
            for j in range(len(grid[0])):
                if (i, j) in unique_coords:
                    line += "#"
                    count += 1
                else:
                    line += "."
            total_count += count
            # print(line, count)
        
        # print(total_count)
        return len(unique_coords)

    def calculate_next_nodes(self, node, grid):
        node_value = grid[node.row][node.col]
        next_directions = []
        if node_value == EMPTY:
            next_directions.append(node.direction)
        elif node_value == HORIZONTAL_SPLIT:
            if node.direction in {UP, DOWN}:
                next_directions.append(LEFT)
                next_directions.append(RIGHT)
            else:
                next_directions.append(node.direction)
        elif node_value == VERTICAL_SPLIT:
            if node.direction in {LEFT, RIGHT}:
                next_directions.append(UP)
                next_directions.append(DOWN)
            else:
                next_directions.append(node.direction)
        elif node_value == INVERSE_DIAGIONAL:
            if node.direction == UP:
                next_directions.append(RIGHT)
            if node.direction == DOWN:
                next_directions.append(LEFT)
            if node.direction == LEFT:
                next_directions.append(DOWN)
            if node.direction == RIGHT:
                next_directions.append(UP)
        elif node_value == DIAGONAL:
            if node.direction == UP:
                next_directions.append(LEFT)
            if node.direction == DOWN:
                next_directions.append(RIGHT)
            if node.direction == LEFT:
                next_directions.append(UP)
            if node.direction == RIGHT:
                next_directions.append(DOWN)

        next_nodes = []
        for direction in next_directions:
            next_node = self.calculate_next_node(direction, node)
            if self.is_within_grid(next_node, grid):
                next_nodes.append(next_node)
        return next_nodes


    def is_within_grid(self, node, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        return node.row >= 0 and node.col >= 0 and node.row < num_rows and node.col < num_cols

    def calculate_next_node(self, direction, node):
        row, col = node.row, node.col
        if direction == UP:
            return Tile(direction, row-1, col)
        if direction == DOWN:
            return Tile(direction, row+1, col)
        if direction == LEFT:
            return Tile(direction, row, col-1)
        if direction == RIGHT:
            return Tile(direction, row, col+1)