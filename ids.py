import networkx as nx
DG = nx.DiGraph()
G = nx.Graph()
Goal_list = []
class IDS:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def idsTraversal(self, dfsPath):
        for i in dfsPath:
            print(i, end=" ")
        print()

    def dlSearch(self, s, g, limit):
        visited = []
        queue = []
        expanded = []
        queue.append(s)
        visited.append(s)

        while queue:
            current = queue.pop(0)
            expanded.append(current[0])
            if current[0] in g:
                current.reverse()
                return current
            if len(current) < limit+1:
                neighbors = self.graph[current[0]]
                neighborsInOrder = sorted(neighbors)  # visits in the order they were expanded
                neighborsInOrder.reverse()
                for neighbor in neighborsInOrder:
                    if neighbor not in expanded:
                        visited.append(neighbor)
                        tempPath = [neighbor]
                        for parents in current:
                            tempPath.append(parents)
                        queue.insert(0, tempPath)
        return []

    def ids(self, s, g, max_depth):
        for i in range(max_depth):
            path = self.dlSearch(s, g, i)
            if g in path:
                return path
        return []



G.add_edge( 'A', 'B', weight=1)
G.add_edge('B', 'C', weight=1)
G.add_edge('C', 'D', weight=1)
G.add_edge('A', 'E', weight=1)
G.add_edge('E', 'D', weight=1)
G.add_edge('A', 'F', weight=1)

D = IDS(G, "nothing")
print(D.ids('A', 'D', 5))