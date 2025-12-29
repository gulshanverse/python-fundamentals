#list can store value of any datatypes 
#unlike strings, lists are mutable, meaning their elements can be changed after creation.
#Lists are defined by enclosing elements in square brackets [] and separating them with commas.
fruits =["apple", 50, "banana",10.26, "cherry",2508,48]
print(fruits)
#Accessing elements in a list using indexing
print(fruits[0])  # Output: apple

print("Modifying elements in a list")
fruits[1] = 60
print(fruits)  # Output: ['apple', 60, 'banana', 10.26, 'cherry', 2508, 48]

print("Adding elements to a list using append() method")
fruits.append("orange")
print(fruits)  # Output: ['apple', 60, 'banana', 10.26, 'cherry', 2508, 48, 'orange']

print("Removing elements from a list using remove() method")
fruits.remove("banana")

print("slicing a list to get a sublist")
print(fruits[1:4])  # Output: [60, 10.26, 'cherry']

print(fruits)  # Output: ['apple', 60, 10.26, 'cherry', 2508, 48, 'orange'] 

print("Finding the length of a list using len() function")
print(len(fruits))  # Output: 7 #it is total number of elements in the list

#Iterating through a list using a for loop
for itemss in fruits:
    print(itemss) 
