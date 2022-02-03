# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  first, second = map(int, input().split())
  graph[first].append(second)
  graph[second].append(first)

visited = [False] * (N+1)
to_visit = [V]

while(to_visit):
  new_one = to_visit.pop()
  if not visited[new_one]:
    visited[new_one] = True
    print(new_one, end=' ')
    graph[new_one].sort(reverse=True)
    for node in graph[new_one]:
      if not visited[node]:
        to_visit.append(node)

print()

visited = [False] * (N+1)
to_visit = deque([V])

while(to_visit):
  new_one = to_visit.popleft()
  if not visited[new_one]:
    visited[new_one] = True
    print(new_one, end=' ')
    graph[new_one].sort()
    for node in graph[new_one]:
      if not visited[node]:
        to_visit.append(node)

# 좋은 구현이라고 생각한다. 이 방법을 적용하는 것도 앞으로 연습하자. 익숙하지 않은 방법에 익숙해질 필요가 있다.
# from collections import deque

# def DFS(graph, root):
#     visited = []
#     stack = [root]

#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n]) - set(visited))
#                 temp.sort(reverse=True)
#                 stack += temp
#     return " ".join(str(i) for i in visited)

# def BFS(graph, root):
#     visited = []
#     queue = deque([root])

#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n]) - set(visited))
#                 temp.sort()
#                 queue += temp
#     return " ".join(str(i) for i in visited)

  
# graph = {}
# n = input().split(' ')
# node, edge, start = [int(i) for i in n]
# for i in range(edge):
#     edge_info = input().split(' ')
#     n1, n2 = [int(j) for j in edge_info]
#     if n1 not in graph:
#         graph[n1] = [n2]
#     elif n2 not in graph[n1]:
#         graph[n1].append(n2)

#     if n2 not in graph:
#         graph[n2] = [n1]
#     elif n1 not in graph[n2]:
#         graph[n2].append(n1)

# print(DFS(graph, start))
# print(BFS(graph, start))


# 다른 구현. BFS에서 queue에 넣어줌과 동시에 바로 visit처리를 하면 중복으로 들어가는 것을 미연에 방지할 수 있다.
# 쓰고 보니까 이거 옛날에 생각해봤던것 같다
# 당연히 DFS는 이렇게 하면 안될 것이다.
# def DFS(n):
#     print(n,end=' ')
#     visit[n]=1
#     for i in graph[n]:
#         if visit[i]==0:
#             DFS(i)

# def BFS(n):
#     q=deque()
#     q.append(n)
#     visit[n]=1
#     while q:
#         n=q.popleft()
#         print(n,end=' ')
#         for i in graph[n]:
#             if visit[i]==0:
#                 q.append(i)
#                 visit[i]=1