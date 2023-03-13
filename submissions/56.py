N,S = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(S+1):
        if dp[i][j] == True:
            if j+AB[i][0] <= S:
                dp[i+1][j+AB[i][0]] = True
            if j+AB[i][1] <= S:
                dp[i+1][j+AB[i][1]] = True
                
if not dp[-1][-1]:
    print("Impossible")
    exit()
    
ans = ""

for i in range(N-1,-1,-1): #for i in reversed(range(N))でも書ける
    if S-AB[i][0] >= 0 and dp[i][S-AB[i][0]] == True:
        ans += "A"
        S -= AB[i][0]
        continue
    
    if S-AB[i][1] >= 0 and dp[i][S-AB[i][1]] == True:
        ans += "B"
        S -= AB[i][1]
        continue

print(ans[::-1])