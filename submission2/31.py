N,K = map(int, input().split())
R,S,P = map(int, input().split())
T = input()
point = 0
pre = []

for i in range(N):
    if i <= K-1:
        if T[i] == "r":
            point += P
            pre.append("p")
        elif T[i] == "s":
            point += R
            pre.append("r")
        elif T[i] == "p":
            point += S
            pre.append("s")
    else:
        if T[i] == "r":
            if pre[i-K] =="p":
                pre.append("x")
            else:
                point += P
                pre.append("p")
        elif T[i] == "s":
            if pre[i-K] == "r":
                pre.append("x")
            else:
                point += R
                pre.append("r")
        elif T[i] == "p":
            if pre[i-K] == "s":
                pre.append("x")
            else:
                point += S
                pre.append("s")

print(point)