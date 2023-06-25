def to9(num,v):
    res = ""
    while True:
        if num == 1:
            res = "1" + res
            break
        elif num == 0:
            break
        res = str(num%v) + res
        num //= v
        
    return res if res != "" else "0"

def f(num):
    num = int(num,8)
    num = to9(num,9)
    num = num.replace("8","5")
    return num

N,K = map(int, input().split())
N = str(N)

for i in range(K):
    N = f(N)

print(N)