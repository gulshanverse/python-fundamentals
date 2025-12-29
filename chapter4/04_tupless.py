t = (1, 2, 3)
a =(9,88,62)
#concatenate two tuples
c = t + a
print(c)

#repeat tuple elements
r = t*3
print(r)
k = a*2
print(k)
j = r + k
print(j) #output: (1, 2, 3, 1, 2, 3, 1, 2, 3, 9, 88, 62, 9, 88, 62)

#check membership using 'in' keyword
print(2 in t)  # Output: True
print(5 in a)  # Output: False

#unpacking tuples
x = (10, 20, 30)
p, q, r = x
print(p)  # Output: 10
print(q)  # Output: 20  
print(r)  # Output: 30

#nested tuples
nested = (1, 2, (3, 4), (5, 6))
print(nested[2])  # Output: (3, 4) #accessing nested tuple using indexing
print(nested[2][1])  # Output: 4 #accessing element 4 from nested tuple

#tuple with different data types
mixed = (1, "Hello", 3.14, True)
print(mixed)  # Output: (1, 'Hello', 3.14, True)
print(type(mixed))  # Output: <class 'tuple'>

#tuple inside a list
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
print(list_of_tuples)  # Output: [(1, 2), (3, 4), (5, 6)]
#accessing elements in tuple inside a list
print(list_of_tuples[1])  # Output: (3, 4)
print(list_of_tuples[1][0])  # Output: 3

#