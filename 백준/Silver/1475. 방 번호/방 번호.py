room = input()
li = [0 for _ in range(10)]
for c in room:
    li[int(c)] += 1
sixNineTotal = li[6] + li[9]
li[6] = (sixNineTotal + 1) // 2
li[9] = (sixNineTotal + 1) // 2
print(max(li))