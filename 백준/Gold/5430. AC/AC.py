from collections import deque


t = int(input())
for _ in range(t):
    forward = True
    fail = False

    funcs = list(input())
    n = int(input())
    li = input()[1:-1].split(',')
    if n == 0:
        li = []
    li = deque(li)

    for func in funcs:
        if func == 'R':
            forward = not forward
        if func == 'D':
            if not li:
                fail = True
                break
            if forward:
                li.popleft()
            else:
                li.pop()
    if fail:
        print('error')
    else:
        if not forward:
            li.reverse()
        print('[' + ','.join(li) + ']')