import sys
from itertools import combinations

input = sys.stdin.readline
equation = input().strip()
operands = set(('+-*/'))

def convert(start, equation):
    answer = ''
    operatorStack = []
    operandStack = []
    index = start

    while(index < len(equation)):
        letter = equation[index]
        index += 1

        if letter == '(':
            letter, index = convert(index, equation)
        elif letter == ')':
            break
        
        if letter == '+' or letter == '-':
            answer += ''.join(operandStack) + ''.join(operatorStack[::-1])
            operatorStack = [letter]
            operandStack = []
        elif letter == '*' or letter == '/':
            operatorStack.append(letter)
        else:
            if operatorStack and (operatorStack[-1] == '*' or operatorStack[-1] == '/'):
                lastOperator = operatorStack.pop()
                lastOperand = operandStack.pop()
                letter = lastOperand + letter + lastOperator
            operandStack.append(letter)
    answer += ''.join(operandStack) + ''.join(operatorStack[::-1])
    return answer, index

answer, _ = convert(0, equation)
print(answer)