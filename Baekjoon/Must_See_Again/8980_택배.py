# 45분

# 마을에서 배송할 물건 박스에 넣어보냄
# 본부에서는 박스를 보내는 마을번호,박스를 받는 마을번호, 보낼 박수 개수를 알고있음

# 트럭에 박스 ㅈㄴ 담아야함

# 박스는 받는 마을에서만 내림. 트럭은 직진만함 후진없음 ㅇㅇ. 박스 다 배송할필요 없음 ㅇㅇㅇ

import sys
input = sys.stdin.readline

# 마을 수, 트럭 용량
N, C = map(int, input().split())
M = int(input())
requests = [list(map(int, input().split())) for _ in range(M)]
requests.sort(key=lambda x:x[1])

truck = [C]*(N+1)

result = 0
for request in requests:
  
  available_space = min(truck[request[0]:request[1]])
  boxes_to_load = min(request[2], available_space)
  for i in range(request[0], request[1]):
    truck[i] -= boxes_to_load
  result += boxes_to_load

print(result)
  
# 버려야할걸 제차 일일히 확인하고 버리고 새로운 것을 담는 과정은 실제 현실에서 괜찮을 수 있지만, 알고리즘으로서 작성하기 까다롭고, 고려할 조건이 매우 방대해질 수 있다.
# 애초에 특정 기준을 가지고 받거나, 받지 않거나로 나누는게 현명하다