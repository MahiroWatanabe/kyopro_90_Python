import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

N = int(input())
x0,y0 = map(int, input().split())
xn2,yn2 = map(int, input().split())

center_X = (x0+xn2)/2
center_Y = (y0+yn2)/2

x0-=center_X
y0-=center_Y

p = 2*pi/N

x1 = cos(p)*x0 - sin(p)*y0 + center_X
y1 = sin(p)*x0 + cos(p)*y0 + center_Y

print(x1,y1)