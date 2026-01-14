# celcius to fahrenheit conversion
def tempinC(c):
    f = (c*9/5) + 32
    print(f"{c} degree celcius = {f} degree fahrenheit")
t = float(input("Enter the temperature in celcius: "))
tempinC(t)

# fahrenheit to celcius conversion
def tempinC(f):
    c = (f-32)*5/9
    print(f"{f} degree fahrenheit  = {c} degree celcius")
t = float(input("Enter the temperature in fahrenheit: "))
tempinC(t)