import sys
import numpy as np

def inp(cf=int, vpl=1, s=" "):
    if vpl == 1: return cf(sys.stdin.readline().strip("\n"))
    else: return list(map(cf, sys.stdin.readline().strip("\n").split(s)))


def isOnLine(p,q,b):
    x1 = p[0]
    y1 = p[1]
    x2 = q[0]
    y2 = q[1]
    xb = b[0]
    yb = b[1]
    if x2 - x1 == 0:
        return x1 == xb
    else:
        return ((xb - x1) / (x2 - x1)) * (y2 - y1) + y1 == yb

ballons = []



testCases = inp()
for t in range(1, testCases+1):
    ballons.append(inp(int, 2))

ballons = np.array(ballons)

b1 = ballons[1]
b2 = ballons[5]
sv = b1
rv = b2 - b1

for ballon in ballons:
    print(isOnLine(sv, rv, ballon))