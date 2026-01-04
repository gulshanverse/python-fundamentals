marks = {
    "Gulshan": 100,
    "Krishna": 98,
    "Aparna": 78.50,
    "Priya" : 79
}
print(type(marks))
# print(marks["Priya"]) #accessing value using key

# #propeties of dictionary
# #0. Dictionaries are defined using curly braces {} with key-value pairs separated by commas.
# #1. Dictionaries are unordered collections of key-value pairs.
# #2. Keys must be unique and immutable (e.g., strings, numbers, tuples).
# #3. Values can be of any data type and can be duplicated.
# #4. Dictionaries are mutable, meaning you can change their content without changing their identity.
# marks.update({"Aparna" : 90})
# print("Updated Marks:", marks) #updated already existing key value pair
# print("Addeing the New Member:")
# marks.update({"Divyam": 70}) #adding new key value pair
# print("Dictionary after adding new members:", marks)

# #5. Accessing values is done using keys, not indices.
# print(marks["Priya"]) #accessing value using key

# #6. Dictionaries can be nested, meaning a dictionary can contain other dictionaries as values.
# marks_nested = {
#     "Gulshan" : {"Maths": 100, "PDS": 99.50},
#     "Pragati" : {"Maths": 98, "PDS": 95},
#     "Swati Mehra" : {"Maths": 97, "PDS": 96, "OS": 98, "DAA": 99}
# }
# print("Nested Dictionary:", marks_nested)
# #7. Common methods include .keys(), .values(), .items(), .get(), .update(), and .pop().
# #(i) .key method
# print("Keys in marks dictionary:", marks.keys())
# #(ii) .values method
# print("Values in marks dictionary:", marks.values())
# #(iii) .items method
# print("Items in marks dictionary:", marks.items())
# #(iv) .get method
# print(marks.get("Gulshan")) #accessing value using get method
# some difference between accessing value .get() and using [] method
print(marks.get("Priyaanka")) #accessing non existing key using get method will return None
#print(marks["Priyaanka"]) #accessing non existing key using [] will raise error
#(v) .pop method
removed_value = marks.pop("Krishna")
print("Removed Value:", removed_value)
print("Dictionary after popping Krishna:", marks)
removed_item = marks[79] #
print("Removed Item:", removed_item)
print("Dictionary after popping item with value 79:", marks)

#8. Dictionaries are optimized for fast lookups, making them efficient for retrieving values based on keys.
#9. Dictionaries can be created using the dict() constructor as well.
#10. Iterating over a dictionary can be done using loops to access keys, values, or key-value pairs.
#11 . Dictionary comprehensions provide a concise way to create dictionaries.

