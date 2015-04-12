from pprint import pprint

__author__ = 'shen'
from exp2.findnlgn import getpoint
from exp2.findnlgn import countdistance
import arrow


def findn2(l):
    templength = countdistance(l[0], l[1])
    for i in range(len(l) - 1):
        for j in range(i, len(l) - 1):
            if countdistance(l[i], l[j + 1]) < templength:
                temp = l[i], l[j + 1]
                templength = countdistance(temp[0], temp[1])
    pprint(temp)
    print(templength)


if __name__ == "__main__":
    t1 = arrow.now()
    # l = getpoint(500)

    l = ((1, 1), (1, 4), (1, 2), (1, 1.3))
    findn2(l)
    t2 = arrow.now()
    t = t2 - t1
    print(t)
