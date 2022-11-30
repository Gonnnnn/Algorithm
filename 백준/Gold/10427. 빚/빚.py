import sys
from collections import defaultdict

input = sys.stdin.readline

def solve(N, li):
    result = 0
    for windowSize in range(1, N + 1):
        tempTotal = sum(li[:windowSize])
        tempMin = li[windowSize - 1] * windowSize - tempTotal
        for start in range(1, N - windowSize + 1):
            tempTotal = tempTotal - li[start - 1] + li[start + windowSize - 1]
            moneyToPayBack = li[start + windowSize - 1] * windowSize
            tempMin = min(tempMin, moneyToPayBack - tempTotal)
        result += tempMin
    return result    

T = int(input())
for _ in range(T):
    li = list(map(int, input().split()))
    N = li[0]
    li = li[1:]
    li.sort()

    print(solve(N, li))