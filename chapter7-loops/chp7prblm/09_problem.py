'''
***
* *
***
'''

# for i in range(0,3):
#     if(i==1):
#         print("*","*")
#     else:
#         print("*"*3)

#for any number of n

n = int(input("Enter the number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*",end = "")
        print(" "*(n-2),end="")
        print("*",end = "")
    print()