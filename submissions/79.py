H,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
cnt = 0

for i in range(H-1):
    for j in range(W-1):
        if A[i][j] != B[i][j]:
            diff = B[i][j]-A[i][j]
            cnt += abs(diff)
            A[i][j] += diff
            A[i+1][j] += diff
            A[i][j+1] += diff
            A[i+1][j+1] += diff

for i in range(H):
    for j in range(W):
        if A[i][j] != B[i][j]:
            print("No")
            exit()

print("Yes")
print(cnt)