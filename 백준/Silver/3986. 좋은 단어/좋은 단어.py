import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    stk = []
    word = input().strip()
    for c in word:
        if not stk:
            stk.append(c)
            continue
        if stk[-1] == c:
            stk.pop()
        else:
            stk.append(c)
    if not stk: cnt += 1
print(cnt)