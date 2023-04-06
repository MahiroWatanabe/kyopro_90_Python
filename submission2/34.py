def prime_factorize(N):
    if N == 1:
        return [1]
    prime_list = []
    i = 2
    while i*i <= N:
        if N%i == 0:
            prime_list.append(i)
            N //= i
        else:
            i += 1
    if N != 1:
        prime_list.append(N)
    
    return prime_list

N = int(input())

if N == 1:
    print(0)
    exit()

prime_N = set(prime_factorize(N))
ans = 0

for p in prime_N:
    for e in range(1,10**10):
        if N % (p**e) == 0:
            ans += 1
            N //= p**e
        else:
            break

print(ans)