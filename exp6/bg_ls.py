__author__ = 'shen'
# 使用拉斯维加斯算法解决0-1背包问题, 只能找到算法的一个解，而不能找到最优解
# 尝试找非平凡解吧

from random import random

w = [0, 5, 2, 1, 6, 3]
v = [0, 3, 6, 8, 2, 1]
c = 6
n = len(w) - 1
# x = [1 for i in range(n + 1)]


def random_01():
    if random() > 0.5:
        return 1
    else:
        return 0


def w_total(x, w):
    total = 0
    for i in range(len(w)):
        total += x[i] * w[i]
    return total


def las_vegas():
    failure = True
    while failure:
        x = [random_01() for i in range(len(w))]
        x[0] = 0
        if w_total(x, w) < c:
            failure = False
            return x


def las_vegas_backtrack():
    i = n
    x = [random_01() for j in range(len(w))]
    x[0] = 0
    while w_total(x, w) > c:
        backtrack(i, x)
        i -= 1
    return x



def backtrack(i, x):
    if x[i] == 1:
        x[i] = 0


if __name__ == '__main__':
    print(las_vegas())
    print(las_vegas_backtrack())