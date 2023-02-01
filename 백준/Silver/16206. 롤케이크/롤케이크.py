import sys

input = sys.stdin.readline
N, M = map(int, input().split(' '))
cakes = sorted(list(map(int, input().split(' '))))

cut = 0
answer = 0
for index, cake in enumerate(cakes):
    if cake % 10 != 0: continue
    cut += (cake // 10) - 1
    answer += cake // 10
    cakes[index] = 0
    if cut < M: continue
    if cut > M:
        answer -= cut - M + 1
    break
if cut < M:
    for cake in cakes:
        if cake < 10: continue
        cut += cake // 10
        answer += cake // 10
        if cut < M: continue
        if cut > M:
            answer -= cut - M
        break
print(answer)