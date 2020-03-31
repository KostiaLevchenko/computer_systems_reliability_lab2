from collections import defaultdict
AllPath = []


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_all_paths_util(self, u, d, visited, path):
        global AllPath
        visited[list(self.graph.keys()).index(u)] = True
        path.append(u)
        if u == d:
            AllPath.append([])
            for i in range(len(path)):
                AllPath[len(AllPath) - 1].append(path[i])
        else:
            for i in self.graph[u]:
                if not visited[list(self.graph.keys()).index(i)]:
                    self.print_all_paths_util(i, d, visited, path)
        path.pop()
        visited[list(self.graph.keys()).index(u)] = False

    def print_all_paths(self, s, d):
        visited = [False] * self.V
        path = []
        self.print_all_paths_util(s, d, visited, path)