import sys

input = sys.stdin.readline
N = int(input())
words = sorted(list(set([input().strip() for _ in range(N)])), key = lambda x:(len(x), x))
for word in words: print(word)