def check(mid):
    current_num = 0
    pre = 0
    for i in range(N):
        if A[i]-pre >= mid:
            current_num += 1
            pre = A[i]
    
    if L-pre >= mid:
        current_num += 1
    
    if current_num >= K+1:
        return True
    else:
        return False

N,L = map(int, input().split())
K = int(input())
A = list(map(int,input().split()))

ok = -1
ng = L+1

while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)