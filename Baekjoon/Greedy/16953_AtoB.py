# 문제
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

# 입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

# 출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def search(x, goal, count):
  
  if(x >= goal):
    return x, count

  double, db_cnt = search(x*2, goal, count+1)
  plus_one, po_cnt = search(x*10 +1, goal, count+1)

  if double == goal:
    return double, db_cnt
  elif plus_one == goal:
    return plus_one, po_cnt

  return 0, -2

_, result = search(a, b, 0)
print(result + 1)

# another answer
# import sys
# input = sys.stdin.readline

# # 파싱
# n, m = map(int, input().split())

# # 역체크
# count = 1
# while n < m:
#     if str(m)[-1] == "1":
#         m = int(str(m)[:-1])
#         count += 1
#     else:
#         if m % 2 == 0:
#             m = m // 2
#             count += 1
#         else:
#             break

# # 결과 출력
# if n == m:
#     print(count)
# else:
#     print(-1)

# a,b = map(int, input().split())
# cnt = 1


# if __name__ == "__main__":
#     while True:
#         if b == a:
#             break
#         elif a > b:
#             cnt = -1
#             break
#         elif b % 10 == 1:
#             b //= 10
#             cnt += 1
#         elif b % 2 == 0:
#             b //= 2
#             cnt += 1
#         else:
#             cnt = -1
#             break
#     print(cnt)

