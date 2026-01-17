''' 
1 for snake
-1 for water
0 for gun

'''
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1,"w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]

# By now we have 2 numbers(variables),you and computer
print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

result = you - computer

if (computer == you):
    print("Draw!")

# """ if (computer == -1 and you == 1):(computer - you) = -2
#         print("You Win!")
#     elif(computer == -1 and you == 0):(computer - you) = -1
#         print("You Lose")
#     elif (computer == 1 and you == -1):(computer - you) = 2
#         print("You Lose!")
#     elif(computer == 1 and you == 0):(computer - you) = 1
#         print("You Win")
#     elif (computer == 0 and you == -1):(computer - you) = 1
#         print("You Win!")
#     elif(computer == 0 and you == 1):(computer - you) = -1
#         print("You Lose")
#     else:
#         print("Something went wrong") 
# The Below logic is written on the basis of the value of compter - you
# """
elif result == 1 or -2 :
    print("You Win!")
else:
    print("You Lose!")
