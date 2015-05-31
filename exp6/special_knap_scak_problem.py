# 特殊类型的0-1背包问题

w = [1, 2, 3, 4, 5, 6, 7]
v = [7, 6, 5, 4, 3, 2, 1]
c = 14
x = [0, 0, 0, 0, 0, 0, 0]

if __name__ == '__main__':
    g = 0
    for i in range(len(w)):
        g += w[i]
        if g <= c:
            x[i] = 1
    print(x)
