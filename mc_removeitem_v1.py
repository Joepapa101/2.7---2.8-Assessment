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




removeitem = enterbox('Enter the name of the item you would like to remove')

while True:
    if removeitem in monster_cards:
        del monster_cards[removeitem]
        print(monster_cards)
        break
    for key, value in monster_cards.items():
        print(f"{key}: {value}")
    else:
        msgbox('That is not a valid card, please try again')
