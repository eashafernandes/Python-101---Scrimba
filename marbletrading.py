import random

print("Marble Game!")
bag = ("green","green","green","green","green","black","red","red","red","white")
start_purse = 1000
purse = start_purse
result=0
rounds = 3
marble = "none"
print(f"You start the game with {start_purse} gold pieces")
for draw in range(1, rounds+1):
    bet = int(input(f"Current Purse: {purse} Last Draw: {marble} \n Round {draw} - How much do you want to bet?: "))
    marble = random.choice(bag)
    if marble == "green":
        print("Green Marble")
        print(f"Congrats! You win {bet}! Adding to purse~")
        result = bet
        purse+=result
    elif marble == "black":
        print("Black Marble")
        result = 10 * bet
        print(f"Congrats! You win {result}! Adding to purse~")
        purse+=result
    elif marble == "white":
        print("White Marble")
        result = -5 * bet
        print(f"Sorry :( ! You loose {result}! Deducting from purse~")
        purse-=result
    else:
        print("Red Marble")
        print(f"Sorry :( ! You loose {bet}! Deducting from purse~")
        result= -bet
        purse-=result
    if purse < (start_purse/2):
        print("Purse value less! Exiting game")
        break
    print(f"Purse Amount: {purse}, Last Result: ({marble}): {result}")
    print('')
# print final results
print('Starting/ Ending Purse Value: ', start_purse, '/',purse)
print('Gain/Loss: ', ((purse-start_purse)/start_purse *100),'%')
      
