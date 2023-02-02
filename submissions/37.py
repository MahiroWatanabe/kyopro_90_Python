import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

W,N = map(int, input().split())
LRV = [list(map(int, input().split())) for _ in range(N)]
    
INF = 10**18
dp = [[-INF]*(W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    l,r,v = LRV[i-1]
    d = deque()
    nxt = 0
    
    for w in range(W+1):
        dp[i][w] = max(dp[i][w],dp[i-1][w])
        
        lower = w-r
        upper = w-l
        while nxt <= w and nxt <= upper:
            val = dp[i-1][nxt]
            while len(d) > 0 and d[-1][0] <= val: #一番後ろがvalより小さいならpop
                d.pop()
            d.append([val,nxt]) #valの値を追加
            nxt += 1
        while len(d) > 0 and d[0][1] < lower:
            d.popleft()
            
        if len(d) == 0:
            continue
        
        dp[i][w] = max(dp[i][w],d[0][0]+v)

print(dp[N][W] if not dp[N][W] < 0 else -1)