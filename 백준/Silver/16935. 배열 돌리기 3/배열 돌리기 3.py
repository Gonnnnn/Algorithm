import sys

input = sys.stdin.readline
N, M, R = map(int, input().split(' '))
nums = [list(map(int, input().split(' '))) for _ in range(N)]
ops = list(map(int, input().split(' ')))

def solve(op, nums):
    if op == 1:
        return one(nums)
    elif op == 2:
        return two(nums)
    elif op == 3:
        return three(nums)
    elif op == 4:
        return four(nums)
    elif op == 5:
        return five(nums)
    elif op == 6:
        return six(nums)

def one(nums):
    M, N = len(nums[0]), len(nums)
    newNums = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            newNums[i][j] = nums[N-1-i][j]
    return newNums

def two(nums):
    M, N = len(nums[0]), len(nums)
    newNums = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            newNums[i][j] = nums[i][M-1-j]
    return newNums

def three(nums):
    M, N = len(nums[0]), len(nums)
    newNums = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(N):
        for j in range(M):
            newNums[j][N - 1 - i] = nums[i][j]
    return newNums

def four(nums):
    M, N = len(nums[0]), len(nums)
    newNums = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(N):
        for j in range(M):
            newNums[M - 1 - j][i] = nums[i][j]
    return newNums

def five(nums):
    M, N = len(nums[0]), len(nums)
    newNums = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            newNums[i][j + M//2] = nums[i][j]
    for i in range(N//2):
        for j in range(M//2, M):
            newNums[i + N//2][j] = nums[i][j]
    for i in range(N//2, N):
        for j in range(M//2, M):
            newNums[i][j - M//2] = nums[i][j]
    for i in range(N//2, N):
        for j in range(M//2):
            newNums[i - N//2][j] = nums[i][j]
    return newNums

def six(nums):
    M, N = len(nums[0]), len(nums)
    newNums = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            newNums[i + N//2][j] = nums[i][j]
    for i in range(N//2):
        for j in range(M//2, M):
            newNums[i][j - M//2] = nums[i][j]
    for i in range(N//2, N):
        for j in range(M//2, M):
            newNums[i - N//2][j] = nums[i][j]
    for i in range(N//2, N):
        for j in range(M//2):
            newNums[i][j + M//2] = nums[i][j]
    return newNums

for op in ops:
    nums = solve(op, nums)

for row in nums:
    print(' '.join(map(str, row)))