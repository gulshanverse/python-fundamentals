# def gr8(a,b,c):
#     if(a>=b and a>c):
#         print(f"{a} is greatest number.")
#     elif(b>=a and b>c):
#         print(f"{b} is greatest number.")
#     else:
#         print(f"{c} is greatest number.")
# p = gr8(8,78,78)



def gr8(a,b,c):
    if(a>=b and a>c):
        return a
    elif(b>=a and b>c):
        return b
    else:
        return c
a = 56
b = 67
c = 97
print(gr8(a,b,c))


