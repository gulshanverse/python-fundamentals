def mul(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
p = int(input("Enter the number to print the table:  "))
print(mul(p))
