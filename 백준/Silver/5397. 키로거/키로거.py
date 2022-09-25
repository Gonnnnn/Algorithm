n = int(input())
for _ in range(n):
    word = input()
    stkL = []
    stkR = []
    for letter in word:
        if letter == '<':
            if stkL:
                stkR.append(stkL.pop())
        elif letter == '>':
            if stkR:
                stkL.append(stkR.pop())
        elif letter == '-':
            if stkL:
                stkL.pop()
        else:
            stkL.append(letter)
    stkR.reverse()
    print(''.join(stkL) + ''.join(stkR))