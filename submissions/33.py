import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,K = map(int, input().split())
a = list(map(int,input().split()))

cnt = defaultdict(int)
ans = 0
l = 0

for r in range(N):
    cnt[a[r]] += 1
    while True:
        if len(cnt) <= K:
            break
        cnt[a[l]] -= 1
        if cnt[a[l]] == 0:
            del cnt[a[l]]
        l += 1
    ans = max(ans,r-l+1)

print(ans)