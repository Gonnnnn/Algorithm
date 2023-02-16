import sys

input = sys.stdin.readline
number = input().strip()
print(''.join(sorted(number, reverse=True)))