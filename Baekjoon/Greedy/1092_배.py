# 문제
# 지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다. 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

# 각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 각 크레인의 무게 제한이 주어진다. 이 값은 1,000,000보다 작거나 같다. 셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다. 넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다. 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.

import heapq as hq

N = int(input())
limit = list(map(int, input().split()))
M = int(input())
weights = list(map(int, input().split()))
limit.sort(reverse=True)
for i in range(len(weights)):
  weights[i] *= -1
hq.heapify(weights)

if -1 * weights[0] > limit[0]:
  print(-1)
else:
  result = 0
  while(weights):
    idx = 0
    bag = []
    while(weights):
      weight = hq.heappop(weights)
      if -1 * weight <= limit[idx]:
        idx += 1
        if idx == len(limit):
          break
      else:
        bag.append(weight)

    weights = weights + bag
    hq.heapify(weights)

    result += 1

  print(result)