def take_input():
    num = int(input("Enter a number: "))
    if (num<0):
        print("Negative number entered. Stopping.........")
        return
    print("Number entered: ",num)
    take_input()

take_input()