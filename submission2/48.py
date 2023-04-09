N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]
pointX_conv = []
pointY_conv = []

for x,y in point:
    pointX_conv.append(x+y)
    pointY_conv.append(x-y)

X_max = abs(max(pointX_conv)-min(pointX_conv))
Y_max = abs(max(pointY_conv)-min(pointY_conv))

print(max(X_max,Y_max))