# 使用动态规划来求解0-1背包问题
from pprint import pprint

w = [0, 5, 2, 1, 6, 3]
v = [0, 3, 6, 8, 2, 1]
c = 6
n = len(w) - 1
m = [[0 for j in range(c + 1)] for i in range(n + 1)]
x = [0 for i in range(n + 1)]


def knap_snak(w, v):
    n = len(v) - 1
    for j in range(1, c + 1):
        if j >= w[n]:
            m[n][j] = v[n]
    for i in range(n - 1, 0, -1):
        for j in range(1, c + 1):
            if j < w[i]:
                m[i][j] = m[i + 1][j]
            else:
                m[i][j] = max(m[i + 1][j], m[i + 1][j - w[i]] + v[i])
    # pprint(m)
    # pprint(w)


def show(w, c):
    for i in range(1, n):
        if m[i][c] != m[i + 1][c]:
            x[i] = 1
            c -= w[i]
    if m[n][c] != 0:
        x[n] = 1
    pprint(x)


if __name__ == '__main__':
    knap_snak(w, v)
    show(w, c)
