import sys

input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split(' ')))
answer = 0
while(sum(numbers) != 0):
    isThereOdd = False
    for index, number in enumerate(numbers):
        if number % 2 == 1:
            isThereOdd = True
            answer += 1
            numbers[index] -= 1
    if not isThereOdd:
        for index in range(N):
            numbers[index] = numbers[index] // 2
        answer += 1
print(answer)