import math

UP="^"
DOWN="v"
LEFT="<"
RIGHT=">"

class Node:
    def __init__(self, row, col, direction=None, steps=1):
        self.row = row
        self.col = col
        self.direction = direction
        self.steps = steps

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return (self.row, self.col, self.direction, self.steps) == (other.row, other.col, other.direction, other.steps)

    def __hash__(self):
        return hash((self.row, self.col, self.direction, self.steps))


class BestPathFinder:
    def find(self, grid):
        distance_by_node = {}
        
        node = Node(0, 0, RIGHT, 1)
        distance_by_node[node] = 0
        # for n, distance in distance_by_node.items():
        #     print(n, distance)
        # print("")
        visited = set()
        while node != None:
            # print("NODE", node)
            visited.add(node)
            node = self.get_closest_node(node, grid, visited, distance_by_node)
            # for i in range(len(grid)):
            #     line = []
            #     for j in range(len(grid[0])):
            #         line.append(distance_by_node[(i,j)])
            #     print(line)
            # print("")
            # for i in range(len(grid)):
            #     line = []
            #     for j in range(len(grid[0])):
            #         line.append(distance_by_node[(i,j)].value)
            #     print(line)
            # print("")
            # for i in range(len(grid)):
            #     line = []
            #     for j in range(len(grid[0])):
            #         if distance_by_node[(i,j)].direction == None:
            #             line.append("--")
            #         else:
            #             line.append(distance_by_node[(i,j)].direction + str(distance_by_node[(i,j)].steps))
            #     print(line)
            # print(" ")

        last_node = (len(grid)-1, len(grid[0])-1)
        distances_to_last_node = []
        for node, distance in distance_by_node.items():
            if (node.row, node.col) == last_node:
                distances_to_last_node.append(distance)
        # print(distances_to_last_node)
        return min(distances_to_last_node)+1

    def get_closest_node(self, current_node, grid, visited, distance_by_node):
        next_nodes = self.get_nodes_inside_grid(current_node, grid)
        for next_node in next_nodes:
            cost = int(grid[next_node.row][next_node.col])
            current_node_distance = distance_by_node[current_node]
            next_node_distance = distance_by_node[next_node] if next_node in distance_by_node else math.inf
            total_distance = cost + current_node_distance
            if total_distance < next_node_distance:
                if next_node.steps <= 3:
                    distance_by_node[next_node] = total_distance
        closest_node = None
        closest_node_distance = math.inf
        for next_node, distance in distance_by_node.items():
            if next_node not in visited and distance < closest_node_distance:
                closest_node_distance = distance
                closest_node = next_node

        # print("SELECTED NODE", closest_node)
        return closest_node

    def get_nodes_inside_grid(self, node, grid):
        row, col = node.row, node.col
        all_possibilities = [
            (row-1,col,UP), 
            (row+1,col,DOWN), 
            (row,col-1,LEFT), 
            (row,col+1,RIGHT)]
        return [self.map_to_node_entity(node, node_tuple) for node_tuple in all_possibilities if self.is_node_inside_grid(node_tuple, grid)]
    
    def map_to_node_entity(self, current_node, next_node_tuple):
        row, col, direction = next_node_tuple
        current_direction = current_node.direction
        steps = 1 if current_direction != direction else current_node.steps + 1
        return Node(row, col, direction, steps)


    def is_node_inside_grid(self, node, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        row, col, _ = node
        return row >= 0 and col >= 0 and row < num_rows and col < num_cols
        

    def get_all_nodes(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        nodes = set()
        for i in range(num_rows):
            for j in range(num_cols):
                nodes.add((i, j))
        return nodes