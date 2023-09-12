# prompts user for a value X and stores it in an interger and stores it in the value X
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

# n times itself is literally a number timed by itself and with the return keyword is returns value. 
# different ways to solve this problem like (n ** 2) and the function pow(n, 2) first is the number and second is the exponent.  
def square(n):
    return n * n

main()