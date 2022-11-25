def solution(n, times):
    l = 1
    r = max(times) * n
    while(l != r):
        mid = (l + r) // 2
        numOfPpl = 0
        for time in times:
            numOfPpl += mid // time
        # possible = canFinishInTime(mid, n, times)
        if numOfPpl >= n: r = mid
        else: l = mid + 1    

    return l

def canFinishInTime(targetTime, n, times):
    가능한_심사관_수 = 0
    for time in times:
        if time <= targetTime:
            가능한_심사관_수 += 1
        else:
            break

    커버할수있는_모든_사람수 = 0
    for i in range(가능한_심사관_수):
        time = times[i]
        심사관이_커버할수있는_사람수 = targetTime // time
        커버할수있는_모든_사람수 += 심사관이_커버할수있는_사람수
    
    if 커버할수있는_모든_사람수 < n:
        return False
    
    return True
        