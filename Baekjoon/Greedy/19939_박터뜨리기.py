N, K = map(int, input().split())

if N < K*(K+1)/2:
  print(-1)
else:
  if (N-K*(K+1)/2)%K == 0:
    print(K-1)
  else:
    print(K)