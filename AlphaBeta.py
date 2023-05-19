import networkx as nx


def maxIndex(costs):
    max = 0
    for i in range(len(costs)):
        if costs[max] < costs[i]:
            max = i
    return max

def minIndex(costs):
    min = 0
    for i in range(len(costs)):
        if costs[min] > costs[i]:
            min = i
    return min
class AlphaBeta:
    def __init__(self, G, heuristics):
        self.G = G
        self.H = heuristics

    def isTerminal(self, node):
        adj = list(self.G.adj[node].keys())

        for i in reversed(range(len(adj))):
            if adj[i] in self.visited:
                adj.pop(i)

        if len(adj) == 0:
            return True

    def alphaBeta(self, source, heuristics):
        self.visited = []
        self.heuristic_result = {}

        self.miniMax("Max", source, heuristics, -1000000000, 100000000)
        G = self.G

        for v in G.nodes:
            if v in self.heuristic_result.keys():
                G.nodes[v]['val'] = str(self.heuristic_result[v]) + ':' + v
            else:
                G.nodes[v]['val'] = 'X'+ ':' + v

        return G

    def miniMax(self, turn, source, heuristics, alpha, beta):
        self.visited.append(source)
        if self.isTerminal(source):
            self.heuristic_result[source] = heuristics[source]
            return heuristics[source]

        if turn == "Max":
            adj = list(self.G.adj[source])
            costs=[]
            # Removing visited nodes
            for i in reversed(range(len(adj))):
                if adj[i] in self.visited:
                    adj.pop(i)
            # Recursive call to Min
            for v in adj:
                result = self.miniMax("Min", v, heuristics, alpha, beta)
                if result > alpha:
                    alpha = result
                if result > beta:
                    self.heuristic_result[source] = result
                    return result
                costs.append(result)
            max_index = maxIndex(costs)
            self.heuristic_result[source] = costs[max_index]
            return costs[max_index]

        if turn == 'Min':
            adj = list(self.G.adj[source])
            costs = []
            # Removing visited nodes
            for i in reversed(range(len(adj))):
                if adj[i] in self.visited:
                    adj.pop(i)
            # Recursive call to Max
            for v in adj:
                result = self.miniMax("Max", v, heuristics, alpha, beta)
                if result < beta:
                    beta = result
                if result < alpha:
                    self.heuristic_result[source] = result
                    return result
                costs.append(result)
            min_index = minIndex(costs)
            self.heuristic_result[source] = costs[min_index]
            return costs[min_index]

