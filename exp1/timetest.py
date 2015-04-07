__author__ = 'shen'
import numpy as np
import time
from exp1.quicksort import quicksort
from exp1.bubblesort import bubblesort
import arrow


def getRandomArray(n):
    """
    Construct a random array for sorting
    :param n: the number of elements in array
    :return: a random array whose number of element is set by n
    """
    return np.random.rand(n)


if __name__ == "__main__":
    number = 1000, 5000, 10000
    for i in number:
        t1 = arrow.now()
        array = getRandomArray(i)
        quicksort(array, 0, len(array) - 1)
        t2 = arrow.now()
        t = t2 - t1
        print("在{0}个数据下，{1}效率为{2} 秒".format(i, quicksort.__name__, t))
