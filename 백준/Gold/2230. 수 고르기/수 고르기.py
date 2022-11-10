import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
nums = [int(input().strip()) for _ in range(n)]
nums.sort()

st, en = 0, 0
answer = float('inf')
while(en < n and st < n):
    if(nums[en] - nums[st] < m): en += 1
    else:
        answer = min(answer, nums[en] - nums[st])
        st += 1
print(answer)