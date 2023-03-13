import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N,P,Q = map(int, input().split())
A = list(map(int,input().split()))
cnt = 0

for i in combinations(A,5):
    if i[0]%P*i[1]%P*i[2]%P*i[3]%P*i[4]%P == Q:
        cnt += 1

print(cnt)