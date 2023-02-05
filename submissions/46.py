N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

cnt_a = [0]*46
cnt_b = [0]*46
cnt_c = [0]*46

for i in range(N):
    cnt_a[A[i]%46] += 1
    cnt_b[B[i]%46] += 1
    cnt_c[C[i]%46] += 1
    
cnt = 0

for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k) % 46 == 0:
                cnt += cnt_a[i] * cnt_b[j] * cnt_c[k]

print(cnt)