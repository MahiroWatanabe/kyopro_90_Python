N = int(input())
X,Y = [],[]
for _ in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = 0
  
X.sort()
Y.sort()
mid_x,mid_y = 0,0

if N%2 == 0:
    mid_x = (X[N//2-1]+X[N//2])//2
    mid_y = (Y[N//2-1]+Y[N//2])//2
else:
    mid_x = X[N//2]
    mid_y = Y[N//2]

for i in range(N):
    ans += abs(X[i]-mid_x)+abs(Y[i]-mid_y)

print(ans)