N,K = map(int, input().split())
A = [0] + list(map(int,input().split()))
visited = [-1]*(N+1)
visited[1] = 0
now_town = 1
move_cnt = 0

for i in range(10**6):
    move_cnt += 1
    now_town = A[now_town]
    
    if move_cnt == K:
        print(now_town)
        exit()
    
    if visited[now_town] == -1:
        visited[now_town] = move_cnt
    else:
        cycle = move_cnt-visited[now_town]
        break

K -= move_cnt
K %= cycle

for i in range(K):
    now_town = A[now_town]

print(now_town)