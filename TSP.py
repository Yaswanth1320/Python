# Implementation traveling salesman by using python

from sys import maxsize
from itertools import permutations
V = 4


def travellingSalesmanProblem(graph, s):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        min_path = min(min_path, current_pathweight)

    return min_path


# Driver Code
if __name__ == "__main__":

    graph = [[0, 15, 10, 20], [10, 0, 25, 35],
             [35, 15, 0, 30], [25, 20, 30, 0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))
