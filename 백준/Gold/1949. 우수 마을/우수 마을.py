import sys
sys.setrecursionlimit(10_000)

input = sys.stdin.readline
N = int(input())
populations = [0] + list(map(int, input().split()))
tree_table = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree_table[u].append(v)
    tree_table[v].append(u)
# 우수 마을 총합 [해당 마을이 우수 마을일 때, 해당 마을이 우수 마을이 아닐 때]
great_town_table = [[population, 0] for population in populations]
visited = [False for _ in range(N + 1)]

def solve(town):
    visited[town] = True
    for neighbor_town in tree_table[town]:
        if visited[neighbor_town]: continue
        solve(neighbor_town)
        great_town_table[town][0] += great_town_table[neighbor_town][1]
        great_town_table[town][1] += max(great_town_table[neighbor_town])

solve(1)
print(max(great_town_table[1]))