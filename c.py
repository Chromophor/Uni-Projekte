import sys, math

def inp(cf=int, vpl=1, s=" "):
    if vpl == 1: return cf(sys.stdin.readline().strip("\n"))
    else: return list(map(cf, sys.stdin.readline().strip("\n").split(s)))


planetsCount, trainsCount, holesCount = inp(int, 3)
holesIndecies = inp(int, 2)
trains = []
for t in range(trainsCount):
    trains.append(inp(int, 2))


def getCount(planet, target, currentCount):
    possibilties = []
    for t in trains:
        if t[0] == planet: possibilties.append(t[1])
    if target in possibilties: return currentCount+1
    lowestCount = float("inf")
    lowestPlanet = 0
    for p in possibilties:
        if getCount(p, target, currentCount+1) < lowestCount:
            lowestPlanet = p
    return getCount(lowestPlanet, target, currentCount+1)


fastest = getCount(1, planetsCount, 0)
for inh in holesIndecies:
    c = getCount(1, inh, 0)
    countSum = 0
    holes = holesIndecies.copy()
    holes.remove(inh)
    for outh in holes:
        countSum += c + getCount(outh, planetsCount, 0)
    countSum /= len(holes)
    if countSum < fastest: fastest = countSum

from fractions import Fraction
print(Fraction(fastest))