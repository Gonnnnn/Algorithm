import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split(' '))
    houses = list(map(int, input().split(' ')))
    total = sum(houses[:M])
    if N == M:
        if total < K: print(1)
        else: print(0)
    else:
        answer = 0
        for index, house in enumerate(houses):
            if total < K:
                answer += 1
            total -= house
            total += houses[(index + M) % N]
        print(answer)