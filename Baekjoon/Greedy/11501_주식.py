import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  chart = list(map(int, input().split()))

  Max = 0
  revenue = 0

  for idx in range(len(chart)-1,-1,-1):
    if chart[idx] < Max:
      revenue += Max - chart[idx]
    else:
      Max = chart[idx]
  
  print(revenue)