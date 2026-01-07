#write a program to find the greatest of three numbers entered by the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))
if(a>=b and a>=c and a>=d and a>=e):
    print("The greatest number is:",a)
elif(b>=a and b>=c and b>=d and b>=e):
    print("The greatest number is:",b)
elif(c>=a and c>=b and c>=d and c>=e):
    print("The greatest number is:",c)
elif(d>=a and d>=b and d>=c and d>=e):
    print("The greatest number is:",d)
else:
    print("The greatest number is:",e)
