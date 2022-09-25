n = int(input())
towers = list(map(int, input().split(' ')))
stk = []
result = []
for i, tower in enumerate(towers):
    if not stk:
        stk.append([i, tower])
        result.append('0')
        continue
    if stk[-1][1] > tower:
        result.append(stk[-1][0]+1)
        stk.append([i, tower])
    else:
        while(stk and stk[-1][1] < tower):
            stk.pop()
        if not stk:
            result.append('0')
        else:
            result.append(stk[-1][0]+1)
        stk.append([i, tower])

print(' '.join(map(str, result)))