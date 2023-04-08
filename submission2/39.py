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
A = list(map(int,input().split()))
A = [-i for i in A]
heapify(A)

for i in range(M):
    v = heappop(A)
    num = -v//2
    heappush(A,-num)

print(-sum(A))