def arrayTotalsum(a):
    length = len(a)
    if length==1:
        return a[0]
    return a[0] + arrayTotalsum(a[1:])

a = [5, 6, 8]
print("Total array sum: ", arrayTotalsum(a))