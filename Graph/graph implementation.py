from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edges(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) # this is removed when using for the directed graph

    def bfs(self,start_node):
        visited = set()
        queue = deque([start_node])
        traversal =[]

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                for i in self.adj_list[node]:
                    if i not in visited:
                        queue.append(i)

        return traversal

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        traversal = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                for i in self.adj_list[node]:
                    if i not in visited:
                        stack.append(i)

        return traversal

graph = Graph()
graph.add_edges(0,1)
graph.add_edges(0,2)
graph.add_edges(1,2)
graph.add_edges(1,4)
graph.add_edges(2,5)
graph.add_edges(3,4)

start_node = 0
print(graph.bfs(start_node))
print(graph.dfs(start_node))

