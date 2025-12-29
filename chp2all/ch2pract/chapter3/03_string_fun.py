name = "Alice"
print(name.upper())        # ALICE Return a copy of the string converted to uppercase.
print(name.lower())        # alice Return a copy of the string converted to lowercase.
print(name.capitalize())   # Alice Return a copy of the string with its first character capitalized and the rest lowercased.
print(name.title())        # Alice Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
print(name.replace("A", "E"))  # Elice Return a copy of the string with all occurrences of substring old replaced by new.
print(name.find("l"))     # 2 Return the lowest index in the string where substring sub is found.
print(name.rfind("e"))    # 4 Return the highest index in the string where
print(name.count("i"))    # 1 Return the number of non-overlapping occurrences of substring sub in the string.
print(name.startswith("A"))  # True Return True if the string starts with the specified prefix.
print(name.endswith("e"))    # True     Return True if the string ends with the specified suffix.
print(name.split("i"))    # ['Al', 'ce'] Return a list of the words in the string, using sep as the delimiter string.
print(name.splitlines())  # ['Alice'] Return a list of the lines in the string
print("-".join(["A", "l", "i", "c", "e"]))  # A-l-i-c-e Join the elements of an iterable to the end of the string.
print(name.strip())       # Alice Return a copy of the string with leading and trailing whitespace removed
print(f"Length of the name is: {len(name)}")  # Length of the name is: 5    
print(name.center(20, '*'))  # *******Alice******** Center the string in a field of given width.
print(name.ljust(20, '-'))   # Alice--------------- Left-justify the string in a field of given width.
print(name.rjust(20, '-'))   # ---------------Alice Right-justify the string in a field of given width.
print(name.strip("A"))      # lice Return a copy of the string with the leading and trailing characters removed.
print(name.isalpha())      # True   Return True if all characters in the string are alphabetic.         
print(name.isdigit())      # False  Return True if all characters in the string are digits.
print(name.islower())      # False Return True if all cased characters in the string are lowercase.
print(name.isupper())      # False Return True if all cased characters in the string are uppercase.
print(name.istitle())      # True  Return True if the string is a titlecased string.
print(name.swapcase())     # aLICE Return a copy of the string with uppercase characters converted to lowercase and vice versa.
print(name.count("l", 0, 3))  # 1 Return the number of non-overlapping occurrences of substring sub in the string.
print(name.index("i"))    # 3         
print(name.encode())       # b'Alice'        
print(name.encode('ascii'))  # b'Alice'  
print(name.partition("i"))  # ('Al', 'i', 'ce')
print(name.rpartition("i")) # ('Al', 'i', 'ce')
print(name.zfill(10))      # 00000Alice
print(name.translate(str.maketrans("A", "E")))  # Elice
print(name.expandtabs(tabsize=4))  # Alice
print(name.removeprefix("Al"))  # ice
print(name.removesuffix("ce"))   # Ali
print(name.isprintable())  # True
print(name.isidentifier()) # True
print(name.casefold())    # alice
print(name.encode('utf-8'))  # b'Alice'
print(name.format())      # Alice
print(name.format_map({}))  # Alice
print(name.partition("x"))  # ('Alice', '', '')
print(name.rfind("i"))    # 3
print(name.zfill(8))      # 000Alice
print(name.center(30))    #             Alice
print(name.lstrip("A"))   # lice 
print(name.rstrip("e"))   # Alic 
print(name.isascii())     # True
print(name.isnumeric())   # False
print(name.isdecimal())   # False
print(name.isalnum())     # True
print(name.startswith("Al"))  # True
print(name.endswith("ce"))    # True
print(name.splitlines())  # ['Alice']
print(name.join(["Hello ", "!"]))  # Hello Alice!
print(name.replace("i", "y"))  # Alyce
print(name.find("x"))     # -1
print(name.count("l"))    # 2


