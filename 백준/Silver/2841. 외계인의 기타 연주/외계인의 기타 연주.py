import sys
import heapq

input = sys.stdin.readline
# 음의 개수, 프렛 수
N, P = map(int, input().split(' '))
pressed = [[0] for _ in range(N + 1)]
answer = 0
for _ in range(N):
    stringNum, fret = map(int, input().split(' '))
    # 최악의 경우 해당 줄에서 눌린 fret을 다 떼어내야한다고 하더라도, 이를 모두 눌러가는데 그만큼의 상수 시간이 걸린다.
    while(fret < pressed[stringNum][-1]):
        pressed[stringNum].pop()
        answer += 1
    if pressed[stringNum][-1] == fret: continue
    pressed[stringNum].append(fret)
    answer += 1
print(answer)