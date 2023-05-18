import networkx as nx

def lowestIndex(costs):
    min = 0

    for i in range(len(costs)):
        if costs[i] > min:
            min = i

    return min

def getIndex(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i

class UCS:
    def __init__(self, G):
        self.G = G
    def ucs(self, goal_list, start):
        Graph = self.G

        # initializing parents
        parents = {}
        for v in list(Graph.nodes):
            parents[v] = None

        Q = []
        costs = []
        visited = []
        Q.append(start)
        costs.append(0)

        while len(Q) > 0:
            lowest = lowestIndex(costs)

            curr = Q.pop(lowest)
            curr_cost = costs.pop(lowest)
            visited.append(curr)

            # Goal Test
            if curr in goal_list:

                # - Goal is found
                path = nx.DiGraph()
                while curr != start:
                    path.add_edge(parents[curr], curr)
                    curr = parents[curr]

                return path
            adj = list(Graph.adj[curr])

            for v in adj:
                adjacency = dict(Graph.adj[curr][v])
                if (v not in visited) and (v not in Q):
                    Q.append(v)
                    costs.append(curr_cost + adjacency['weight'])
                    parents[v] = curr

                elif v in Q:
                    index = getIndex(Q,v)
                    if costs[index] > curr_cost + adjacency['weight']:
                        costs[index] = curr_cost + adjacency['weight']
                        parents[index] = curr

        return []


