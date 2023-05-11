from easygui import *

monster_cards = {
    "Stoneling": {
        'strength': 7,
        'speed': 1,
        'stealth': 25,
        'cunning': 15
    },
    'Vexscream': {
        'strength': 1,
        'speed': 6,
        'stealth': 21,
        'cunning': 19
    },
    'Dawnmirage': {
        'strength': 5,
        'speed': 15,
        'stealth': 18,
        'cunning': 22
    },
    'Blazegolem': {
        'strength': 15,
        'speed': 20,
        'stealth': 23,
        'cunning': 6
    },
    'Websnake': {
        'strength': 7,
        'speed': 15,
        'stealth': 10,
        'cunning': 5
    },
    'Moldvine': {
        'strength': 21,
        'speed': 18,
        'stealth': 14,
        'cunning': 5
    },
    'Vortexswing': {
        'strength': 19,
        'speed': 13,
        'stealth': 19,
        'cunning': 5
    },
    'Rotthing': {
        'strength': 16,
        'speed': 7,
        'stealth': 4,
        'cunning': 12
    },
    'Froststep': {
        'strength': 14,
        'speed': 14,
        'stealth': 17,
        'cunning': 4
    },
    'Wispghoul': {
        'strength': 17,
        'speed': 19,
        'stealth': 3,
        'cunning': 2
    }
}



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


