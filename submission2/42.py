N,W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*(W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(W+1):
        if dp[i][j] != -1:
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            if j+WV[i][0] <= W:
                dp[i+1][j+WV[i][0]] = max(dp[i+1][j+WV[i][0]],dp[i][j]+WV[i][1])
    
print(max(dp[-1]))