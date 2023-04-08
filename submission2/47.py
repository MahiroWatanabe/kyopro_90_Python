import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,Q = map(int, input().split())
A = [0] + list(map(int,input().split()))
for i in range(1,N+1):
    A[i] = A[i] ^ A[i-1]
for _ in range(Q):
    T,X,Y = map(int, input().split())
    if T == 1:
        A[X] = A[X] ^ Y
    else:
        print()