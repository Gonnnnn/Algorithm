# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

formula = input()
formula += ';'

op = ['+', '-', ';']
old_op = ''
idx_marker = 0
nums = []
# parsing
for idx, ch in enumerate(formula):
    if ch in op:
        if(idx_marker == 0):
            nums.append(int(formula[:idx]))
        else:
            if(old_op == '+'):
                nums.append(int(formula[idx_marker + 1:idx]))
            
            elif(old_op == '-'):
                nums.append(-1 * int(formula[idx_marker + 1:idx]))
        old_op = ch
        idx_marker = idx

result = 0
stack = []
# -가 발견되면 stack에 쌓고, 다음 -가 나오면 합쳐서 결과에서 빼준 후 stack을 비운 후 다음 숫자 집어넣기
for i in nums:
    if i < 0:
        if len(stack) == 0:
            stack.append(-1 * i)
        else:
            result -= sum(stack)
            stack = [-1 * i]
    else:
        if len(stack) == 0:
            result += i
        else:
            stack.append(i)

if(len(stack) != 0):
    result -= sum(stack)

print(result)