def inch2cm(i):
    return i*2.54
n = float(input("Enter value in inches: "))
m = inch2cm(n)
print(f"{n} inches = {m} cm")