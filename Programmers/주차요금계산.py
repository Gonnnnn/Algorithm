def solution(fees, records):
    import math
    answer = []
    note = {}
    for re in records:
        temp = re.split(" ")
        h = int(temp[0][:2])
        m = int(temp[0][3:])
        num = int(temp[1])
        inout = temp[2]
        if num not in note:
            note[num] = [h, m, inout, 0]
        else:
            if inout == 'OUT':
                note[num][3] += (h-note[num][0])*60 + (m-note[num][1])
            note[num][0] = h
            note[num][1] = m
            note[num][2] = inout
    kk = sorted(note.keys())
    for k in kk:
        if note[k][2] == 'IN':
            note[k][3] += (23-note[k][0])*60 + (59-note[k][1])
        answer.append(fees[1] if note[k][3] <= fees[0] else fees[1] + math.ceil((note[k][3]-fees[0])/fees[2])*fees[3])
    return answer