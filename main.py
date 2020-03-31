from collections import defaultdict
import math

from src.ask_file_path import ask_file_path
from src.open_file import open_file
from src.truth_table import truth_table

if __name__ == "__main__":

    freq = [0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.92, 0.94]

    array = open_file(path=ask_file_path())

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


    graph = dict()
    for i in range(len(array)):
        c = True
        for j in range(len(array)):
            if array[j] == '1':
                if str(i + 1) not in graph:
                    graph[str(i + 1)] = list()
                graph[str(i + 1)].append(str(j + 1))
                c = False
        if (c):
            if str(i + 1) not in graph:
                graph[str(i + 1)] = list()
            graph[str(i + 1)].append(str(i + 1))

    g = Graph(len(graph.keys()))
    for i, v in graph.items():
        for e in v:
            g.add_edge(i, e)

    s = '1'
    for i in range(len(graph)):
        if graph[str(i + 1)] == list(str(i + 1)):
            g.print_all_paths(s, str(i + 1))

    table = truth_table(len(array))

    able_bodied = []
    for i in range(len(table)):
        for j in range(len(AllPath)):
            c = True
            for k in range(len(AllPath[j])):
                if table[i][int(AllPath[j][k]) - 1] != 1:
                    c = False
                    break
            if (c):
                break
        if (c):
            able_bodied.append(table[i])

    p_system = 0
    for i in range(len(able_bodied)):
        p_state = 1
        for j in range(len(able_bodied[i])):
            if able_bodied[i][j] == 1:
                p_state *= freq[j]
            else:
                p_state *= 1 - freq[j]
        p_system += p_state

    print("P_system =", p_system)
    lambda1 = -math.log(p_system) / 10
    Tndv = 1 / lambda1
    print("λ =", lambda1)
    print("Tндв =", Tndv)