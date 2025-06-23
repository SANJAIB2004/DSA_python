from collections import defaultdict

class WeightedGraph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, weight, directed=False):
        # Add edge u -> v with weight
        self.adj_list[u].append((v, weight))

        # For undirected graphs, also add v -> u
        if not directed:
            self.adj_list[v].append((u, weight))

    def print_graph(self):
        for vertex in self.adj_list:
            edges = ', '.join([f"{neighbor}({weight})" for neighbor, weight in self.adj_list[vertex]])
            print(f"{vertex} -> {edges}")

# Example usage
g = WeightedGraph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)
g.add_edge('D', 'E', 6)
g.add_edge('F', 'E', 3, directed=True)  # Directed edge

g.print_graph()
