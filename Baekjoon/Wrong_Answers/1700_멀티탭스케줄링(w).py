from collections import Counter

# 멀티탭 구멍 수, 전기 용품의 총 사용횟수
N, K = map(int, input().split())
devices = list(map(int, input().split()))

counts = Counter(devices)
# counts = [0]*(K+1)
# for device in devices:
#   counts[device] += 1

outlet = {}
result = 0
for i, device in enumerate(devices):
  counts[device] -= 1
  if len(outlet) < N:
    outlet[device] = counts[device]
  else:
    if device in outlet:
      outlet[device] -= 1
    else:
      idx = -1
      key = -1
      devices_copy = devices[i+1:]
      for temp_key in outlet:
        if counts[temp_key] == 0:
          key = temp_key
          break
        temp_idx = devices_copy.index(temp_key)
        if idx < temp_idx:
          idx = temp_idx
          key = temp_key

      del outlet[key]
      outlet[device] = counts[device]
      result += 1
print(result)