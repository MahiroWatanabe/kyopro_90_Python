N,K = map(int,input().split())
point = []
for _ in range(N):
    A,B = map(int,input().split())
    point.append(B)
    point.append(A-B)

point.sort(reverse=True)

ans = 0
for i in range(K):
    ans += point[i]

print(ans)