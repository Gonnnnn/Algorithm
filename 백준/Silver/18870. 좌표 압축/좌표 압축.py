import sys
input = sys.stdin.readline

n = int(input().strip())
li = list(map(int, input().strip().split(' ')))
sortedLi = sorted(li)

cleared = sorted(list(set(sortedLi)))
idxDict = {}
for idx, num in enumerate(cleared):
    idxDict[num] = idx
for num in li:
    print(idxDict[num], end=' ')