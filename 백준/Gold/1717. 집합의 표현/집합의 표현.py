import sys
sys.setrecursionlimit(10**5)

def find(x):
    if x == p[x]:
        return p[x]
    p[x] = find(p[x])
    return p[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return
    if a < b:
        p[b] = a
    else:
        p[a] = b

input = sys.stdin.readline
n,m = map(int,input().split())

p = [i for i in range(0,n+1)]
for i in range(m):
    f,a,b = map(int,input().split())

    if f == 1: #find
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')

    else: #f == 0 union
        union(a,b)