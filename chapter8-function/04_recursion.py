#recursion
#1. recursion is a functiom which calls itself
# factorial(n) = n* factorial(n-1)
'''
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 x 2 X 1
factorial(4) = 4 x 3 x 3 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1

factorial(n) = n*factorial(n-1)

'''
def fact(n):
    if (n==0 or n ==1):
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter the number: "))
print(f"Factorial of {n} = {fact(n)}")




