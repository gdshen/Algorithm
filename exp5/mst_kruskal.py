"""
使用Kruskal算法和Prim算法求最小生成树
"""

from pprint import pprint


def find_set(u, v, m_set):
    for i in m_set:
        if u in i and v in i:
            return True
    return False


def union(u, v, m_set):
    t = []
    t_set = set()
    for i in m_set:
        if u not in i and v not in i:
            t.append(i)
        else:
            t_set = t_set | i
    t.append(t_set)
    return t


def mst_kruskal(V, E):
    A = []
    m_set = []
    for v in V:
        m_set.append({v})
    edges = sorted(E, key=lambda e: e[1])
    for edge in edges:
        u, v = edge[0]
        if not find_set(u, v, m_set):
            A.append(edge[0])
            m_set = union(u, v, m_set)
    return A


if __name__ == '__main__':
    V = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
    E = [[{'a', 'h'}, 8], [{'a', 'b'}, 4], [{'b', 'c'}, 8], [{'b', 'h'}, 11], [{'c', 'd'}, 7], [{'c', 'f'}, 4],
         [{'c', 'i'}, 2], [{'d', 'e'}, 9], [{'d', 'f'}, 14], [{'e', 'f'}, 10], [{'f', 'g'}, 2], [{'g', 'h'}, 1],
         [{'g', 'i'}, 6], [{'h', 'i'}, 7]]
    A = mst_kruskal(V, E)
    pprint(A)
