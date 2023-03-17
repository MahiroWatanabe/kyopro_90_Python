import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

def do(bit):
    column = 0
    #選ばれた行の個数をカウント
    for i in range(H):
        if (bit >> i) & 1:
            column += 1
    
    D = defaultdict(int)
    
    for j in range(W):
        num = []
        for i in range(H):
            if (bit >> i) & 1:
                num.append(P[i][j])
        #列で見ていき、選ばれている行の値をnumに追加していく、
        #そして、set型にすることで値が一つしかなかった時（列の値がすべて同じ時）
        #の判定を行うことができる
        if len(set(num)) == 1:
            D[num[0]] += 1
    #最後にカウントされた数×列の数を返す
    return max(D.values()) * column if len(D) > 0 else 0
            
                
            
H,W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]
ans = 0
for bit in range(2**H):
    ans = max(ans,do(bit))

print(ans)