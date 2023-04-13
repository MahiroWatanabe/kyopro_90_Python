def oct_num(i):
    s = ""
    while i > 0:
        s = str(i % 10) + s
        i //= 10

    return s


def kyu_num(i):
    s = ""
    while i > 0:
        s = str(i % 9) + s
        i //= 9

    return s


N, K = map(int, input().split())

for _ in range(K):
    new_oct_num = oct_num(N)
    print(new_oct_num)
