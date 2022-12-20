import sys

def isPel(p):
    s = 0
    e = len(p) - 1
    while(s < e):
        if p[s] != p[e]: return False
        s += 1
        e -= 1
    return True

input = sys.stdin.readline
'''
abcde가 회문인 경우
-> a = e, b = d
e를 제외했을 때도 회문이려면?
-> a = d, b = c
위 두 조건을 합치면?
-> a = e d = b = c여야한다.
즉 회문에서 양 끝단 글자 하나가 지워져도 회문이려면, 모든 문자가 같아야한다.
'''

s = input().strip()
if isPel(s):
    if len(set(s)) == 1:
        print(-1)
    else:
        print(len(s) - 1)
else:
    print(len(s))