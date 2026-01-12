#function definition
def avg():
    a = int(input("Enter your number:  "))
    b = int(input("Enter your number:  "))
    c = int(input("Enter your number:  "))
    average =(a+b+c)/3
    print("Average: ",average)
    return average
a = avg()   #function call
print("Hey this", a*3)

#1 a function is a group of statements performing a specific task.
#2 when a program gets bigger in size and its complexity grows,it gets difficult for a 
#..program to keeo track on which piece of code is doing what!
#3 a functio n can be reused by the programmer in a given program any number of times
"""
def fun():
    print("Hello")

"""
#function call
"""
fun() 
"""
