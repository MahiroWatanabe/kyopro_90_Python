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
ans = len(prime_factorize(N))

if ans == 1:
    print(0)
else:
    cnt = 0
    while pow(2,cnt) < ans:
        cnt += 1
    print(cnt)