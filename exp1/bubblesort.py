__author__ = 'shen'
import numpy as np
import time


def bubblesort(array):
    """
    This is the code for bubble sort algorithm.
    :param array: the array to be sorted
    :return: the sorted array
    """
    for i in range(len(array), 1, -1):
        for j in range(i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == "__main__":
    l = np.random.rand(10)
    t1 = time.clock()
    bubblesort(l)
    t2 = time.clock()
    print(l)
    t = t2 - t1
    print(t)