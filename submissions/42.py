K = int(input())
if K%9 != 0:
    print(0)
    exit()

MOD = (10**9)+7
dp = [0]*(K+1)
dp[0] = 1
for s in range(1,K+1):
    for d in range(1,10):
        if s-d >= 0:
            dp[s] += dp[s-d]
    dp[s] %= MOD
    
print(dp[K])