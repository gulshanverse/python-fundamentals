#detect double spaces in a string
s = "Hey Parth!  How can I help you"
print(s.find("  "))  # finding index of double spaces

print(s.find("good")) # finding index of substring not present
print(s.index("Parth"))  # finding index of substring present
print(s.replace("  ", " "))  # replacing double spaces with single space
print(s.endswith("you"))  # checks if the string ends with 'you'
print(s.count("a"))  # counts occurrences of 'a' in the string
print(s.expandtabs(tabsize=4))  # expands tabs to spaces
print(s.isprintable())  # checks if all characters in the string are printable


name = "Gulshan  Kumar is a  good boy and he is  very smart"
double_spaces = name.find("  ")
print("Index of double spaces is:", double_spaces) # Output: Index of double spaces
#above line will give index of first occurrence of double spaces
while double_spaces != -1:
    print("Double spaces found at index:", double_spaces)
    double_spaces = name.find("  ", double_spaces + 1)

print(name) #strings are immutable so original string will remain unchanged
