# write a program to check whether a student has passed or failed.
# A student is considered to have passed if he/she has scored at least 33% 
# in each subject and an overall average of at least 40%. 
# Assume there are three subjects.
a = int(input("Marks in Subject 1:"))
b = int(input("Marks in Subject 2:"))
c = int(input("Marks in Subject 3:"))
if(a%100>=33 and b%100>=33 and c%100>=33 and (a+b+c)/3>=40):
    print("You have passed the exam")
else:
    print("You have failed the exam")
