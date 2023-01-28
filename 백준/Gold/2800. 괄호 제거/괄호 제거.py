import sys
from itertools import combinations

input = sys.stdin.readline
equation = input().strip()

def getParenthesisPairs(equation):
    stack = []
    parenthesisPairs = []

    for index, letter in enumerate(equation):
        if letter == ")":
            while(stack and stack[-1][1] != '('):
                stack.pop()
            leftIndex, _ = stack.pop()
            parenthesisPairs.append((leftIndex, index))
        else:
            stack.append((index, letter))
    return parenthesisPairs

def getNewEquations(parenthesisPairs):
    newEquations = set()
    for i in range(1, len(parenthesisPairs) + 1):
        for combination in combinations(parenthesisPairs, i):
            indices = set()
            for parenthesisPair in combination:
                for index in parenthesisPair:
                    indices.add(index)

            newEquation = ''
            for index, letter in enumerate(equation):
                if index in indices: continue
                newEquation += letter
            newEquations.add(newEquation)
    return sorted(list(newEquations))

parenthesisPairs = getParenthesisPairs(equation)
newEquations = getNewEquations(parenthesisPairs)
for newEquation in newEquations:
    print(newEquation)

'''
1. 괄호쌍의 index를 구한다. 괄호가 두쌍이면 index쌍도 두쌍
2. 이들의 조합으로 다음을 반복한다.
    - 새로운 string을 만든다. 이 때 조합에 포함되는 index는 제외하고 string을 만든다.
    - 출력한다.
'''