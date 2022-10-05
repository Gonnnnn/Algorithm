import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split(' '))
randNums = list(map(int, input().strip().split(' ')))
randNums.sort()

visited = [False for _ in range(n + 1)]
def solve(nums):
    global n
    if len(nums) == m:
        print(' '.join(list(map(str, nums))))
        return

    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        nums.append(randNums[i])
        solve(nums)
        nums.pop()
        visited[i] = False

    return
solve([])