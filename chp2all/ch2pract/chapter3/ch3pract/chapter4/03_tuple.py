#tuple
#A tuple is an ordered, immutable collection of elements in Python.
#Unlike lists, tuples cannot be modified after their creation.
#tuples are immutable, meaning their elements cannot be changed after creation.
#Tuples are defined by enclosing elements in parentheses () and separating them with commas.
from itertools import count


a = (20,"Apple",30.5,"Banana",True) #multiple element tuple
print(a)
b =(5,) #single element tuple
print(b)

t1 = (1,2,3,4,5)
print(t1)
print(type(t1))

print("Accessing elements in a tuple using indexing")
print(t1[0])  # Output: 1

print("slicing a tuple to get a sub-tuple") 
print(t1[1:4])  # Output: (2, 3, 4)

print("Finding the length of a tuple using len() function")
print(len(t1)) #output: 5

print("Iterating through a tuple using a for loop")
x = ("Radhe-Shyam",18700,729-2 ,True, "Love=\"I am in India\"")
for item in x:
    print(item)

#tuples do not have methods like append() or remove() because they are immutable
#However, you can use methods like count() and index() with tuples

s1 = (3673, "HaldiRam",78.79,"I am Parth",False,a==2,78.79,"PremanandBaba",78.79)
no = s1.count(78.79) #count gives how may times element is present in tuple
print(no)

i = s1.index("I am Parth") #index gives at which position element is present in tuple
print(i)



