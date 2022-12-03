import sys

input = sys.stdin.readline

R, C = map(int, input().split(' '))
puzzle = [list(input().strip()) for _ in range(R)]
words = []

def search():
    global R, C, puzzle
    for i in range(R):
        word = ''
        for j in range(C):
            letter = puzzle[i][j]
            if letter == '#':
                if len(word) >= 2: words.append(word)
                word = ''
            else:
                word += letter
        if len(word) >= 2: words.append(word)
    
    for j in range(C):
        word = ''
        for i in range(R):
            letter = puzzle[i][j]
            if letter == '#':
                if len(word) >= 2: words.append(word)
                word = ''
            else:
                word += letter
        if len(word) >= 2: words.append(word)
    return

search()
words.sort()
print(words[0])