class BFS:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def bfsTraversal(self, bfsPath):
        for i in bfsPath:
            print(i, end=" ")
        print()

    def bfsSearch(self, s, g):
        visited = []
        queue = []
        path = []
        queue.append(s)
        visited.append(s)

        while queue:
            current = queue.pop(0)
            path.append(current)

            if current in g:
                return path

            neighbors = self.graph[current]
            neighborsInOrder = sorted(neighbors)  #visits in the order they were expanded

            for neighbor in neighborsInOrder:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return []

    def bfs(self, s, g):
        return self.bfsSearch(s, g)