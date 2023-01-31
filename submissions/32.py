import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [[False]*N for _ in range(N)]

for _ in range(M):
    X,Y = map(int, input().split())
    X,Y = X-1,Y-1
    XY[X][Y] = True
    XY[Y][X] = True
    
ans = 10**10

for run in permutations(i for i in range(N)):
    cnt = 0
    flag = False
    for i in range(N-1):
        if XY[run[i]][run[i+1]] == True:
            flag = True
            break
        cnt += A[run[i]][i]
        
    if flag:
        continue
    
    cnt += A[run[-1]][N-1]
    ans = min(ans,cnt)

print(ans if ans != 10**10 else -1)