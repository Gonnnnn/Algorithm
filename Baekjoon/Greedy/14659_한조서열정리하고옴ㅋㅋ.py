N = int(input())

hills = list(map(int, input().split()))

result = 0
Max = 0
count = 0

for hill in hills:
  if hill > Max:
    Max = hill
    count = 0
  else:
    count += 1
  result = max(result, count)

print(result)