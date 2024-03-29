import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right
from functools import reduce
from decimal import Decimal, getcontext

N = int(input())
A = [0] + list(map(int,input().split()))
S = sum(A)
if S%10 != 0:
    print("No")
    exit()
A = set(accumulate(A))

for i in A:
    if (i+S//10)%S in A:
        print("Yes")
        exit()

print("No")