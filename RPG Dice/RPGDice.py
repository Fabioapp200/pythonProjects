#RPG Dice system
#by Fábio Pinto

import random

def rollDice():
    dice = input(f'\nChoose a dice to roll.(d2, d4, d6, d8, d10, d12, d20, d100)\n')

    if str(dice.lower())[0].isalpha():
        rollSingleDie(dice)
    elif str(dice.lower())[0].isnumeric():
        rollMultiDice(dice)
    else:
        print('To roll a single die use the prefix "d"')
    playAgain()
    
def rollSingleDie(dice):
    
    splitText = dice.split('+',1)
    
    if str(dice.lower())[0] == 'd':
        diceNumber = str(dice.lower())
        diceNumber = diceNumber[1:3]
        diceNumber = int(diceNumber)
        result = random.randint(1,diceNumber)
        if len(splitText) > 1:
            diceModifier = int(splitText[1])
            print(f'\nYou rolled a {dice.lower()}')
            print(f'Your result is: {result} + {diceModifier} = {result+diceModifier}')
        else:
            print(f'\nYou rolled a {dice.lower()}')
            print(f'Your result is: {result}')
        
    else:
        print('To roll a single die use the prefix d')

def rollMultiDice(dice):
    
    split_DiceModifier = dice.split('+')
    
    if len(split_DiceModifier) == 2:
        diceIndexNumber = split_DiceModifier[0]
        split_IndexNumber = diceIndexNumber.split('d',1)
        diceIndex = int(split_IndexNumber[0])
        diceNumber = int(split_IndexNumber[1])
        diceModifier = int(split_DiceModifier[1])
        totalRoll = 0
        rollNumber = 0
        for x in range(diceIndex):
            currentRoll = random.randint(1,diceNumber)
            totalRoll+=currentRoll
            rollNumber+=1
            print(f'Roll #{rollNumber}: {currentRoll}')
        print(f'And your total roll is: {totalRoll} + {diceModifier} = {totalRoll+diceModifier}')
    elif len(split_DiceModifier) == 1:
        diceIndexNumber = split_DiceModifier[0]
        split_IndexNumber = diceIndexNumber.split('d',1)
        diceIndex = int(split_IndexNumber[0])
        diceNumber = int(split_IndexNumber[1])
        totalRoll = 0
        rollNumber = 0
        for x in range(diceIndex):
            currentRoll = random.randint(1,diceNumber)
            totalRoll+=currentRoll
            rollNumber+=1
            print(f'Roll #{rollNumber}: {currentRoll}')
        print(f'And your total roll is: {totalRoll}')
    else:
        print('To roll multiple dice, use "XdY + Z"')

def playAgain():
    playAgain = input(f'\nDo you wish to roll again? (y/n)\n')

    if playAgain == 'y':
        rollDice()
    elif playAgain =='n':
        input(f'Press any key to exit\n')

rollDice()