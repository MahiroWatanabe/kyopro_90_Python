def price(N):
    N_str = str(N)
    d = len(N_str)
    return A*N + B*d

A,B,X = map(int, input().split())

if X < price(1):
    print(0)
    exit()

left = 1
right = 20**20

while right-left > 1:
    mid = (left+right)//2
    if price(mid) <= X:
        left = mid
    else:
        right = mid

if 10**9 < left:
    left = 10**9

print(left)