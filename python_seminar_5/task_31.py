number = 7

def numberF(n):
    if n <= 1:
        return 1
    return numberF(n-1) + numberF(n-2)

print(numberF(number))