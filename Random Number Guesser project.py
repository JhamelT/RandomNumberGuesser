#The user is playing a guessing game with the computer. The computer has randomly chosen an integer between 1 and 25. The user is trying to guess the number correctly and the program tells them how many tries it took to get the right number.
#The computer chooses a number.
#The user is prompted to guess and enter a number. 
#When the guess is incorrect, the computer counts it as a try and prompts for another guess.
#When the guess is correct the program displays that the user got it right and how many guesses it took.
#The program ends when the guess is correct.
#print value in tries when the correct and or incorrect

import random

tries = 0
z =0
ran_num = random.randint(1, 25)
print(ran_num)
while z == 0:
    guess = int(input("Pick a number between 1 and 25: "))
    if guess == ran_num:
        print("Total tries ", tries)
        print("You guessed the correct number!")
        z += 1
    else:
        tries += 1
        print("That was not the picked number.")
    
game_running()
sys.exit("You have exited the program.")
game_running()
            
#Tells users how many tries it took for them to guess the number correctly.             

tries = 0
z =0
ran_num = random.randint(1, 25)
print(ran_num)
while z == 0:
    guess = int(input("Pick a number between 1 and 25: "))
    if guess == ran_num:
        print("Total tries ", tries)

