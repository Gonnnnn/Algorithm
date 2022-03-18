import sys
input = sys.stdin.readline

# 세로, 가로
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 왼쪽 위부터 시작한다.
# 테트로미노마다 한 칸을 기준으로 회전하는 경우도 경우의 수로 포함시킨다.
# 해당 칸을 기준으로 테트로미노를 놓을 수 있는지 확인하고, 놓을 수 있다면 놓는다.
# 놓을 때마다 최댓값과 비교하고 최댓값보다 크면 최댓값을 갱신한다.

# rotate하는 함수를 구현할 수도 있었다.
# y, x좌표를 각각 -x, y로 바꿔주면 된다.

# 1번 블럭
tet1 = [[0, 0], [0, 1], [0, 2], [0, 3]]
tet2 = [[0, 0], [1, 0], [2, 0], [3, 0]]
# 2번 블럭
tet3 = [[0, 0], [0, 1], [1, 0], [1, 1]]
# 3번 블럭
tet4 = [[0, 0], [1, 0], [2, 0], [2, 1]]
tet5 = [[0, 0], [0, 1], [0, 2], [1, 0]]
tet6 = [[0, 0], [0, 1], [1, 1], [2, 1]]
tet7 = [[0, 2], [1, 0], [1, 1], [1, 2]]
# 3번 블럭 대칭
tet8 = [[2, 0], [0, 1], [1, 1], [2, 1]]
tet9 = [[0, 0], [1, 0], [1, 1], [1, 2]]
tet10 = [[0, 0], [1, 0], [2, 0], [0, 1]]
tet11 = [[0 ,0], [0, 1], [0, 2], [1, 2]]
# 4번 블럭
tet12 = [[0, 0], [1, 0], [1, 1], [2, 1]]
tet13 = [[0, 1], [0, 2], [1, 0], [1, 1]]
# 4번 블럭 대칭
tet14 = [[0, 1], [1, 1], [1, 0], [2, 0]]
tet15 = [[0, 0], [0, 1], [1, 1], [1, 2]]
# 5번 블럭
tet16 = [[0, 0], [0, 1], [0, 2], [1, 1]]
tet17 = [[0, 1], [1, 1], [2, 1], [1, 0]]
tet18 = [[1, 0], [1, 1], [1, 2], [0, 1]]
tet19 = [[0, 0], [1, 0], [2, 0], [1, 1]]
tets = [tet1, tet2, tet3, tet4, tet5, tet6, tet7, tet8, tet9, tet10, tet11, tet12, tet13, tet14, tet15, tet16, tet17, tet18, tet19]

# structure = []
# # 1번 idx 0
# structure.append([[0, 0], [0, 1], [0, 2], [0, 3]])
# # idx 1
# structure.append([[0, 0], [1, 0], [2, 0], [3, 0]])
# # 2번 idx 2
# structure.append([[0, 0], [0, 1], [1, 0], [1, 1]])
# # 3, 4번 idx 3
# temp = [[0, 0], [0, 1],
#         [1, 0], [1, 1],
#         [2, 0], [2, 1]]
# structure.append(temp)
# # 5번 idx 4
# temp = [[0, 0], [0, 1], [0, 2],
#         [1, 0], [1, 1], [1, 2],
#         [2, 0], [2, 1], [2, 2]]
# structure.append(temp)
# # tet_n = [structure, idx1, idx2, idx3, idx4]
# tet1 = [0, 0, 1, 2, 3]
# tet2 = [1, 0, 1, 2, 3]
# tet3 = [2, 0, 1, 2, 3]
# tet4 = [3, 0, 2, 4, 5]
# # 이런식으로도 가능

def calc(tet, y, x):
  global N, M
  Sum = 0
  for dy, dx in tet:
    ny = y + dy
    nx = x + dx
    if ny < 0 or N <= ny or nx < 0 or M <= nx:
      return 0
    Sum += Map[ny][nx]
  return Sum

result = 0
for tet in tets:
  for y in range(N):
    for x in range(M):
      temp = calc(tet, y, x)
      if temp == 0:
        break
      result = max(result, temp)
    
print(result)