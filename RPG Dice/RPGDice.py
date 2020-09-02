#RPG Dice system
#by Fábio Pintoa

import random



def rollDice():
    dice = input(f'Choose a dice to roll.\n')

    if str(dice.lower())[0].isalpha():
        rollSingleDie(dice)
    if str(dice.lower())[0].isnumeric() and str(dice.lower())[1] == 'd':
        rollMultiDice(dice)
    
    playAgain = input(f'Do you wish to roll again? (y/n)\n')

    if playAgain == 'y':
        rollDice()
    elif playAgain =='n':
        input(f'Press any key to exit')



def rollSingleDie(dice):
    if str(dice.lower())[0] == 'd':
        diceNumber = str(dice.lower())
        diceNumber = diceNumber[1:3]
        diceNumber = int(diceNumber)
        print(random.randint(1,diceNumber))
    else:
        print('To roll a single die use the prefix d')


def rollMultiDice(dice):
    diceIndex = int(dice[0])
    diceNumber = int(dice[2:5])
    totalRoll = 0
    rollNumber = 0
    for x in range(diceIndex):
        currentRoll = random.randint(1,diceNumber)
        totalRoll+=currentRoll
        rollNumber+=1
        print(f'Roll #{rollNumber}: {currentRoll}')
    print(f'And your total roll is: {totalRoll}')


rollDice()



