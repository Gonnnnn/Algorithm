import sys
input = sys.stdin.readline

n = int(input().strip())
li = list(map(int, input().strip().split(' ')))
m = int(input().strip())
nums = list(map(int, input().strip().split(' ')))

# 삽입했을 때 오름차순이 유지되는 가장 왼쪽 위치
def lowerBound(target):
    global n, li
    st, en = 0, n
    while(st != en):
        mid = (st + en) // 2
        midVal = li[mid]
        if midVal < target: st = mid + 1
        else: en = mid
    return st

# 삽입했을 때 오름차순이 유지되는 가장 오른쪽 위치
def upperBound(target):
    global n, li
    st, en = 0, n
    while(st != en):
        mid = (st + en) // 2
        midVal = li[mid]
        if midVal <= target: st = mid + 1
        else: en = mid
    return st

li.sort()
answer = []
for num in nums:
    answer.append(upperBound(num) - lowerBound(num))
print(' '.join(str(e) for e in answer))