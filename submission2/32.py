N = int(input())
ans = 0
i = 1

while i*i <= 2*N:
    if 2*N%i == 0:
        x = i
        y = 2*N//i
        
        if x%2 != y%2:
            ans += 2
        
    i += 1
print(ans)      