p1 = "money"
p2 = "buy now"
p3 = "click this"
p4 = "subscribe this"
comment = input("Enter your comment: ")
if(p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment):
    print("This is a spam comment")
else:
    print("This is not a spam comment")
print("End of the program")