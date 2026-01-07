a = int(input("Enter your age: "))
# If stsement number 1
if(a%2 == 0):
    print("a is even")
# End of statement 1
# If stsemnet number 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you!")
elif(a<0):
    print("You are entering an invalid age")
elif(a==0):
    print("You are entering 0 which is not a valid age")
else:
    print("You are below the age of consent")
# End of the statement 2
    
print("End of the program")

#there can be any number of elif statements.
#last else is executed only if all the conditions inside elif fails
