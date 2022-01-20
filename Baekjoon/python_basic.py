# ###########################list
array = [[0]*3 for _ in range(4)]
# 4*3의 리스트

# append-O(1), sort-O(NlogN), reverse-O(N), insert-O(N), count-O(N), remove-O(N)
# how to remove certain data in a list
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]

# ###########################String --> +, *, slicing
# 특정 인덱스의 값을 바꿀 수는 없음
oh = "hello"
print(oh)
oh = oh*3
print(oh)
ah = "ooh"
print(oh+ah)

# ###########################tuple --> 한 번 선언된 값을 변경 불가
# 서로 다른 성질의 데이터를 "묶어서" 사용할 때 유용. ex) 최단 경로 알고리즘에서 (비용, 노드 번호)
# hashing의 키 값으로서 데이터를 사용할 때
tuplee = (1, 2, 3, 4, 5)

# ###########################dictionary --> hash table사용한다고 함! 보통 값에 접근하는데 O(1)이겠네
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
if '사과' in data:
  print("'사과' exists!")

key_list = data.keys()
data.values()
for key in key_list:
  print(data[key])

data2 = {'사과':'apple', '바나나':'banana'}

# ###########################set --> 중복 허용 x, 순서 x ** map은 중복허용했었지?
# list나 문자열로 초기화 가능
# 중복인 것들은 사라진다
sett = set([1, 1, 2, 3, 4, 5, 5, 6, 7, 8])
settt = {1, 1, 2, 3,  4, 5, 5}
# 합, 교, 차집합 연산이 제공된다. 이거 자료구조 들을 때 함수로 구현해본걸로 기억함. TC는 더 긴 set의 길이가 N일 때 O(N)이었던걸로 기억(알고리즘 떠올려보면)
print(sett|settt)
print(sett&settt)
print(sett-settt)
# 원소 하나 추가 O(1)
sett.add(10)
# 원소 여러개 추가 O(1)
sett.update([11, 12])
# 특정한 값을 갖는 원소 삭제 O(1)
sett.remove(3)

# ###########################입출력
# input : 한줄의 문자열을 입력받음
# 입력을 빨리 받아야하면 sys.stdin.readline() -> 마지막에 개행문자가 초함되므로 rstrip()메소드를 함께 사용

# print(7, end" ") -> 줄바꿈 하지 않고 한칸만 띄움
# print(f"하하하ㅏ하 {variable}하하하")

##########################
# 기타 연산자
# x in 리스트, 튜플, 문자열, 딕셔너리 다 가능!

# 아무것도 처리하고 싶지 않아? pass!
score = 85
if score >= 80:
  pass
else:
  print("too low")

# 조건부 표현식
result = "Success" if score >= 80 else "Fail"

##########################
# 함수
# global keyword
number = 0

def func():
  global number
  number += 1

for i in range(10):
  func()
print(number)
# 동일 이름의 지역변수가 있다면, 전역변수보다 우선적으로 적용된다는 점 잊지말자!
# 전역변수로 선언된 리스트의 경우 global keyword업시도 함수 안에서 참조가 가능하다! 덜덜
# 다만, 동일 이름의 리스트가 있더라도, 먼저 global keyword를 써줬으면, 전역변수인 리스트를 참조한다. 아래 예시를 가지고 놀아보자

abcd = [1, 2, 3, 4, 5]

def oof():
  global abcd
  abcd = [1, 1, 1]
  abcd.append(6)
oof()
print(abcd)

##########################
#람다 표현식
# sorted key에 쓸 수 있고, 여러 개의 리스트에 특정 함수를 적용할 때도 유용
print((lambda a, b: a+b)(3, 7))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
oohoo = map(lambda a, b: a+b, list1, list2)
print(list(result))

##########################
#유용한 표준 라이브러리!
# 내장함수
inner = sum([1, 2, 3, 4, 5]) # 리스트나 튜플 등등
min_result = min(1,2133,5235,23)
max_result = max(12, 4324, 232)
# string으로 식을 써주면 실제 수의 형태로 계산해서 반환..
wow = eval("(3+5)*7")
hmm = [('a', 12), ('b', 13), ('c', 1)]
sorted_result = sorted(hmm, key=lambda x:x[1], reverse=True)
oohsodfhosdf = "".join(['a', 'b', 'c'])


# itertools - 순열(Permutations) 조합(combinations. 모든 경우를 고려해야하는 경우. 완전탐색문제
# 먼저 순열 조합 공식으로 계산해봐서 경우의수가 어느정도가 되는지 생각해보고 쓸지 안쓸지 생각해봐야지
# 얘는 구글링해서 쓰는법 보자!
# 중복 순열과 중복 조합은 "from itertools import product"

# heapq - heap 자료구조 제공. 다익스트라같은 최단경로 알고리즘

# bisect - 이진탐색 기능이 필요할 때

# collections - deque, counter등의 자료구조
# counter는 리스트 같은 반복가능한 객체가 있을 때 내부의 원소가 몇 번씩 등장했는지 알려줌

# math - 삼각함수, 팩토리얼, 제곱근, 최대공약수 등등

