def solution(relation):
    row = len(relation)
    col = len(relation[0])
    answer = []
    for i in range(1, 1 << col):
        key_set = set()
        for re in relation:
            key = ""
            for j in range(col):
                if i & (1 << j):
                    key += re[j]
            key_set.add(key)
        if len(key_set) == row:
            subset = False
            for a in answer:
                if (a & i) == a:
                    subset = True
                    break
            if not subset:
                answer.append(i)
                    
    return len(answer)