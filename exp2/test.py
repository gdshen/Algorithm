from pprint import pprint
from exp2.findnlgn import findnlgn
from exp2.findn2 import findn2
from exp2.findnlgn import getpoint

if __name__ == "__main__":
    l1 = getpoint(10)
    l2 = l1.copy()

    findn2(l1)
    findnlgn(l2)