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


def mergesort(array, position):
    """
    This is the mergesort.And it doesn't modify the array itself
    :param array: unsorted array
    :return: sorted array
    """
    n = len(array)
    if n <= 1:
        return array
    a1 = array[:n // 2]
    a2 = array[n // 2:]
    a1 = mergesort(a1, position)
    a2 = mergesort(a2, position)
    return merge(a1, a2, position)


def merge(a1, a2, position):
    c = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i][position] <= a2[j][position]:
            c.append(a1[i])
            i += 1
        else:
            c.append(a2[j])
            j += 1
    if a1[i:]:
        c += a1[i:]
    if a2[j:]:
        c += a2[j:]
    return c


def findnlgn(l):
    sortl = mergesort(mergesort(l, 1), 0)
    templength = countdistance(sortl[0], sortl[1])
    for i in range(1, len(sortl) - 1):
        if countdistance(sortl[i], sortl[i + 1]) < templength:
            temp = sortl[i], sortl[i + 1]
            templength = countdistance(sortl[i], sortl[i + 1])
    pprint(temp)
    pprint(templength)


if __name__ == "__main__":
    l = getpoint(5000)
    # sortl = sorted(l, key=itemgetter(0, 1)
    sortl = mergesort(mergesort(l, 1), 0)
    templength = countdistance(sortl[0], sortl[1])
    for i in range(1, len(sortl) - 1):
        if countdistance(sortl[i], sortl[i + 1]) < templength:
            temp = sortl[i], sortl[i + 1]
            templength = countdistance(sortl[i], sortl[i + 1])
    pprint(temp)
    pprint(templength)
