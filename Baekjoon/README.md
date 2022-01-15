# Note
## Ones to do later again
10610__30 1946__신입사원(greedy에 대해 이해하기에 좋은 문제. 다만 내가 푼 풀이(1)은 왜 틀렸는지 모르겠다. 생각해봐야할 것이다.)

## A little tricky
1931_회의실배정 1080_배열(논리는 맞았지만 구현하는데 있어서 오류가 많았던 문제)

## It could be better
1541_잃어버린괄호 16953_AtoB 1439_뒤집기

## Greedy
### Idea

#### 1339
- 알고리즘 문제 한정, 경우의 수를 다양한 조건문을 통해서 작성해야 하는 경우, 되게 간단한 방법이 존재하거나, Brute-Force해야하는 경우가 존재한다.

#### 4796
- 간단한 계산이더라도, 범위 등을 손으로 그려보고, 표현해보며 검증하자. 매우 간단한 문제였지만, 중간에 더해지는 값이 문제에서 제시되는 L을 넘으면 안되는게 당연한데, 그 부분을 생각치 못했다.

#### 1202
- 두개의 변수가 있을 때 하나를 고정하고, 그에 적합한 것을 찾아보고, 그 반대로 다른 하나를 고정 후 우너래 고정했던 것을 변경하며 그에 적합한 것을 찾아가보자  
- 가장 가치가 높은 보석을 선택 후 그에 맞는 최선의 가방을 찾기 vs 가장 큰 or 작은 가방을 선택 후 그에 맞는 최선의 보석 찾기


### Python modules that i wasn't really familiar with

#### 11047
- reverse for loop  
for i in range(number, -1, -1):

#### 1931
- readline  
import sys / input = sys.stdin.readline / variable = int(input())  
faster than normal 'intput()'  
****** readline으로 읽어올 때, 제일 마지막에 개행문자 '\n'이 붙는다. 이는 input().split()으로 없앨 수 있다.  
int(input())을 했을 때 자동으로 사라지며, input().split()을 했을 때도 자동으로 떨어져 나간다.

#### 10162
- "".join  
print("{0} {1} {2}".format(nums[0], nums[1], nums[2])) -> print(" ".join(map(str, nums))  

- int(time/buttons[idx])

#### 10610
- map("".join, iteratable)  
It applies ' "".join ' to each element

- "".join(map(str, iteratble))  
It applies 'str' to each element and then join them

- Permutation, combination  
from itertools import permutations  
permutations(iteratable, 3) --> it returns an iteratable object. You'll have to change it to a list. Each element will be a tuple. ex) ('A', 'B', 'C')  
** It wouldn't be proper to use when you have to deal with a big number of cards (Space complexity)

#### 1946
- lambda  
lambda variable: return --> Lambda expression itself returns a function object. You need to assign it to a variable 
ex) a = lambda x:x + 10  
** https://dojang.io/mod/page/view.php?id=2359

- you can't assign list.sort() to a variable

#### 2864
- variable = str.replace('a word i want to change to ABCD', 'ABCD')

#### 1080
- a = [list(map(int, input().strip())) for _ in range(n)]  
- a[n-2:n][:m] != b[n-2:n][:m]  
arrays can be compared through != and ==