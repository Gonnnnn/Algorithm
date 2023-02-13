import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
print(sorted(Counter([input().strip() for _ in range(N)]).items(), key=lambda x:(-1*x[1], x))[0][0])