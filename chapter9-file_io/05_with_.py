f = open("myFiles")
print(f.read())
f.close()

#  The same can be written using with statement like this
with open("myFiles","r") as f:
    #read the content of the file
    text = f.read
# Print the contents
print(text)