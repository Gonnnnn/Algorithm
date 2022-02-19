N = int(input())
houses = list(map(int, input().split()))
houses.sort()
houses.append(houses[-1] + 1)
Sum = sum(houses) - houses[-1]

count = 1
total_distance = 1e+10
antena = 0
for i in range(N):
  if houses[i+1] == houses[i]:
    count += 1
  else:
    Sum -= 2*houses[i]*count
    temp = Sum - (N-2*(i+1))*houses[i]
    if temp < total_distance:
      total_distance = temp
      antena = houses[i]
    count = 1

print(antena)

# 그냥 가운데꺼 뽑으면 되긴한다.