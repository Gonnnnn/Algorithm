def solution(n, times):
    l = 1
    r = max(times) * n
    while(l != r):
        mid = (l + r) // 2
        numOfPpl = 0
        for time in times:
            numOfPpl += mid // time
        if numOfPpl >= n: r = mid
        else: l = mid + 1    
    return l