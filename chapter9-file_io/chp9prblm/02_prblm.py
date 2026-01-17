#2. The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file 'Hi--score.txt' which is either blank or contains the previous

import random
def game():
    print("You are playing the game.")
    score = random.randint(1,62)
    # Fetch the hisghcore
    with open("highscore")
    