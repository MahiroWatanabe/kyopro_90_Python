import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,M,X,Y = map(int, input().split())
connect = [[] for _ in range(N+1)]

for _ in range(M):
    A,B,T,K = map(int, input().split())
    connect[A].append([B,T,K])
    connect[B].append([A,T,K])

Que = []
heappush(Que,[0,X])
time = [10**20]*(N+1)
time[X] = 0
confirmed = [False]*(N+1)

while Que:
    now_time,now_place = heappop(Que)
    if confirmed[now_place]:
        continue
    confirmed[now_place] = True
    for to_place,T,K in connect[now_place]:
        if not confirmed[to_place]:
            to_time = ceil(now_time/K)*K+T
            if to_time < time[to_place]:
                time[to_place] = to_time
                heappush(Que,[to_time,to_place])

if time[Y] == 10**20:
    print(-1)
else:
    print(time[Y])