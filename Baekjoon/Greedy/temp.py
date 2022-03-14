# print(bin(10))
# print(bin(10)[::-1].index('1'))
from collections import Counter

a = [1, 1, 1, 2, 3, 4, 5]
t = Counter(a)
print(t)