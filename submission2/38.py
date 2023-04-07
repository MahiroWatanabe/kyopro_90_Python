def calc_or(left,right):
    result = 0
    for i in range(left,right):
        result = result | A[i]
    return result

def do(bit):
    if bit&1 == 0 or bit>>N&1 == 0:
        return 2**40
    
    partitions = []
    for i in range(N+1):
        if (bit >> i) & 1:
            partitions.append(i)
    
    ans_temp = 0
    for i in range(len(partitions)-1):
        ans_temp = ans_temp ^ calc_or(partitions[i],partitions[i+1])
        
    return ans_temp

N = int(input())
A = list(map(int,input().split()))
ans = 2**40

for bit in range(2**(N+1)):
    ans = min(ans,do(bit))

print(ans)