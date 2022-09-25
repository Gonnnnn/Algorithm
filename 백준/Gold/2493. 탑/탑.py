n = int(input())
towers = list(map(int, input().split(' ')))
stk = []
result = []
for i, tower in enumerate(towers):
    while stk:
        if stk[-1][1] > tower:            
            break
        else:
            stk.pop()
    if stk:
        result.append(stk[-1][0]+1)
    else:
        result.append('0')
    stk.append([i, tower])
print(' '.join(map(str, result)))