# Note
## Ones to do later again
10610_30 1946_신입사원(greedy에 대해 이해하기에 좋은 문제. 다만 내가 푼 풀이(1)은 왜 틀렸는지 모르겠다. 생각해봐야할 것이다.)

## A little tricky
1931_회의실배정 

## It could be better
1541_잃어버린괄호

## Greedy
### 11047
- reverse for loop  
for i in range(number, -1, -1):

### 1931
- readline  
import sys / input = sys.stdin.readline / variable = int(input())  
faster than normal 'intput()'

### 10162
- "".join  
print("{0} {1} {2}".format(nums[0], nums[1], nums[2])) -> print(" ".join(map(str, nums))  

- int(time/buttons[idx])

### 10610
- map("".join, iteratable)  
It applies ' "".join ' to each element

- "".join(map(str, iteratble))  
It applies 'str' to each element and then join them

- Permutation, combination  
from itertools import permutations  
permutations(iteratable, 3) --> it returns an iteratable object. You'll have to change it to a list. Each element will be a tuple. ex) ('A', 'B', 'C')  
** It wouldn't be proper to use when you have to deal with a big number of cards (Space complexity)