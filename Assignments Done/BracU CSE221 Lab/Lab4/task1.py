# https://replit.com/languages/python3

import sys
from heapq import heappop, heappush


class Node:
    def __init__(self, v, w=0):
        self.v = v
        self.w = w

    def __lt__(self, other):
        return self.w < other.w


class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dst, w) in edges:
            self.adjList[src].append((dst, w))


def increase_one(lst):
    return [x + 1 for x in lst]


def minTitans(graph, source, n):
    priorQ = []
    heappush(priorQ, Node(source))
    dist = [sys.maxsize] * n
    dist[source], done = 0, [False] * n
    done[source], prev = True, [-1] * n

    while priorQ:
        node = heappop(priorQ)
        u = node.v
        for (v, weight) in graph.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:
                prev[v], dist[v] = u, dist[u] + weight
                heappush(priorQ, Node(v, dist[v]))
        done[u] = True

    xii = 0
    for i in range(n):
        if i != source and dist[i] != sys.maxsize:
            xii = dist[i]
    print(f'{xii}')


if __name__ == '__main__':

    with open('input1.txt') as f:
        lines = f.readlines()
    sdf = 0
    T = int(lines[sdf])
    sdf += 1
    for _ in range(T):
        nodes, edges_num = int(lines[sdf][0]), int(lines[sdf][2])
        sdf += 1
        # nodes, edges_num = [int(x) for x in input().split(' ')]
        edges_lst = []

        for __ in range(edges_num):
            u, v, w = int(lines[sdf][0]), int(lines[sdf][2]), int(lines[sdf][4])
            # u, v, w = [int(x) for x in input("Enter three values\n").split(' ')]
            tup = (u - 1, v - 1, w)
            edges_lst.append(tup)

        graph = Graph(edges_lst, nodes)
        minTitans(graph, 0, nodes)
