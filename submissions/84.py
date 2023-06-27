import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

def nC2(v):
    return v*(v-1)//2

N = int(input())
S = input()
D = [[i,len(list(j))] for i,j in groupby(S)]
ans = nC2(N+1)

for i,j in D:
    ans -= nC2(j+1)

print(ans)