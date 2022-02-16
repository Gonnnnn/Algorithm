# Greedy Algorithm
### We use Greedy methods when
- Greedy Choice Property : 앞의 선택이 이후의 선택에 영향을 주지 않는다.  
무슨 소리인지 이해가 안갈 것이다. 설명이 불친절해쳐먹어서 그렇다!  
*쉽게 말하면, 논리가 바뀌지 않는다는 것이다.*  
 앞의 선택을 하는데 있어서 적용한 논리가 있을 것이다. 이때, 앞의 선택은 이후 선택들에 대해서도 선택을 위해 적용하는 논리에 영향을 미치지 않는다는 것이다. 대표적인 동전 거스름돈 문제를 예로들자. 애초에 최소 갯수의 동전을 주기 위해서는 줄 수 있는 가장 가치가 큰 동전으로 최대한 돈을 거슬러줘야하고, 그 후 남은 돈에 대해서도 같은 과정을 반복해야한다! 
- Optimal Substructure : 문제에 대한 최종 해결 방법은 부분 문제에 대한 최적 문제 해결 방법으로 구성된다.
- 위의 조건이 성립하지 않는 경우 최적해를 구할 수 없다.
### Procedure
- 선택 절차(Selection Procedure): 현재 상태에서의 최적의 해답을 선택한다.
- 적절성 검사(Feasibility Check): 선택된 해가 문제의 조건을 만족하는지 검사한다.
- 해답 검사(Solution Check): 원래의 문제가 해결되었는지 검사하고, 해결되지 않았다면 선택 절차로 돌아가 위의 과정을 반복한다.  

<pre>
  <code>
  while (there are more coins and the instance is not solved) {
  Grab the largest remaining coin;	// 선정과정
    
    if ( adding the coin makes the change exceed the amount owed){
      reject the coin;			// 적정성 점검
    }
    else
      add the coin to the change;
    
    if ( the total value of the change equals the amount owed )
      the instance is solved;			// 해답 점검
  }
  </code>
</pre>

Ref : https://hanamon.kr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%83%90%EC%9A%95%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-greedy-algorithm/

### 좋은 문제들
1946  1715  1339  1202  2437 11000  

9576 : 이분 매칭을 활용할 수도 있는 문제이다. 다만 정렬을 함으로써 그리디로 해결이 가능했던 것이다. 막상 보면 쉬운데 어렵게 다가왔고 내 실력으로 푼게 아닌 것 같았다. 꼭 다시 풀자  

8980 : 교집합 관계를 다른 방향으로 생각해볼 수 있는 좋은 문제이다. 직접 제대로 못풀었다.

### Idea

#### 1339
- 알고리즘 문제 한정, 경우의 수를 다양한 조건문을 통해서 작성해야 하는 경우, 되게 간단한 방법이 존재하거나, Brute-Force해야하는 경우가 존재한다.
- 먼저 답을 결정짓는데 필요한 요소(단어의 길이, 같은 자리수에서 알파벳이 같은지의 유무 등))를 파악하고, 이러한 요소들이 같은 경우, 다른경우-작은경우/큰경우를 생각해 케이스를 만들어보는 것이 중요하다.  
- Dictionary  
dict.keys(), dict.values(), dict(items) --> iterable. can be used for a for loop. list화 하는 경우 인덱스를 통해 접근도 가능

#### 4796
- 간단한 계산이더라도, 범위 등을 손으로 그려보고, 표현해보며 검증하자. 매우 간단한 문제였지만, 중간에 더해지는 값이 문제에서 제시되는 L을 넘으면 안되는게 당연한데, 그 부분을 생각치 못했다.

#### 1202
- 두개의 변수가 있을 때 하나를 고정하고, 그에 적합한 것을 찾아보고, 그 반대로 다른 하나를 고정 후 우너래 고정했던 것을 변경하며 그에 적합한 것을 찾아가보자  
- 가장 가치가 높은 보석을 선택 후 그에 맞는 최선의 가방을 찾기 vs 가장 큰 or 작은 가방을 선택 후 그에 맞는 최선의 보석 찾기

#### 1213
- alphabet과 같이 한정된 경우의 수가 있고, 그게 26가지 정도로 작을 때, 배열을 임의로 만들고 각 알파벳 index에 맞게 카운트 해주기만 하면 공간을 덜 잡아먹을 수 있겠다.

#### 2212
- 물론 특정 기준을 잡고 그 것을 만족하지 못할 때 케이스들을 제외하는 경우도 있겠지만, 그리디의 경우 대부분 기준 자체가 항상 일정하게 있다기 보다는, 전체적으로 봤을 때 가장 안좋은 것들을 하나씩 제외해 나가는 경우가 많은 것 같다.

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

- 매번 비교할 때 기준을 바꿔야할 경우가 있다. 이러한 문제들에서 주어지는 데이터는 많은 경우 대소관계를 비교해야한다. 집합을 사용하자.  
ex) 내가 비교하고자 하는 데이터들을 어떤 기준에 의해 먼저 정렬해놓았고, 정렬된 순서대로 데이터들을 체크해가며 특정 기준에 부합하면 채택한다고 하자. 그 특정 기준이라는걸 바꿔야할 경우가 있다는 것이다. 데이터가 작으면 작을 수록 좋지만, 이전에 비교했던 것들 전부보다 크면 안된다고 할 때, 이전에 비교했던 것들 중 제일 작은 것보다는 무조건 작아야 한다는 것이다. 이 말은 매번 비교하면서, 기준보다 작은 값이 나오면, 그 작은 값을 새 기준으로 채택할 수 있다는 것이다.

#### 2864
- variable = str.replace('a word i want to change to ABCD', 'ABCD')

#### 1080
- a = [list(map(int, input().strip())) for _ in range(n)]  
- a[n-2:n][:m] != b[n-2:n][:m]  
arrays can be compared through != and ==

#### 1715
- heapq : heaq.heapify(list) - O(N), heapq.heappop(heapified list) - O(logn), heapq.heappush(heapified list, value) - O(logn)

#### 1343
- replace : string = string.replace('character to change', 'character to change the previous one to')  
- 0번째 idx부터 해당 character을 찾아 교체하고, 남은 character들을 기준으로 다시 반복한다.  

#### 12904
- list[::-1] - 뒤집기
- 구현과정 중, 마지막 알파벳이 B이면 리스트를 뒤집어야하는 부분이 있었다. deque를 이용해서 popleft하는편이 list를 계속해서 뒤집는 것보다 효율적일 것이라고 생각해, deque를 사용했지만, list[::-1]를 사용한 사람들보다 실행시간이 조금 더 오래걸렸다. 여러 이유가 있을 수 있겠지만, 일단 저 방법도 알아두자. TC만 따져보면 popleft()하는 편이 훨씬 빠를 수 밖에 없다. 아마 list -> deque 객체 생성 과정에서 시간이 좀 걸릴 수도 있고,,