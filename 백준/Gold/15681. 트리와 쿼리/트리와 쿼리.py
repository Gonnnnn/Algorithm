import sys
sys.setrecursionlimit(100_000 + 1)

input = sys.stdin.readline
N, R, Q = map(int, input().split(' '))

table = [[] for _ in range(N + 1)]
for _ in range(N-1):
    U, V = map(int, input().split(' '))
    table[U].append(V)
    table[V].append(U)
d = [1 for _ in range(N + 1)]
visited = [False for _ in range(N+ 1)]

def updateSubNodeNumber(node):
    if visited[node]: return 0
    visited[node] = True
    for children in table[node]:
        d[node] += updateSubNodeNumber(children)
    return d[node]

updateSubNodeNumber(R)
for _ in range(Q):
    print(d[int(input())])