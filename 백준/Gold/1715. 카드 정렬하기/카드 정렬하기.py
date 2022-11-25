import sys
import heapq

input = sys.stdin.readline
num = int(input())
cards = []
for i in range(num):
  cards.append(int(input()))

result = 0
heapq.heapify(cards)
while(len(cards) >= 2):
  temp = heapq.heappop(cards) + heapq.heappop(cards)
  result += temp
  heapq.heappush(cards, temp)

print(result)