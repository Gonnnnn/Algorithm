def solution(record):
    from collections import defaultdict
    answer = []
    verb = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
    d = defaultdict(str)
    for re in record:
        t = re.split(" ")
        if t[0] == 'Enter' or t[0] == 'Change':
            d[t[1]] = t[2]
        if t[0] == 'Enter' or t[0] == 'Leave':
            answer.append([t[0], t[1]])
    for i in range(len(answer)):
        v, Id = answer[i]
        answer[i] = f"{d[Id]}님이 {verb[v]}"
    
    return answer