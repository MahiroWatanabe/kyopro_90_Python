L,R = map(int, input().split())
MOD = 10**9+7
l,r = len(str(L)),len(str(R))
ans = 0

for i in range(l,r+1):
    min_num = max(L,10**(i-1))
    max_num = min(R,10**i-1)
    num = max_num-min_num+1
    print(min_num,max_num,i)
    ans += num*(min_num+max_num)//2*i

print(ans%MOD)