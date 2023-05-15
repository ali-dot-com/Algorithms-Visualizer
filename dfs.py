class DFS:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def dfsTraversal(self, dfsPath):
        for i in dfsPath:
            print(i, end=" ")
        print()

    def dfsSearch(self, s, g):
        visited = []
        queue = []
        path = []

        queue.append(s)
        visited.append(s)

        while queue:
            current = queue.pop()
            path.append(current)

            if current == g:
                return path

            neighbors = self.graph[current]
            neighborsInOrder = sorted(neighbors)  # visits in the order they were expanded

            for neighbor in neighborsInOrder:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return []

    def dfs(self, s, g):
        return self.dfsSearch(s, g)