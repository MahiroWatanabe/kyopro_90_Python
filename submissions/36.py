N,Q = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
min_Zj ,max_Zj,min_Wj,max_Wj = 10**18,0,10**18,0

for i in range(N):
    x,y = XY[i]
    min_Zj = min(min_Zj,x+y)
    max_Zj = max(max_Zj,x+y)
    min_Wj = min(min_Wj,x-y)
    max_Wj = max(max_Wj,x-y)

for _ in range(Q):
    q = int(input())
    q -= 1
    x,y = XY[q]
    Zi = x+y
    Wi = x-y
    print(max(Zi-min_Zj,max_Zj-Zi,Wi-min_Wj,max_Wj-Wi))