#head recursion example: n to 1
def head_recursion(n):
    if n==0:
        return
    print("Before recursion: ", n)    #action hapens before recursive call
    head_recursion(n-1)

def main():
    number = int(input("Enter the number for number to 1: "))
    print("Head Recursion output:-")
    head_recursion(number)

main()