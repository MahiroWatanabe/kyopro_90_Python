import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
sys.setrecursionlimit(10**7)

def dfs(x,last=-1):
    size[x] += 1
    for to in point[x]:
        if to == last:
            continue
        dfs(to,x)
        size[x] += size[to]

N = int(input())
point = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    point[a].append(b)
    point[b].append(a)

size = [0]*N

dfs(0)
ans = 0
print(size)
for i in range(N):
    ans += size[i]*(N-size[i])
print(ans)