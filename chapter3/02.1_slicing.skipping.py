 #name[start : stop : step]
name = "Gulshankumar"
print(name[1:10:6])

#slicing a string 
s = "PYTHON"

print(s[0:4])   # PYTH
print(s[2:])    # THON
print(s[:3])    # PYT


#Slicing a list
nums = [10, 20, 30, 40, 50]

print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[3:])    # [40, 50]

#Step slicing (this is where power kicks in)
nums = [1, 2, 3, 4, 5, 6]

print(nums[::2])   # [1, 3, 5]
print(nums[1::2])  # [2, 4, 6]



