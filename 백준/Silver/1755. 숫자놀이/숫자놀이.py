import sys

input = sys.stdin.readline
M, N = map(int, input().split())
num_to_string_dict = {0: "zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
string_to_num_dict = {}
for key, value in num_to_string_dict.items():
    string_to_num_dict[value] = key

string_nums = []
for num in range(M, N + 1):
    first = num // 10
    second = num % 10
    if first != 0: string_nums.append(f'{num_to_string_dict[first]}  {num_to_string_dict[second]}')
    else: string_nums.append(num_to_string_dict[second])
string_nums.sort()

nums = []
for string_num in string_nums:
    num = string_num.split()
    if len(num) == 1:
        nums.append(str(string_to_num_dict[num[0]]))
    else:
        nums.append(str(string_to_num_dict[num[0]] * 10 + string_to_num_dict[num[1]]))
for i in range(len(nums) // 10 + 1):
    print(' '.join(nums[i * 10:min(len(nums), (i + 1) * 10)]))