from collections import deque
from src.commons.tile import *

LEFT="LEFT"
RIGHT="RIGHT"
UP="UP"
DOWN="DOWN"

class EnergizedPathFinder:
    def find(self, grid, source):
        visited = set()
        nodes = deque()
        nodes.append(source)
        while len(nodes) > 0:
            node = nodes.popleft()
            if node in visited:
                continue
            visited.add(node)
            next_nodes = self.calculate_next_nodes(node, grid)
            nodes.extend(next_nodes)
        
        unique_coords = set([(node.row, node.col) for node in visited])
        return unique_coords

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