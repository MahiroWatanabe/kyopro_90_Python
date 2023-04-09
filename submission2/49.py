N=int(input())
A=list(map(int, input().split()))

D=[0]*(10**6+10)

for i in range(2,10**6+10):
    if D[i]!=0:
        continue
    for k in range(1,10**6):
        if i*k<10**6+10:
            if D[i*k]==0:
                D[i*k]=i
        else:
            break

def fast_prime_fact(x):
    prime=[]
    while 1<x:
        prime.append(D[x])
        x//=D[x]
    return prime

pairwise=True
prime_used=[0]*(10**6+10)
for i in range(N):
    prime_list=fast_prime_fact(A[i])
    prime_set=set(prime_list)
    for i in prime_set:
        if prime_used[i]==1:
            pairwise=False
            break
        else:
            prime_used[i]=1

if pairwise==True:
    print("pairwise coprime")
    exit()

from math import gcd
g=A[0]
for i in range(1,N):
    g=gcd(g,A[i])

if g==1:
    print("setwise coprime")
else:
    print("not coprime")