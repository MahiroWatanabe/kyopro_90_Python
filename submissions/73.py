def dfs(x,y,cnt):
    if dist[x][y] != -1:
        if cnt-dist[x][y] >= 4:
            return cnt-dist[x][y]
        else:
            return -1
    
    num = -1
    dist[x][y] = cnt
    for dx,dy in XY:
        if 0 <= x+dx < H and 0 <= y+dy < W:
            if C[x+dx][y+dy] != "#":
                num = max(num,dfs(x+dx,y+dy,cnt+1))
    dist[x][y] = -1
                
    return num

H,W = map(int, input().split())
C = [list(input()) for _ in range(H)]
XY = [[1,0],[-1,0],[0,1],[0,-1]]
dist = [[-1 for _ in range(W)] for _ in range(H)]
ans = -1

for i in range(H):
    for j in range(W):
        ans = max(ans,dfs(i,j,0))

print(ans)