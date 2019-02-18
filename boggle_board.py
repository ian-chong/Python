import random
import string

def board():
    letter = random.choice(string.ascii_uppercase)
    letter1 = random.choice(string.ascii_uppercase)
    letter2 = random.choice(string.ascii_uppercase)
    letter3 = random.choice(string.ascii_uppercase)
    letter4 = random.choice(string.ascii_uppercase)
    letter5 = random.choice(string.ascii_uppercase)
    letter6 = random.choice(string.ascii_uppercase)
    letter7 = random.choice(string.ascii_uppercase)
    letter8 = random.choice(string.ascii_uppercase)
    letter9 = random.choice(string.ascii_uppercase)
    letter10 = random.choice(string.ascii_uppercase)
    letter11 = random.choice(string.ascii_uppercase)
    letter12 = random.choice(string.ascii_uppercase)
    letter13 = random.choice(string.ascii_uppercase)
    letter14 = random.choice(string.ascii_uppercase)
    letter15 = random.choice(string.ascii_uppercase)
    
    board = [[letter, letter1, letter2, letter3],
            [letter4, letter5, letter6, letter7],
            [letter8, letter9, letter10, letter11],
            [letter12, letter13, letter14, letter15]]

    for i in board:
        for j in i:
            if j == "Q":
                j = "Qu"
                print(j, end = "  ")
            elif j != "Q":
                print(j, end = "  ")
        print()    

board()

