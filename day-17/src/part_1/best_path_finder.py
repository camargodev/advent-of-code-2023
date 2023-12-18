import math

UP="^"
DOWN="v"
LEFT="<"
RIGHT=">"

class Distance:
    def __init__(self, value=math.inf, direction=None, steps=1):
        self.value = value
        self.direction = direction
        self.steps = steps

class BestPathFinder:
    def find(self, grid):
        unvisited = self.get_all_nodes(grid)
        distance_by_node = {node:Distance() for node in unvisited}
        
        node = (0,0)
        distance_by_node[node] = Distance(0, RIGHT)
        # for n, distance in distance_by_node.items():
        #     print(n, distance)
        # print("")
        visited = set()
        while len(unvisited) > 0:
            # print("NODE", node)
            unvisited = unvisited - {node}
            visited.add(node)
            node = self.get_closest_node(node, grid, unvisited, distance_by_node)
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
            for i in range(len(grid)):
                line = []
                for j in range(len(grid[0])):
                    if distance_by_node[(i,j)].direction == None:
                        line.append("--")
                    else:
                        line.append(distance_by_node[(i,j)].direction + str(distance_by_node[(i,j)].steps))
                print(line)
            print(" ")
        # for n, distance in distance_by_node.items():
        #     print(n, distance)
        last_node = (len(grid)-1, len(grid[0])-1)
        return distance_by_node[last_node].value + int(grid[0][0])

    def get_closest_node(self, node, grid, unvisited, distance_by_node):
        for next_node in self.get_nodes_inside_grid(node, grid):
            next_row, next_col, next_direction = next_node
            cost = int(grid[next_row][next_col])
            node_distance = distance_by_node[node]
            next_node_distance = distance_by_node[(next_row, next_col)]
            total = cost + node_distance.value
            if total < next_node_distance.value:
                current_direction = node_distance.direction
                steps = 1
                if next_direction == current_direction:
                    steps = node_distance.steps + 1
                if steps <= 3:
                    distance_by_node[(next_row, next_col)] = Distance(total, next_direction, steps)
        closest_node = None
        closest_node_distance = math.inf
        for next_node, distance in distance_by_node.items():
            if next_node in unvisited and distance.value < closest_node_distance:
                closest_node_distance = distance.value
                closest_node = next_node

        # print("SELECTED NODE", closest_node)
        return closest_node

    def get_nodes_inside_grid(self, node, grid):
        row, col = node
        all_possibilities = [(row-1,col,UP), (row+1,col,DOWN), (row,col-1,LEFT), (row,col+1,RIGHT)]
        return [node for node in all_possibilities if self.is_node_inside_grid(node, grid)]

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