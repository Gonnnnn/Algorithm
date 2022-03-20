N = int(input())
rooms = list(map(int, input().split()))
B, C = map(int, input().split())

result = N
for i in range(N):
  rooms[i] -= B
  if rooms[i] > 0:
    result += (rooms[i]-1)//C + 1

print(result)