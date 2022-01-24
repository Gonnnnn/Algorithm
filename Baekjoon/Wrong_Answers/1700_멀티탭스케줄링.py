# 문제
# 기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다. 준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다. 그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.

# 예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면, 

# 키보드
# 헤어드라이기
# 핸드폰 충전기
# 디지털 카메라 충전기
# 키보드
# 헤어드라이기
# 키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다. 

# 입력
# 첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다. 

# 출력
# 하나씩 플러그를 빼는 최소의 횟수를 출력하시오.



# 꼭 다시 풀어보자! 이거 문제가 낫밷
import sys
import heapq as hq
input = sys.stdin.readline

N, K = map(int, input().split())
times = [0] * (K+1)
temp_list = list(map(int, input().split()))

devices = [temp_list[0]]
times[temp_list[0]] += 1
for i in range(1, len(temp_list)):
  if (temp_list[i] != temp_list[i-1]):
    # 각 상품마다 사용하는 횟수 기록
    times[temp_list[i]] += 1
    # 연속해서 사용하는 물품들은 한번으로 묶어주기
    devices.append(temp_list[i])

times[devices[0]] -= 1
plugged = [[times[devices[0]], devices[0]]]
count = 0

for i in range(1, len(devices)):
  temp = [times[devices[i]], devices[i]]
  if temp in plugged:
    bags = []
    for j in range(len(plugged)):
      bag = hq.heappop(plugged)
      if bag[1] == temp[1]:
        break
      else:
        bags.append(bag)
    for k in range(len(bags)):
      hq.heappush(plugged, bags[k])
    times[devices[i]] -= 1
    temp[0] -= 1
    hq.heappush(plugged, temp)    
  else:
    times[devices[i]] -= 1
    temp[0] -= 1 
    if len(plugged) < N:
      hq.heappush(plugged, temp)
    else:
      hq.heappop(plugged)
      hq.heappush(plugged, temp)
      count += 1

print(count)




