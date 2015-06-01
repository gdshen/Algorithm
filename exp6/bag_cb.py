from pprint import pprint

__author__ = 'shen'
# 使用分支限界解决0-1背包问题, 使用的时FIFO队列，只返回了最大值，没有返回最大值的构成

from collections import deque


class node:
    def __init__(self, level, value, cw, cv):
        self.level = level
        self.value = value
        self.cw = cw
        self.cv = cv

    def __str__(self, *args, **kwargs):
        return "level{0} value{1} cw{2} cv{3}".format(self.level, self.value, self.cw, self.cv)


w = [0, 1, 2, 5, 6, 3]
v = [0, 8, 6, 3, 2, 1]
c = 6
n = len(w) - 1


def sack():
    cw = 0
    cv = 0
    best_x = 0
    d = deque()
    i = 1
    up = bound(1, cw, cv, n)
    while i != n + 1:
        if cw + w[i] <= c:
            if cv + v[i] > best_x:
                best_x = cv + v[i]
            d.append(node(i + 1, 1, cw + w[i], cv + v[i]))
        up = bound(i + 1, cw, cv, n)
        if up > best_x:
            d.append(node(i + 1, 0, cw, cv))
        p = d.popleft()
        i = p.level
        cv = p.cv
        cw = p.cw
    return best_x


def bound(i, cw, cv, n):
    cleft = c - cw
    b = cv
    while i <= n and w[i] <= cleft:
        cleft -= w[i]
        b += v[i]
        i += 1
    if i <= n:
        b += v[i] / w[i] * cleft
    return b


if __name__ == '__main__':
    v = sack()
    print(v)
