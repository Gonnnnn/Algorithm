from collections import deque

n, targetN = map(int, input().split(' '))
targets = list(map(int, input().split(' ')))
q = deque([i for i in range(1, n+1)])
answer = 0

for target in targets:
    k = q.index(target) + 1
    if k == 1:
        q.popleft()
    else:
        if k - 1 >= len(q) - k + 1:
            itr = len(q) - k + 1
            for _ in range(itr):
                temp = q.pop()
                q.appendleft(temp)
            q.popleft()
            answer += itr
        else:
            itr = k - 1
            for _ in range(itr):
                temp = q.popleft()
                q.append(temp)
            q.popleft()
            answer += itr
print(answer)