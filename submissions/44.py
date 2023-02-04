N,Q = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
for _ in range(Q):
    T,x,y = map(int,input().split())
    x -= 1
    y -= 1
    
    x = (x-cnt)%N
    y = (y-cnt)%N
    
    if T == 1:
        A[x],A[y] = A[y],A[x]
    elif T == 2:
        cnt += 1
        cnt %= N
    else:
        print(A[x])