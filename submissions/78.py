N,M = map(int, input().split())
point = [[] for _ in range(N)]
ans = 0

for _ in range(M):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    point[a].append(b)
    point[b].append(a)

for i in range(N):
    cnt = 0
    
    for to in point[i]:
        if i != to and to < i:
            cnt += 1
            
    if cnt == 1:
        ans += 1

print(ans)