#loop statement
for i in range(1,100):
    print(i)

n = int(input("Enter a number in between 0 and 999: "))

if n < 0 or n > 999:
    print("Invalid Number! Enter a number in between 0 annd 999")
elif (n < 10):
    print(n, "is one digit number")
elif (n < 100):
    print(n,"is two digit number")
else:
    print(n,"is three digit number")


