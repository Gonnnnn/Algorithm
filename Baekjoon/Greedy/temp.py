import sys
input = sys.stdin.readline
doc = int(input())

a = [[[0] for _ in range(doc)] for _ in range(doc)]

for i in range(doc):
  print(a[i])