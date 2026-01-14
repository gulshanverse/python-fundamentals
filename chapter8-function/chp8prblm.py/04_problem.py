#1.without recursion
def sum(n):
    return n*(n+1)//2
n = int(input("Enter the number: "))
print(f"sum of {n} natural number = {sum(n)}")


#2.with recursion 
def sum(n):
    if (n==0) :
        return 0
    else:
        return n + sum(n-1)
n = int(input("Enter the number: "))
print(f"sum of {n} natural number = {sum(n)}")
