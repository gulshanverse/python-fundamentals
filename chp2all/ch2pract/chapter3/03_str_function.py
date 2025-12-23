name = "gulshan kumaryadav"
print(len(name))
print(name.endswith("n")) #true
print(name.startswith("gul")) # false

print(name.capitalize())
#Purpose: Convert string to lowercase or uppercase
s = "Python"
print(s.lower())  # python
print(s.upper())  # PYTHON

#Purpose: Removes whitespace from beginning and end
s = "   hello   "
print(s.strip())  # "hello"

#.replace(old, new)
#Purpose: Replace a substring with another
s = "I like Java"
print(s.replace("Java", "Python"))  # I like Pythoner-  
#Purpose: Split a string into a list of substrings based on a delimiter
s = "apple,banana,cherry"   