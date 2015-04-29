"""
实现最长公共子序列算法
"""
from pprint import pprint


def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for i in range(n + 1)] for i in range(m + 1)]
    b = [["" for i in range(n + 1)] for i in range(m + 1)]
    for i in range(0, m):
        for j in range(0, n):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "left-up"
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "up"
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = "left"
    return c, b


def lcs_print(b, x, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j] == "left-up":
        lcs_print(b, x, i - 1, j - 1)
        print(x[i], end=" ")
    elif b[i][j] == "up":
        lcs_print(b, x, i - 1, j)
    else:
        lcs_print(b, x, i, j - 1)


if __name__ == "__main__":
    x = "ABCBDAB"
    y = "BDCABA"
    c, b = lcs_length(x, y)
    pprint(c)
    pprint(b)
    lcs_print(b, x, len(x) - 1, len(y) - 1)