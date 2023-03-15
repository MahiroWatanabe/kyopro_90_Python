import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

Q = int(input())
D = deque()

for _ in range(Q):
    t,x = map(int, input().split())
    
    if t == 1:
        D.appendleft(x)
    elif t == 2:
        D.append(x)
    else:
        print(D[x-1])