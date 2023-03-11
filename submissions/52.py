import bisect

N,K = map(int,input().split())
A = list(map(int,input().split()))
P = []
Q = []

def make_bit(A):
    B = []
    for i in range(2**len(A)):
        sum = 0
        for j in range(len(A)):
            if (i >> j) & 1:
                sum += A[j]
        B.append(sum)
        
    return B

P = make_bit(A[:N//2])
Q = make_bit(A[N//2:])

Q.sort()

for i in range(len(P)):
    pos = bisect.bisect_left(Q,K-P[i])
    if pos < len(Q) and Q[pos] == K-P[i]:
        print("Yes")
        exit()

print("No")