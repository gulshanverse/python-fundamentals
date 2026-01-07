a = {50: "fifty",
     60: "sixty",
     70: "seventy"  
}
#above is also a dictionary with integer keys and string values
print(type(a))
print(a[60]) #accessing value using key
#you can have mixed key value pairs in a dictionary
mydict = {
    "name": "Gulshan",
    1: [2, 3, 4],#list as value
    (1, 2): "tuple as key",
    3.5: "float as key"
}
print("My Dictionary:", mydict)
print("Accessing value using string key 'name':", mydict["name"])
print("Accessing value using integer key 1:", mydict[1])

#empty dictionary
empty_dict = { }
#or you can also use empty_dict = dict()
empty_dict1 = dict()
print("Empty Dictionary:", empty_dict)