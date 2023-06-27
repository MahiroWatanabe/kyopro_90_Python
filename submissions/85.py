'リスト形式で約数を全部表示'
def calc_divisors(N):
    res = []

    for i in range(1, N + 1):
        if i * i > N:
            break
        
        if N % i != 0:
            continue

        res.append(i)

        if N // i != i:
            res.append(N // i)

    res.sort()
    return res

K = int(input())
D = calc_divisors(K)
ans = 0

for a in D:
    for b in D:
        c = K//(a*b)
        if a <= b <= c <= K and a*b*c == K:
            ans += 1

print(ans)