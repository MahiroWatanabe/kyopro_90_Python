n,a,b = map(int, input().split())
mod = 10**9+7

def nCr_mod(n,r,mod):
    numerator = 1
    for i in range(n-r+1,n+1):
        numerator *= i
        numerator %= mod
    
    denominator = 1
    for i in range(1,r+1):
        denominator *= i
        denominator %= mod
    
    denominator_inv = pow(denominator,-1,mod)
    
    return numerator*denominator_inv

ans = pow(2,n,mod)
ans -= 1
ans -= nCr_mod(n,a,mod)
ans -= nCr_mod(n,b,mod)
ans %= mod
print(ans)