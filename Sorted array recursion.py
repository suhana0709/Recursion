def checksorted(a):
    length = len(a)
    if length==1 or length==0:
        return True
    return a[0] <= a[1] and checksorted(a[1:])

a =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if checksorted(a):
    print("Yes,the given list is sorted.")
else:
    print("No, the given list is not sorted.")