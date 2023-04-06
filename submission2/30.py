K = int(input())

for A in range(-10**3,10**3):
    for B in range(-10**3,10**3):
        if A**5 - B**5 == K:
            print(A,B)
            exit()