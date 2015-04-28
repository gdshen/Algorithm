'''
author: Guodong Shen
Student number: PB12210046
'''
from pprint import pprint
import numpy as np
from operator import itemgetter
import math

# todo 算法有错，修改算法
def getpoint(length):
    return np.random.rand(length, 2).tolist()


def countdistance(t1, t2):
    return math.sqrt((t2[0] - t1[0]) ** 2 + (t2[1] - t1[1]) ** 2)


def mininum(p1, p2):
    if p1 == None:
        return p2
    if p2 == None:
        return p1
    if countdistance(p1[0], p1[1]) < countdistance(p2[0], p2[1]):
        return p1
    else:
        return p2


def getdeltaX(delta, midline, l):
    '''
    得到x值距离中线delta的所有左边点
    :return:
    '''
    c = []
    for i in l:
        if midline - i[0] < delta:
            c += i
    return c


def getcoY(x, delta, l):
    '''
    对到对应左边点得相应六个右边点
    :return:
    '''
    c = []
    for i in l:
        if math.fabs(i[1] - x[0]) < delta:
            c += i
    return c


def findnlgnsort(sortl):
    # p 代表一个点对
    length = len(sortl)
    if length == 2:
        return sortl
    if length == 1:
        return None
    p1 = findnlgnsort(sortl[:length // 2])
    p2 = findnlgnsort(sortl[length // 2:])
    p = mininum(p1, p2)
    midline = (sortl[math.floor((len(sortl) - 1) / 2)][0] + sortl[math.ceil((len(sortl) - 1) / 2)][0]) / 2
    delta = countdistance(p)
    for i in getdeltaX(delta, midline, sortl[:length // 2]):
        for j in getcoY(i, delta, sortl[length // 2:]):
            if countdistance(i, j) < delta:
                p = i, j
                delta = countdistance(i, j)
    return p


def findnlgn(l):
    sortl = sorted(l, key=itemgetter(0, 1))
    findnlgnsort(sortl)


if __name__ == "__main__":
    # l = getpoint(5000)
    l = [[1, 2], [1, 3], [1, 1.5], [2, 4], [2, 3.7]]
    p = findnlgn(l)
    print(p)

