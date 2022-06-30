def solution(N, stages):
    from collections import defaultdict
    d1 = defaultdict(int)
    for stage in stages:
        if stage != N+1:
            d1[stage] += 1
    total = len(stages)
    d2 = defaultdict(int)
    for i in range(1, N+1):
        if total != 0:
            d2[i] = d1[i] / total
            total -= d1[i]
        else:
            d2[i] = 0
    return sorted(d2, reverse=True, key=lambda x:(d2[x], -x))