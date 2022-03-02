N = int(input())
DP = [0]*(N+1)

num = 1
cur_pow = 1
next_pow = 1
for i in range(1, N+1):
  # i가 다음 제곱수인 new_pow 보다 작을 때
  if i < next_pow:
    # i가 17~24라고 했을 때, num은 5
    # i는 i보다 작은 수에 1, 2, 3, 4의 제곱들 중 하나를 더해서 만들어졌을 것
    # 따라서 5-1 = 4를 temp_num으로 지정
    temp_num = num-1
    # DP에 대입할 temp값. 1^2 * i = i이므로 i로 초기화
    temp = i

    # 위의 예시 기준, 4, 3, 2, 1의 제곱들을 i에서 빼주며 DP테이블 확인. 가장 작은걸 구한 후 DP[i] 갱신
    while(temp_num > 0):
      new_value = DP[i-(temp_num * temp_num)] + 1
      if new_value < temp:
        temp = new_value
      temp_num -= 1

    DP[i] = temp
      
  elif i == next_pow:
    # i는 제곱수이므로 DP[i] = 1
    DP[i] = 1
    # i이하인 가장 큰 제곱수 : cur_pow
    # cur_pow를 업데이트
    cur_pow = next_pow
    # num, next_pow 업데이트
    num += 1
    next_pow = num*num
    
  
print(DP[-1])