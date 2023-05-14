from easygui import *
from mc_dictionary_v1 import monster_cards



#while True:
    #strength = int(enterbox('Enter the strength of the character'))
    #if strength >= 25:
        #msgbox("You can't enter a number greater than 25 strength")
    #else:
        #break




while True:
    cardname = enterbox('Enter the name of the card you would like to add')
    
    
    strength = int(enterbox('Enter the strength of the character'))
    if strength >= 25:
        msgbox("You can't enter a number greater than 25 strength")
    else:
        break
    
   
    speed = int(enterbox('Enter the speed of the character'))
    if speed >= 25:
        msgbox("You can't enter a number greater than 25 speed")
    else:
        break

    stealth = int(enterbox('Enter the stealth of the character'))
    if stealth >= 25:
        msgbox("You can't enter a number greater than 25 stealth")
    else:
        break

    cunning = int(enterbox('Enter the cunning of the character'))
    if cunning >= 25:
        msgbox("You can't enter a number greater than 25 cunning6")
    else:
        break


    monster_cards[cardname] = {
        'strength': [strength],
        'speed': [speed],
        'stealth': [stealth],
        'cunning': [cunning]
    }


