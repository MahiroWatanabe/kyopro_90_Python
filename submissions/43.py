from collections import deque

def ch(i,j,k):
    return 4*W*i + 4*j + k

H,W = map(int,input().split())
rs,cs = map(int,input().split())
rt,ct = map(int,input().split())
rs,cs = rs-1,cs-1
rt,ct = rt-1,ct-1
S = [input() for _ in range(H)]
INF = 10**18
dist = [INF]*(H*W*4)
XY = [[1,0],[0,1],[-1,0],[0,-1]]

Que = deque()
for i in range(4):
    Que.append([rs,cs,i])
for i in range(4):
    dist[ch(rs,cs,i)] = 0

while Que:
    x,y,r = Que.popleft()
    preindex = ch(x,y,r)
    for i,[dx,dy] in enumerate(XY):
        current_x,current_y = x+dx,y+dy
        index = ch(current_x,current_y,i)
        if 0 <= current_x < H and 0 <= current_y < W:
            if S[current_x][current_y] == "#":
                continue
            if i == r:
                if dist[index] > dist[preindex]:
                    dist[index] = dist[preindex]
                    Que.appendleft([current_x,current_y,i])
            else:
                if dist[index] > dist[preindex]+1:
                    dist[index] = dist[preindex]+1
                    Que.append([current_x,current_y,i])

ans = INF
for i in range(4):
    lastindex = ch(rt,ct,i)
    if dist[lastindex] == -1:
        continue
    ans = min(ans,dist[lastindex])

print(ans)