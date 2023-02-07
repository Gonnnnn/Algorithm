import sys

def union(a, b):
    parentA = find(a)
    parentB = find(b)
    if parentA == parentB: return
    parents[parentA] = parentB

def find(node):
    root = node
    while(root != parents[root]):
        root = parents[root]
    while(node != parents[node]):
        parents[node] = root
        node = parents[node]
    return parents[node]

input = sys.stdin.readline
n, m = map(int, input().split(' '))
parents = [i for i in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, input().split(' '))
    if op == 0: union(a, b)
    else:
        parentA = find(a)
        parentB = find(b)
        if parentA == parentB:
            print("YES")
        else:
            print("NO")