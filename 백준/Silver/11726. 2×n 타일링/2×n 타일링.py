n = int(input())
DP = [0]*(n+1)
def calc(n):
  if n<=3:
    return n
  if DP[n] == 0:
    DP[n] = calc(n-1) + calc(n-2)
  return DP[n]
result = calc(n)
print(result%10007)