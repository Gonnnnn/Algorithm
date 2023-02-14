import sys

input = sys.stdin.readline
N = int(input())

def solve(word):
    alphabet_set = set()
    prev_letter = ''
    for letter in word:
        if prev_letter == letter: continue
        if letter in alphabet_set: return False
        alphabet_set.add(letter)
        prev_letter = letter
    return True

answer = 0
for _ in range(N):
    if solve(input().strip()): answer += 1
print(answer)