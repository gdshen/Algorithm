import numpy as np
import time


def partition(array, start, end):
    """
    the partition process of quicksort
    :param array: the array to be sorted
    :param start: the start position
    :param end: the end position
    :return: the flag element position
    """
    x = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def quicksort(array, start, end):
    """
    This is the quick sort algorithm.
    :param array: the sub array which we want to sort
    :param start: the start position of the sub array (in)
    :param end: the end position of the sub array (in)
    :return: the sorted sub array
    """
    if start < end:
        q = partition(array, start, end)
        quicksort(array, start, q - 1)
        quicksort(array, q + 1, end)


if __name__ == "__main__":
    t = np.random.rand(100000)
    t1 = time.clock()
    quicksort(t, 0, len(t) - 1)
    t2 = time.clock()
    print(t2 - t1)