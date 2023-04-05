import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

S = deque(input())
Q = int(input())
flag = True

for _ in range(Q):
    x,*_a = input().split()
    if x == "1":
        if flag:
            flag = False
        else:
            flag = True
    else:
        F,C = _a
        if flag:
            if F == "1":
                S.appendleft(C)
            else:
                S.append(C)
        else:
            if F == "1":
                S.append(C)
            else:
                S.appendleft(C)                
S = "".join(list(S))

print(S if flag else S[::-1])