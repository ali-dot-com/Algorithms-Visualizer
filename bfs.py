from collections import deque

class Graph_bfs:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType=graphType

    def print_path(self, bfsPath):
        for i in bfsPath:
            print(i, end=" ")
        print()  # Add a newline after printing the path


    def bfsUndirected(self, start_node, goal_node):
        visited = set()
        # visited = []
        queue = deque()
        path = []

        queue.append(start_node)
        visited.add(start_node)
        visited.append(start_node)

        while queue:
            current = queue.popleft()
            path.append(current)

            if current in goal_node:
                return path

            neighbors = self.graph[current]
            sorted_neighbors = sorted(neighbors)  # Sort neighbors in chronological order

            for neighbor in sorted_neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # visited.append(neighbor)
                    queue.append(neighbor)

        return path

    def bfsDirected(self, start_node, goal_node):
        visited = []
        queue = deque()
        path = []
        queue.append(start_node)
        visited.append(start_node)
        while queue:
            current_vertex = queue.popleft()
            path.append(current_vertex)

            if current_vertex in goal_node:
                return path

            neighbors = self.graph[current_vertex]
            sorted_neighbors = sorted(neighbors)  # Sort neighbors in chronological order

            for neighbor in sorted_neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return []

    def bfs(self,start_node, goal_node):
        if self.graphType == "Undirected Graph":
            return self.bfsUndirected(start_node, goal_node)
        else:
            return  self.bfsDirected(start_node, goal_node)


