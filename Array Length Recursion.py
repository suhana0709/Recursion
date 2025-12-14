def array_length(a):
    # Base Case: If the list is empty, return 0
    if not a:
        return 0
    else:
        return 1 + array_length(a[1:])


list = [4, 6, 9, 55, 64, 2, 98]
print("Length of the list: ",array_length(list))
