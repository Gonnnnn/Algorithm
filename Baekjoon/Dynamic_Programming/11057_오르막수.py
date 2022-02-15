N = int(input())
DP = [1]*10
for i in range(1, N):
  for j in range(len(DP)):
    DP[j] = sum(DP[j:]) % 10007
print(sum(DP) % 10007)