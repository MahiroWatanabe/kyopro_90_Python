import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

H,W,K = map(int, input().split())
C = [list(input()) for _ in range(H)]
cnt = 0

def do(bit1,bit2):
    D = deepcopy(C)
    for i in range(H):
        if (bit1 >> i) & 1:
            for j in range(W):
                D[i][j] = "o"
        else:
            for j in range(W):
                if (bit2 >> j) & 1:
                    D[i][j] = "o"
    
    ans = 0
    for i in range(H):
        for j in range(W):
            if D[i][j] == "#":
                ans += 1
                
    return True if ans == K else False

for bit1 in range(2**H):
    for bit2 in range(2**W):
        if do(bit1,bit2):
            cnt += 1

print(cnt)