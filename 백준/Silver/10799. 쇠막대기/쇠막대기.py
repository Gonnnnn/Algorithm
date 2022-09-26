import sys
input = sys.stdin.readline
p = input().strip()
stk = []
prev = ''
cnt = 0
for c in p:
    if c == '(':
        stk.append(c)
    else:
        stk.pop()
        if prev == '(':
            cnt += len(stk)
        else:
            cnt += 1
    prev = c
print(cnt)