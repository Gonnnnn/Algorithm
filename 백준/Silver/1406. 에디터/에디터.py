word = input()
n = int(input())
stkL = list(word)
stkR = []
for _ in range(n):
    order = input()
    if order[0] == 'P':
        _, letter = order.split(' ')
        stkL.append(letter)
    elif order == 'L':
        if stkL:
            stkR.append(stkL.pop())
    elif order == 'D':
        if stkR:
            stkL.append(stkR.pop())
    elif order == 'B':
        if stkL:
            stkL.pop()
stkR.reverse()
print(''.join(stkL) + ''.join(stkR))
