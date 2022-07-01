def solution(p):
    return split(p)
def split(p):
    if len(p) == 0:
        return ''
    l, r = 0, 0
    idx = 0
    while(idx < len(p)):
        if p[idx] == "(":
            l += 1
        else:
            r += 1
        if l == r:
            break
        idx += 1
    u = p[:idx+1]
    v = p[idx+1:]
    
    s = []
    for c in u:
        if c == ")":
            if s:
                s.pop()
            else:
                s.append(c)
        else:
            s.append(c)
    if len(s) == 0:
        result = split(v)
        return u + result
    else:
        result = '(' + split(v) + ')'
        for c in u[1:-1]:
            if c == '(':
                result += ')'
            else:
                result += '('
        return result