#1. Write a program to  read the text from agiven file 'poem.txt' and find out whether it contains the word 'twinkle'.

f = open("poem.txt")
content = f.read()
if("Twinkle " in content):
    print("The Word Twinkle is present in the content. ")
f.close()



