import sys
from itertools import permutations

input = sys.stdin.readline
A, B = input().strip().split(' ')
B = int(B)
answer = -1
for numberString in permutations(A):
    if numberString[0] == '0': continue
    number = int(''.join(numberString))
    if number < B:
        answer = max(answer, number)
print(answer)