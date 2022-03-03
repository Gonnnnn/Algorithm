# N, K = map(int, input().split())

# DP = [0]*(N+1)
# DP[0] = 1

# for i in range(1, N+1):
#   DP[i] = (DP[i-1] * i)

# print((DP[N]//DP[N-K]//DP[K])%10007)

# 파스칼의 삼각형의 특징도 기억

# N, K = map(int, input().split())

# DP = [[1] for _ in range(N+1)]
# DP[1].append(1)

# for i in range(2, N+1):
#   for j in range(1, i+1):
#     if j == i:
#       DP[i].append(1)
#     else:
#       DP[i].append(DP[i-1][j-1] + DP[i-1][j])

# print(DP[N][K]%10007)