import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
tree = dict()
for _ in range(N):
    p, lc, rc = input().split()
    if lc == '.': lc = None
    if rc == '.': rc = None
    tree[p] = [lc, rc]

def preorder(cur):
    lc, rc = tree[cur]
    print(cur, end='')
    if lc: preorder(lc)
    if rc: preorder(rc)

def inorder(cur):
    lc, rc = tree[cur]
    if lc: inorder(lc)
    print(cur, end='')
    if rc: inorder(rc)

def postorder(cur):
    lc, rc = tree[cur]
    if lc: postorder(lc)
    if rc: postorder(rc)
    print(cur, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')