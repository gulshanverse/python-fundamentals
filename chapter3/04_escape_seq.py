1#\n is usedfor new line
a = "Gulshan is a very smart boy.\nHe studies very hard.\nHe always help others."
print(a)
2#\t is used for tab space
b = "Parth is a very hardworking student.\tHe always scores good marks.\tHe is a brillent student with hardworking mindset."
print(b)

3#\\ is used to print backslash
c = "This is a backslash symbol: \\"
print(c)
4#\' is used to print single quote
d = 'It\'s a beautiful day.' #when the string is enclosed in single quotes.
print(d)
5#\" is used to print double quote
e = "He said, \"Python is my favorite programming language.\" "
print(e)

6#\r is used for carriage return
f = "HelloWorld!\rPython is awesome." #it will replace 'HelloWor' with 'Python is'
print(f)
7#\b is used for backspace
g = "Hello\bWorld!" #it will remove the character before \b, so 'o' will be removed.
print(g)
8#\f is used for form feed
h = "Hello\fWorld!" # it will insert a form feed between Hello and World
print(h)

print("End of escape sequence examples.")

9#\v is used for vertical tab
i = "Hello\vWorld!" 
print(i)

10#\ooo is used to represent octal value
j = "This is an octal value: \101"  # \101 is octal for 'A'
print(j)
11#\xhh is used to represent hexadecimal value
k = "This is a hexadecimal value: \x41"  # \x41 is hexadecimal for 'A'
print(k)

# Unicode escape sequences
print("\U0001F600")   # 😀
print("\u2764")      # ❤
print("\u03A9")      # Ω
print("\u00A9")     # ©
print("\u20B9")    # ₹

# Null character
print("Hello\0World")


