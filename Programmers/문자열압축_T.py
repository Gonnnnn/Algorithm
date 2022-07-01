def solution(s):
    if len(s) == 1:
        return 1
    answer = 2*len(s);
    for i in range(1, len(s)//2 + 1):
        count = 0
        buffer = s[:i]
        temp = ''
        for j in range(0, len(s)+i, i):
            if buffer == s[j:j+i]:
                count += 1
            else:
                if count == 1:   
                    temp += buffer
                else:
                    temp += str(count) + buffer
                    count = 1
                buffer = s[j:j+i]
        if len(temp) < answer:
            answer = len(temp)
    return answer