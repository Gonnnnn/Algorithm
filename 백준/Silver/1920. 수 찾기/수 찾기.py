import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
m = int(input().strip())
nums = list(map(int, input().strip().split(' ')))

def binarySearch(target):
    global n, a
    st, en = 0, n-1
    while(st <= en):
        mid = (st + en) // 2
        midVal = a[mid]
        if midVal == target: return True
        elif midVal < target: st = mid + 1
        else: en = mid - 1
    return False

a.sort()
for i in range(m):
    if binarySearch(nums[i]): print(1)
    else: print(0)