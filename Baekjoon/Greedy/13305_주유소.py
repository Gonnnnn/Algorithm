num = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min = price[0]
result = 0

for i in range(1, len(price)):
  result += min * distance[i - 1]

  if(min > price[i]):
    min = price[i]

print(result)