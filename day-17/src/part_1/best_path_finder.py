import math

class BestPathFinder:
    def find(self, grid):
        unvisited = self.get_all_nodes(grid)
        distance_by_node = {node:math.inf for node in unvisited}
        
        node = (0,0)
        distance_by_node[node] = 0
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
        #         line.append(distance_by_node[(i,j)])
        #     print(line)
        # for n, distance in distance_by_node.items():
        #     print(n, distance)
        print("")
        last_node = (len(grid)-1, len(grid[0])-1)
        return distance_by_node[last_node] + int(grid[0][0])

    def get_closest_node(self, node, grid, unvisited, distance_by_node):
        for next_node in self.get_nodes_inside_grid(node, grid):
            row, col = next_node
            cost = int(grid[row][col])
            total = cost + distance_by_node[node]
            distance_by_node[next_node] = min(distance_by_node[next_node], total)
        closest_node = None
        closest_node_distance = math.inf
        for next_node, distance in distance_by_node.items():
            if next_node in unvisited and distance < closest_node_distance:
                closest_node_distance = distance
                closest_node = next_node

        # print("SELECTED NODE", closest_node)
        return closest_node

    def get_nodes_inside_grid(self, node, grid):
        row, col = node
        all_possibilities = [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]
        return [node for node in all_possibilities if self.is_node_inside_grid(node, grid)]

    def is_node_inside_grid(self, node, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        row, col = node
        return row >= 0 and col >= 0 and row < num_rows and col < num_cols
        

    def get_all_nodes(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        nodes = set()
        for i in range(num_rows):
            for j in range(num_cols):
                nodes.add((i, j))
        return nodes