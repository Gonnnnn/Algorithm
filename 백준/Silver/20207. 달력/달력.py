import sys

input = sys.stdin.readline
N = int(input())
height = [0 for _ in range(365 + 1)]
for _ in range(N):
    S, E = map(int, input().split(' '))
    for i in range(S, E + 1):
        height[i] += 1
        
answer = 0
Max = 0
length = 0
height.append(0)
for h in height:
    if h == 0:
        answer += length * Max
        Max, length = 0, 0
        continue
    Max = max(Max, h)
    length += 1
print(answer)