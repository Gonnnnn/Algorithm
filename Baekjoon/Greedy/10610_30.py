# 문제
# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

# 입력
# N을 입력받는다. N는 최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

# 출력
# 미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.

# 시간 초과 더럽게 많이 뜨던 문제. TC 파악하기!

num_list = list(input())
summ = 0
for i in num_list:
  summ += int(i)

if(summ%3 != 0 or '0' not in num_list):
    print(-1)
else:
    num_list.sort(reverse=True)
    if(num_list[-1] != '0'):
      print(-1)
    else:
      print(''.join(num_list))
# 좀 더 간결
# N = sorted(list(input()), reverse=True)

# if N[-1] != '0':
#     print(-1)
#     exit(0)

# if sum(map(int, N)) % 3 == 0:
#     print(''.join(N))
# else:
#     print(-1)