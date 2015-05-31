"""
使用prim算法求最小生成树
"""
from pprint import pprint

_ = float('inf')


class Node():
    name = 0
    key = _
    parent = None

    def __init__(self, name):
        self.name = name


def extract_min(q, V):
    t = _
    for i in q:
        if V[i].key < t:
            t = V[i].key
            n = i
    return n


def mst_trim(G):
    A = []
    V = [Node(i) for i in range(9)]
    q = {i for i in range(len(G))}
    for i in range(len(G)):
        V[i].key = G[i][0]
        V[i].parent = 0
    V[0].key = 0
    while len(q) != 0:
        u = extract_min(q, V)
        q.remove(u)
        A.append((u, V[u].parent))
        for i in range(len(G)):
            if i != u:
                if i in q and G[u][i] < V[i].key:
                    V[i].parent = u
                    V[i].key = G[i][u]
    return A


if __name__ == '__main__':
    G = [[_, 4, _, _, _, _, _, 8, _],
         [4, _, 8, _, _, _, _, 11, _],
         [_, 8, _, 7, _, 4, _, _, 2],
         [_, _, 7, _, 9, 14, _, _, _],
         [_, _, _, 9, _, 10, _, _, _],
         [_, _, 4, 14, 10, _, 2, _, _],
         [_, _, _, _, _, 2, _, 1, 6],
         [8, 11, _, _, _, _, 1, _, 7],
         [_, _, 2, _, _, _, 6, 7, _]]
    A = mst_trim(G)
    pprint(A)