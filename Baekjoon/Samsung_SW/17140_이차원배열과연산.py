r, c, k = map(int, input().split())
r -= 1
c -= 1
A = [list(map(int, input().split())) for _ in range(3)]

def op(A, C):
  max_len = 0
  temp_A = []

  if C:
    A = transform(A)

  for row in A:
    nums = {}
    for i, num in enumerate(row):
      if i == 100:
        break
      if num == 0:
        continue
      if not num in nums:
        nums[num] = 1
      else:
        nums[num] += 1
    
    li = []
    for num in nums:
      li.append([num, nums[num]])
    li.sort(key=lambda x:(x[1], x[0]))

    temp = []
    for num, count in li:
      temp.append(num)
      temp.append(count)

    if len(temp) > max_len:
      max_len = len(temp)

    temp_A.append(temp)

  for row in temp_A:
    if len(row) < max_len:
      while(True):
        if len(row) == max_len:
          break
        row.append(0)

  if C:
    temp_A = transform(temp_A)
  
  return temp_A

def transform(A):
  temp_A = []
  for j in range(len(A[0])):
    temp = []
    for i in range(len(A)):
      temp.append(A[i][j])
    temp_A.append(temp)
  return temp_A

time = 0
while(True):
  if r < len(A) and c < len(A[0]):
    if A[r][c] == k:
      break
  if time == 100:
    time += 1
    break

  C = True
  if len(A) >= len(A[0]):
    C = False
    
  A = op(A, C)
  
  time += 1

if time == 101:
  time = -1
print(time)