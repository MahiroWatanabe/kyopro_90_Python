import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def bfs(x,y):
    Que = deque()
    Que.append([x,y])
    dist = [[-1]*W for _ in range(H)]
    dist[x][y] = 0
    
    while Que:
        st,sy = Que.popleft()
        for i in range(4):
            move_x,move_y = XY[i]
            current_x,current_y = st+move_x,sy+move_y
            if 0 <= current_x < H and 0 <= current_y < W:
                if S[current_x][current_y] == "." and dist[current_x][current_y] == -1:
                    dist[current_x][current_y] = dist[st][sy] + 1
                    Que.append([current_x,current_y])
    
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                cnt = max(cnt,dist[i][j])
        
    return cnt

H,W = map(int, input().split())
S = [list(input()) for _ in range(H)]
XY = [[1,0],[0,1],[-1,0],[0,-1]]
ans = 0
D = []

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            ans = max(ans,bfs(i,j))

print(ans)