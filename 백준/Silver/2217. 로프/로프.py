from re import X
import sys
input = sys.stdin.readline

n = int(input().strip())
ropes = [int(input().strip()) for _ in range(n)]
ropes.sort(reverse=True)

Max = 0
for i, rope in enumerate(ropes):
    if rope * (i + 1) > Max: Max = rope * (i + 1)
print(Max)