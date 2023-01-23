import sys

def getLastNumAndOp(array):
    nonNumbers = set(['-', '+'])
    lastNum = 0
    lastOp = None
    for element in array:
        if element in nonNumbers:
            lastNum = 0
            lastOp = element
        elif element == ' ':
            continue
        else:
            lastNum = lastNum * 10 + element
    return lastNum, lastOp

def solve(array, Sum, count):
    if count == N:
        if Sum == 0:
            answers.append(array[:])
        return
    
    count += 1

    lastNum, lastOp = getLastNumAndOp(array)

    array.append('+')
    array.append(count)
    solve(array, Sum + count, count)
    array.pop()
    array.pop()

    array.append('-')
    array.append(count)
    solve(array, Sum - count, count)
    array.pop()
    array.pop()
    
    array.append(' ')
    array.append(count)
    newSum = 0
    if lastOp == '+':
        newSum = Sum - lastNum + lastNum * 10 + count
    elif lastOp == '-':
        newSum = Sum + lastNum - lastNum * 10 - count
    else:
        newSum = lastNum * 10 + count
    solve(array, newSum, count)
    array.pop()
    array.pop()
    return

input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    answers = []
    solve([1], 1, 1)
    answers.sort()
    for answer in answers:
        print(''.join(map(str, answer)))
    print()