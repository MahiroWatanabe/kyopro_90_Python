N,Q = map(int, input().split())
A = list(map(int,input().split()))
current_dif = [0]*(10**6)
ans = 0
for i in range(N-1):
    B = A[i+1]-A[i]
    current_dif.append(B)
    ans += abs(B)

for _ in range(Q):
    L,R,V = map(int, input().split())
    L,R = L-1,R-1
    mae = abs(current_dif[L-1]) + abs(current_dif[R])
    if L >= 2:
        current_dif[L-1] += V
    if R <= N-1:
        current_dif[R] -= V
    ato = abs(current_dif[L-1]) + abs(current_dif[R])
    ans += (ato-mae)
    print(ans)