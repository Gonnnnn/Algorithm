import sys
sys.setrecursionlimit(1_000_000 + 1)

input = sys.stdin.readline
N = int(input())
treeTable = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split(' '))
    treeTable[u].append(v)
    treeTable[v].append(u)
visited = [False for _ in range(N + 1)]

answer = 0
def solve(person, treeTable):
    global answer
    visited[person] = True

    isEarlyAdaptor = False
    for friend in treeTable[person]:
        if visited[friend]: continue
        isFriendEarlyAdaptor = solve(friend, treeTable)
        isEarlyAdaptor = isEarlyAdaptor or not isFriendEarlyAdaptor
    if isEarlyAdaptor: answer += 1
    return isEarlyAdaptor
solve(1, treeTable)
print(answer)