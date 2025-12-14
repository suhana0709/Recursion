def Maxarray(a):
    if len(a)==1:
        return a[0]
    return max(a[0] , Maxarray(a[1:]))

a = [1, 5, 7, 3, 98, 100, 68, 19]

print("Largest element of array:", Maxarray(a))