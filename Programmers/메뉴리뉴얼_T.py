def solution(orders, course):
    from itertools import combinations
    from collections import defaultdict
    answer = []
    
    for num in course:
        d = defaultdict(int)
        for order in orders:
            for comb in combinations(sorted(order), num):
                d["".join(comb)] += 1
        if len(d) != 0 and max(d.values()) > 1:
            Max = max(d.values())
            answer.extend([key for key in d if d[key] == Max])
    return sorted(answer)

# def solution(orders, course):
#   from itertools import combinations
#   from collections import Counter
#   answer = []
  
#   for num in course:
#         cases = []
#         for order in orders:
#             cases.extend(combinations(sorted(order), num))
#         counter = Counter(cases)
#         if len(counter) != 0 and max(counter.values()) != 1:
#             Max = max(counter.values())
#             answer += ["".join(f) for f in counter if counter[f] == Max]
#   return sorted(answer)