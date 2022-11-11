import sys
input = sys.stdin.readline

n, s = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
st, en = 0, 0
total = nums[en]
gap = n + 1

while(st < n and en < n):
    if total >= s:
        gap = min(gap, en - st + 1)
        total -= nums[st]
        st += 1
        if st > en and st < n:
            en = st
            total += nums[en]
    else:
        en += 1
        if en < n:
            total += nums[en]
print(gap if gap < n + 1 else 0)