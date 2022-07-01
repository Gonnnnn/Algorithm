def solution(lottos, win_nums):
    answer = []
    zeros = 0
    for n in lottos:
        if n == 0:
            zeros += 1
    temp = set(win_nums) - set(lottos)
    wrong_max = len(temp)
    wrong_min = len(temp) - zeros
    answer = [min(1+wrong_min, 6), min(1+wrong_max, 6)]
    
    return answer