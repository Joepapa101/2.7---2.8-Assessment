from easygui import *
from mc_dictionary_v1 import monster_cards


while True:
    cardname = enterbox('Enter the name of the card you would like to add')
    
    while True:
        strength = enterbox('Enter the strength of the character')
        if not strength.isdigit():
            msgbox('Please enter an integer')
        elif int(strength) >= 25:
            msgbox("You can't enter a number greater than 25 strength")
        else:
            break
    
    while True:
        speed = enterbox('Enter the speed of the character')
        if not speed.isdigit():
            msgbox('Please enter an integer')
        elif int(speed) >= 25:
            msgbox("You can't enter a number greater than 25")
        else:
            break

    while True:
        stealth = enterbox('Enter the stealth of the character')
        if not stealth.isdigit():
            msgbox('Please enter an integer')
        elif int(stealth) >= 25:
            msgbox("You can't enter a number greater than 25")
        else:
            break

    while True:
        cunning = enterbox('Enter the cunning of the character')
        if not cunning.isdigit():
            msgbox('Please enter an integer')
        elif int(cunning) >= 25:
            msgbox("You can't enter a number greater than 25")
        else:
            break


    monster_cards[cardname] = {
        'strength': [strength.int],
        'speed': [speed.int],
        'stealth': [stealth.int],
        'cunning': [cunning.int]
    }