# https://replit.com/languages/python3

import sys
from heapq import heappop, heappush

class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))

def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)

def increase_one(lst):
    return [x + 1 for x in lst]

def findShortestPaths(graph, source, n):
    pq = []
    heappush(pq, Node(source))
    dist = [sys.maxsize] * n
    dist[source] = 0
    done = [False] * n
    done[source] = True
    prev = [-1] * n

    while pq:
        node = heappop(pq)
        u = node.vertex

        for (v, weight) in graph.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))

        done[u] = True

    route = []
    for i in range(n):
        if i != source and dist[i] != sys.maxsize:
            get_route(prev, i, route)

            print(
                f'Path ({source+1} to {i+1}): Minimum cost = {dist[i]}, R = {increase_one(route)}')
            route.clear()


def TESTT():
    edges = [(2, 4, 1), (0, 1, 1), (1, 2, 4), (0, 3, 2), (3, 2, 2), (1, 4, 5)]
    n = 5
    graph = Graph(edges, n)
    findShortestPaths(graph, 0, n)
    # for source in range(n):
    #     findShortestPaths(graph, source, n)


if __name__ == '__main__':
    T = int(input("TestCases\n"))
    for _ in range(T):
        nodes = int(input("Num of nodes\n"))
        edges_num = int(input("Num of edges\n"))
        edges_lst = []
        flag = False
        for __ in range(edges_num) :
            flag = True
            u, v, w = [int(x) for x in input("Enter three values\n").split(' ')]
            tup = (u-1, v-1, w)
            edges_lst.append(tup)
        if (not flag):
            print("0, path : 1")

        graph = Graph(edges_lst, nodes)
        findShortestPaths(graph, 0, nodes)




# 3 5 1
# 1 2 1
# 2 3 4
# 1 4 2
# 4 3 2
# 2 5 5