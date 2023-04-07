import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,M = map(int, input().split())
point = [[] for _ in range(N)]
visited = [-1]*N

for _ in range(M):
    A,B = map(int, input().split())
    A,B = A-1,B-1
    point[A].append(B)
    point[B].append(A)

Que = deque()
Que.append(0)
visited[0] = 1

while Que:
    v = Que.popleft()
    for to in point[v]:
        if visited[to] == -1:
            visited[to] = v+1
            Que.append(to)
print("Yes")
print(*visited[1:])