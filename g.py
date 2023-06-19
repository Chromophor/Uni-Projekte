import sys

def inp(cf=int, vpl=1, s=" "):
    if vpl == 1: return cf(sys.stdin.readline().strip("\n"))
    else: return list(map(cf, sys.stdin.readline().strip("\n").split(s)))
'''
def dasDauert(countdown):
    d = {}
    for n in range(10):
        d[n] = 0
    for c in range(countdown, -1, -1):
        for n in range(10):
            brauchenWir = str(c).count(str(n))
            if brauchenWir > d[n]: d[n] = brauchenWir
    count = 0
    for n in range(10):
        count += d[n]
    return count
'''

def testCase(t):
    countdown = inp()
    if countdown < 10:
        print(countdown+1)
    else:
        count = 10
        for n in range(1, 10):
            schnappzahl = len(str(countdown)) * str(n)
            if int(schnappzahl) <= countdown:
                count += len(schnappzahl)-1
            else:
                count += len(schnappzahl)-2
        add = len(str(countdown))-2
        if add < 0: add = 0
        count += add
        print(count)

testCase(0)
'''
testCases = inp()
for t in range(1, testCases+1):
    testCase(t)

'''