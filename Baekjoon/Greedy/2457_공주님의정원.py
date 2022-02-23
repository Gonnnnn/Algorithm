import sys
input = sys.stdin.readline

N = int(input())
flowers = []
for _ in range(N):
  li = list(map(int, input().split()))
  flowers.append([li[0] * 100 + li[1], li[2] * 100 + li[3]])
flowers.sort()

# 심는게 확정된 꽃의 지는 날짜
end = 100
# 심을지 안심을지 보류중인 애들 중 가장 최선 책!
# 심는게 확정된 꽃의 지는 날짜보다 일찍 심는 애들 중에서 가장 늦게 지는 꽃이 temp가 된다. 앞의 꽃과 며칠이 겹치든 일단 그냥 제일 늦게 지는 꽃을 고르는게 무!적!권! 이득이기 때문.
temp = [100, 301]
result = 0

for flower in flowers:
  # temp가 1130보다 늦게 진다면 거기서 마쳐도 된다. 탈출!
  if 1201 <= temp[1]:
    break
  # flower가 기존의 꽃이 지는 날짜보다 일찍 심어지면 temp 후보이다. 
  if flower[0] <= end:
    # 기존 temp보다 늦게 진다? 새로운 temp가 된다.
    if temp[1] < flower[1]:
      temp = flower
  else: # 기존 꽃이 지는 날짜보다 더 늦게 심어지는 꽃이 나왔다면?
    # 기존 temp가 지는 날짜보다는 일찍 심어져야 꽃이 심어져있는 날짜가 끊기지 않고 이어질 것이다. 만약  그렇다면 현재 temp를 심는 것으로 확정!해버리고 flower을 새 temp로 한다.

    # 제일 처음 end를 100으로 설정하고, temp를 [100, 301]로 설정함으로써 첫 flower는 301보다 일찍 심어진다면 바로 temp가 된다. 그게 아니라면 바로 break한 후 0을 print할 것
    if flower[0] <= temp[1]:
      result += 1
      end = temp[1]
      temp = flower
    # 기존 temp가 지는 날짜 보다 더 늦게 심어지면 중간에 공백 발생. 불가능
    else:
      result = 0
      break

# 위 반복문을 다 돌아도 마지막 temp가 1201보다 일찍 질 수도 있다. 그렇게 되면 0 출력
if temp[1] < 1201:
  print(0)
else:
  print(result)