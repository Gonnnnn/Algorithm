import sys

input = sys.stdin.readline
n = int(input())
stack = [0]
answer = 0
for _ in range(n):
    x, y = map(int, input().split(' '))
    if y < stack[-1]:
        while(y < stack[-1]):
            stack.pop()
            answer += 1
    if stack[-1] != y: stack.append(y)
while(stack[-1] != 0):
    stack.pop()
    answer += 1
print(answer)