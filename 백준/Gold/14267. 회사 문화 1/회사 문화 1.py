import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split(' '))
bossTable = [0] + list(map(int, input().split(' ')))

def getTreeTable(bossTable):
    treeTable = [[] for _ in range(n + 1)]
    for worker, boss in enumerate(bossTable[2:]):
        treeTable[boss].append(worker + 2)
    return treeTable

compliment = [0 for _ in range(n + 1)]
for _ in range(m):
    i, w = map(int, input().split(' '))
    compliment[i] += w
treeTable = getTreeTable(bossTable)

q = deque([1])
while(q):
    boss = q.popleft()
    for subWorker in treeTable[boss]:
        compliment[subWorker] += compliment[boss]
        q.append(subWorker)

print(' '.join(list(map(str, compliment[1:]))))