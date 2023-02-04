K = int(input())
cnt = 0
MOD = 10**9+7

for i in range(9,10**5+1,9):
    index = 0
    S = str(i)
    flag = False
    for j in range(len(S)):
        if S[j] == "0":
            flag = True
            break
        index += int(S[j])
    if K == index and not flag:
        cnt = (cnt+1)%MOD
        
print(cnt)
