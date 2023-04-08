H,N = map(int, input().split())
dp = [10**10]*(H+1)
dp[0] = 0

for i in range(N):
    A,B = map(int, input().split())
    for h in range(H+1):
        if h+A <= H:
            dp[h+A] = min(dp[h+A],dp[h]+B)
        else:
            dp[H] = min(dp[H],dp[h]+B)

print(dp[H])