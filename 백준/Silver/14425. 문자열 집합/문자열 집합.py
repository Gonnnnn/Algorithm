import sys

input = sys.stdin.readline
N, M = map(int, input().split())
S = set([input().strip() for _ in range(N)])
answer = 0
for _ in range(M):
    if input().strip() in S: answer += 1
print(answer)