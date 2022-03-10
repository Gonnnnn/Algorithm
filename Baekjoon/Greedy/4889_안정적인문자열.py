import sys
input = sys.stdin.readline

count = 0
while(True):
  S = input().strip()
  if S[0] == '-':
    break

  count += 1
  stack = []
  for i in range(len(S)):
    if S[i] == '{':
      stack.append('{')
    else:
      if stack and stack[-1] == '{':
        stack.pop()
      else:
        stack.append('}')

  open = 0
  close = 0
  for c in stack:
    if c == '{':
      open += 1
    else:
      close += 1

  result = 0
  if open % 2 == 1:
    result += 2
    open -= 1
    close -= 1
  result += min(open, close) + abs(open-close)//2
  
  print(f'{count}. {result}')

# 좋은 방법
# cnt가 최종 정답
    # cnt = 0
    # for i in data:
    #     if i == '{':
    #         stack.append(i)
    #     else:
    #         if not stack:
    #             cnt += 1
    #             stack.append('{')
    #         else:
    #             stack.pop()

    # cnt += len(stack)//2