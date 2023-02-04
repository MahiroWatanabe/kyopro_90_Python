N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
PA = set()
PB = set()
PC = set()

for i in range(N):
    PA.add(A[i]%46)
for i in range(N):
    PB.add(A[i]%46)
for i in range(N):
    PC.add(A[i]%46)
cnt = 0

for i in list(PA):
    for j in list(PB):
        for k in list(PC):
            if i+j+k % 46 == 0:
                cnt += 1

print(cnt)