import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
sys.setrecursionlimit(10**7)

N,M = map(int, input().split())
point = [[] for _ in range(N)]

for _ in range(M):
    A,B = map(int, input().split())
    A,B = A-1,B-1
    point[A].append(B)

ans = 0

def dfs(pos):
    if goal[pos]:
        return
    goal[pos] = True
    
    for j in point[pos]:
        dfs(j)

for i in range(N):
    goal = [False]*N
    dfs(i)
    ans += sum(goal)
    
print(ans)