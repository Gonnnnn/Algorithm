import sys
sys.setrecursionlimit(100_000)

def solve(building):
    visited[building] = True
    maxTimeTaken = 0
    for dependency in dependencyTree[building]:
        if not visited[dependency]: solve(dependency)
        maxTimeTaken = max(maxTimeTaken, time[dependency])
    time[building] += maxTimeTaken

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    dependencyTree = [[] for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        # Y를 짓기 위해 X가 필요함
        dependencyTree[Y].append(X)
    W = int(input())
    visited = [False for _ in range(N + 1)]
    solve(W)
    print(time[W])