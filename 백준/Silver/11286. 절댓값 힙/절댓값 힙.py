import sys
import heapq

input = sys.stdin.readline
hq = []

def insertNumber(num):
    global hq
    heapq.heappush(hq, (abs(num), num))
    return

def deleteNumber():
    global hq
    if not hq:
        print(0)
        return

    _, num = heapq.heappop(hq)
    print(num)
    return

N = int(input().strip())
for _ in range(N):
    num = int(input().strip())
    if num == 0:
        deleteNumber()
    else:
        insertNumber(num)