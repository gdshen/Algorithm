__author__ = 'shen'
import numpy as np
import time


def mergesort(array):
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
    a1 = mergesort(a1)
    a2 = mergesort(a2)
    return merge(a1, a2)


def merge(a1, a2):
    c = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
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


if __name__ == "__main__":
    l = np.random.rand(10)
    li = l.tolist()
    print(mergesort(li))
