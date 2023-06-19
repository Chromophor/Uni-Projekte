import sys

def inp(cf=int, vpl=1, s=" "):
    if vpl == 1: return cf(sys.stdin.readline().strip("\n"))
    else: return list(map(cf, sys.stdin.readline().strip("\n").split(s)))

def testCase(t):
    s, ns = sys.stdin.readline().strip("\n").split(" ")
    n = int(ns)






testCases = inp()
for t in range(1, testCases+1):
    testCase(t)
