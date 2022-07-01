def solution(new_id):
    new_id = (new_id.lower())
    temp = []
    for c in new_id:
        if 97 <= ord(c) <= 122 or (ord(c)!=47 and 45 <= ord(c) <= 57) or ord(c) == 95:
            temp.append(c)
    new_id = temp
    temp = []
    buffer = ''
    for c in new_id:
        if c == '.' and buffer == '.':
            continue
        temp.append(c)
        buffer = c
    if temp and temp[0] == '.':
        temp.pop(0)
    if temp and temp[-1] == '.':
            temp.pop()
    if len(temp) == 0:
        temp.append('a')
    new_id = temp
    temp = []
    if len(new_id) >= 16:
        for i in range(15):
            if i == 14 and new_id[i] == '.':
                continue
            temp.append(new_id[i])
        new_id = temp
    if len(new_id) <= 2:
        for i in range(3-len(new_id)):
            new_id.append(new_id[-1])
    return "".join(new_id)