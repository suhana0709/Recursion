complexity = 0   

def fac(n):
    global complexity
    if n == 1 or n == 0:
        return 1
    complexity += 1
    return n * fac(n - 1)

def print1to10(n):
    global complexity
    if n > 10:
        return
    print(n)
    complexity += 1
    print1to10(n + 1)

fac(5)
print1to10(1)

print("Time complexity:", complexity)
