__author__ = 'shen'
# 使用回溯法解决0-1背包问题

w = [0, 5, 2, 1, 6, 3]
v = [0, 3, 6, 8, 2, 1]

x = [0 for i in range(len(w))]
best_x = [0 for i in range(len(w))]
n = len(w) - 1
cw = 0
c = 6


def value_sum(x):
    value = 0
    for i in range(len(w)):
        value += v[i] * x[i]
    return value


def backtrack(i):
    global best_x
    global cw
    if i > n:
        if value_sum(best_x) < value_sum(x):
            best_x = x.copy()
    else:
        if cw + w[i] <= c:
            x[i] = 1
            cw += w[i]
            backtrack(i+1)
            cw -= w[i]
        x[i] = 0
        backtrack(i+1)



if __name__ == '__main__':
    backtrack(1)
    print(best_x)
