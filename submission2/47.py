import sys, re, string
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf, cos, sin
from copy import deepcopy, copy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations,groupby
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

# returnに返すx,yの計算方法を変えることで違う処理も可能
# initの部分には単位元となるどの数に対して演算を行っても変わらない数を入れる
# 和、差　：　0
# 積、除算　：　1
# or(|)、xor(^)　：　0
# and(&)　：　1
# 最小値　：　10**10
# 最大値　：　-10**10
# 最大公約数　：　0

def segfunc(x,y):
    return x^y

class SegTree:
    def __init__(self,x_list,init,segfunc):
        self.init=init
        self.segfunc=segfunc
        self.Height=len(x_list).bit_length()+1
        self.Tree=[init]*(2**self.Height)
        self.num=2**(self.Height-1)
        for i in range(len(x_list)):
            self.Tree[2**(self.Height-1)+i]=x_list[i]
        for i in range(2**(self.Height-1)-1,0,-1):
            self.Tree[i]=segfunc(self.Tree[2*i],self.Tree[2*i+1])

    def select(self,k):
        return self.Tree[k+self.num]

    def update(self,k,x):
        i=k+self.num
        self.Tree[i]=x
        while i>1:
            if i%2==0:
                self.Tree[i//2]=self.segfunc(self.Tree[i],self.Tree[i+1])
            else:
                self.Tree[i//2]=self.segfunc(self.Tree[i-1],self.Tree[i])
            i//=2

    def query(self,l,r):
        result=self.init
        l+=self.num
        r+=self.num+1

        while l<r:
            if l%2==1:
                result=self.segfunc(result,self.Tree[l])
                l+=1
            if r%2==1:
                result=self.segfunc(result,self.Tree[r-1])
            l//=2
            r//=2
        return result

N,Q = map(int, input().split())
A = list(map(int,input().split()))
seg = SegTree(A,0,segfunc)

for i in range(Q):
    T,X,Y = map(int, input().split())
    if T == 1:
        X -= 1
        seg.update(X,seg.select(X)^Y)
    else:
        X,Y = X-1,Y-1
        print(seg.query(X,Y))
