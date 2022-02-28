import random
from datetime import date

print('Guessing game')

'''SMALL MINI GAME TO GUESS NUMBER IN 3 TRIES '''

chances=3
seed_val=int(str(date.today()).replace("-",""))
random.seed(seed_val)
number=random.randint(1,100)
wrong=True
guess=0
while wrong and chances>0:
    guess=int(input(f"Enter your guess between 1 to 100: [Chances: {chances}]"))
    print(f"Guess {chances} is {guess}")
    if guess == number:
        wrong=False
    elif guess > number:
        print("Guess {guess} too high from the correct answer ")
    else: 
        print("Guess {guess} is low to the correct answer ")
    chances-=1
    

if wrong == True:
    print(f"Sorry you loose! Correct Answer: {number}")
else:
    print("Congrats you won!")


