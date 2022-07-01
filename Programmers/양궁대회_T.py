def solution(n, info):  
    answer = []
    ryan = [0 for _ in range(11)]
    dif = 0
    for case in range(1, 1<<10):
        cnt = 0
        ry_score = 0
        ap_score = 0
        for i in range(10):
            if case & (1<<i):
                ryan[i] = info[i] + 1
                cnt += ryan[i]
                ry_score += 10 - i
            else:
                ryan[i] = 0
                if info[i] != 0:
                    ap_score += 10 - i
        if cnt > n:
            continue
        ryan[10] = n - cnt
        if ry_score - ap_score >= dif:
            answer = ryan[:]
            dif = ry_score - ap_score
    if dif == 0:
        answer = [-1]
    return answer