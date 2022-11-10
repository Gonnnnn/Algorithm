import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = [int(input().strip()) for _ in range(n)]
nums.sort()

def binarySearch(st, target):
    en = len(nums)
    while(st < en):
        mid = (st + en) // 2
        if nums[mid] < target: st = mid + 1
        else: en = mid
    return st

answer = float('inf')
for i, num in enumerate(nums):
    target = m + num
    idx = binarySearch(i, target)
    if(idx == len(nums)): continue
    answer = min(answer, nums[idx] - num)

print(answer)