def dfs(y,x,cnt):
    if dist[y][x] != -1:
        if cnt-dist[y][x] >= 4:
            return cnt-dist[y][x]
        else:
            return -1
    
    num = -1
    dist[y][x] = cnt
    for dy,dx in XY:
        if 0 <= dy+y < H and 0 <= dx+x < W:
            if S[dy+y][dx+x] != "#":
                num = max(num,dfs(dy+y,dx+x,cnt+1))
    dist[y][x] = -1
    
    return num

H,W = map(int, input().split())
S = [list(input()) for _ in range(H)]
XY = [[1,0],[-1,0],[0,1],[0,-1]]
dist = [[-1 for _ in range(W)] for _ in range(H)]

ans = -1
for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            ans = max(ans,dfs(i,j,0))

print(ans)