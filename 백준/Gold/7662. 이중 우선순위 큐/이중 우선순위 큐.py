import sys
import heapq

def executeOperation(minHq, maxHq, deleted, op, number, i):
    if op == 'I':
        insertNumber(minHq, maxHq, number, i)
    elif op == 'D':
        if number == 1:
            deleteMaxNumber(maxHq, deleted)
        elif number == -1:
            deleteMinNumber(minHq, deleted)

def insertNumber(minHq, maxHq, number, i):
    heapq.heappush(minHq, (number, i))
    heapq.heappush(maxHq, (-1 * number, i))
    return

def deleteMaxNumber(maxHq, deleted):
    while(maxHq and maxHq[0][1] in deleted):
        heapq.heappop(maxHq)
    if maxHq:
        _, idx = heapq.heappop(maxHq)
        deleted.add(idx)
    return

def deleteMinNumber(minHq, deleted):
    while(minHq and minHq[0][1] in deleted):
        heapq.heappop(minHq)
    if minHq:
        _, idx = heapq.heappop(minHq)
        deleted.add(idx)
    return

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    minHq = []
    maxHq = []
    deleted = set()

    for i in range(k):
        op, number = input().strip().split(' ')
        executeOperation(minHq, maxHq, deleted, op, int(number), i)        

    while(minHq and minHq[0][1] in deleted):
        heapq.heappop(minHq)
    while(maxHq and maxHq[0][1] in deleted):
        heapq.heappop(maxHq)
    if minHq:
        print(f'{-1 * maxHq[0][0]} {minHq[0][0]}')
    else:
        print('EMPTY')
