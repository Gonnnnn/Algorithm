import sys
input = sys.stdin.readline
n, s = map(int, input().strip().split(' '))
nums = list(map(int, input().strip().split(' ')))
visited = [False for _ in range(n)]
cnt = 0

def solve(k, Sum):
    global n, s, cnt
    if k == n:
        if s == Sum:
            cnt += 1
        return
    solve(k + 1, Sum)
    solve(k + 1, Sum + nums[k])
   
if s == 0: cnt -= 1
solve(0, 0)
print(cnt)