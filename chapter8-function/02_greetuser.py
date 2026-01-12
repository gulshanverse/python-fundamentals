#function without agument(Taking input from user)
n = input("Enter your name: ")
def hello():
    print(f"Good Morning,{n}")
hello()

#function with argument/parameter
def hi(name):
    print(f"Good Day,{name}")
hi("Gulshan")
hi("Parth Krishna")

#function with multiple argument
def hey(name,ending):
    print("Good Morning," +name)
    print(ending)
hey("Gulshan","Thank You!")
hey("I am Parth.","How are you?")

#return 
def hey(name,ending):
    print("Good Morning," +name)
    print(ending)
    return "Byee"
a = hey("Gulshan","Thank You!")
print(a)


