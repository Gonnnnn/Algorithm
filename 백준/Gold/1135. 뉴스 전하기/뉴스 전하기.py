import sys

input = sys.stdin.readline
N = int(input())
workers = list(map(int, input().split(' ')))

def getTreeTable(workers):
    treeTable = [[] for _ in range(N)]
    for i in range(N):
        for worker, boss in enumerate(workers):
            if boss == i: treeTable[i].append(worker)
    return treeTable

def solve(boss):
    timeTakenOfSubWorkers = []
    for worker in treeTable[boss]:
        solve(worker)
        timeTakenOfSubWorkers.append(timeTaken[worker])
    timeTakenOfSubWorkers.sort(reverse=True)
    maxTimeTaken = 0
    for index, timeTakenOfSubWorker in enumerate(timeTakenOfSubWorkers):
        maxTimeTaken = max(maxTimeTaken, timeTakenOfSubWorker + index + 1)
    timeTaken[boss] = maxTimeTaken
    return

treeTable = getTreeTable(workers)
timeTaken = [0 for _ in range(N)]
solve(0)
print(timeTaken[0])