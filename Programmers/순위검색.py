# 내 답
# 정확도 100 효율성 0
def solution(info, query):
    from collections import defaultdict
    answer = []
    score = []
    cond = [defaultdict(set) for _ in range(4)]
    for i, c in enumerate(info):
        temp = c.split(" ")
        for j, e in enumerate(temp):
            if j == 4:
                score.append(int(e))
            else:
                cond[j][e].add(i)
    for q in query:
        temp = [c for c in q.split(" ") if c != "and"]
        t_set = set([i for i in range(len(info))])
        for j, e in enumerate(temp[:-1]):
            if e == '-':
                continue
            else:
                t_set = t_set & cond[j][e]
        count = 0
        for idx in t_set:
            if score[idx] >= int(temp[-1]):
                count += 1
        answer.append(count)
    return answer

# 카카오에서 안내하는 정석 풀이. 그냥 모든 경우에 대해 dict로 찍어버리고 빠르게 찾자는 마인드네.. 공간 엄청나게 먹겠지만 뭐 빠르게 하려면 이게 낫긴한가보다.
# def solution(info, query):
#     from itertools import combinations
#     from collections import defaultdict
#     answer = []
#     d = defaultdict(list)
#     for line in info:
#         temp = line.split(" ")
#         cond = temp[:-1]
#         score = int(temp[-1])
#         indices = [i for i in range(4)]
#         for i in range(5):
#             for case in combinations(indices, i):
#                 copied = cond.copy()
#                 for idx in case:
#                     copied[idx] = '-'
#                 d["".join(copied)].append(score)
#     for value in d.values():
#         value.sort()
#     for line in query:
#         temp = line.replace(" and", "")
#         temp = temp.split(" ")
#         cond = "".join(temp[:-1])
#         score = int(temp[-1])
#         idx = binary(0, len(d[cond]), d[cond], score)
#         answer.append(len(d[cond]) - idx)
#     return answer

# def binary(low, high, li, target):
#     if low >= high:
#         return low
#     mid = (low + high) // 2
#     if target <= li[mid]:
#         return binary(low, mid, li, target)
#     else:
#         return binary(mid+1, high, li, target)