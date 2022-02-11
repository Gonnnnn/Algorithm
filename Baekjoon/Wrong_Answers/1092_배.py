# 문제
# 지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다. 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

# 각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 각 크레인의 무게 제한이 주어진다. 이 값은 1,000,000보다 작거나 같다. 셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다. 넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다. 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
cranes.sort()
boxes.sort()

# 크레인이 2 2 2 2 10
# 박스가 2 2 2 2  2 2 2 2   10 10과 같은 경우 최소 시간을 구하지 못한다.
if cranes[-1] >= boxes[-1]:
  # 남은 박스들을 옮길 수 있는 크레인들 중 가장 무게 제한이 낮은 크레인
  idx_crane = 0
  # 옮겨야 할 박스
  idx_box = 0
  result = 0
  while(len(boxes) > idx_box):
    boxes_to_move = 0
    for i in range(idx_crane, len(cranes)):
      if cranes[i] >= boxes[idx_box]:
        idx_crane = i
        break
    j = idx_crane

    while(boxes_to_move < len(cranes[idx_crane:]) and len(boxes) > idx_box and j < len(cranes)):
      if boxes[idx_box] <= cranes[j]:
        boxes_to_move += 1
        idx_box += 1
      j += 1

    result += 1    

  print(result)
else:
  print(-1)