import sys

input = sys.stdin.readline
S = input().strip()
postfixes = []
for i in range(len(S)):
    postfixes.append(S[i:])
for postfix in sorted(postfixes):
    print(postfix)