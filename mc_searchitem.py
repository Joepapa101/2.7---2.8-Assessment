from easygui import *
from mc_dictionary_v1 import monster_cards


while True:
    searchcard = enterbox('Search any card from the library')
    if searchcard in monster_cards:
        msgbox(f"{searchcard} exists")
        break
    else:
        msgbox(f'The  {searchcard} does not exist.')

editcard = buttonbox('Would you like to edit this card', choices=['Yes', 'No'])
if editcard == 'Yes':
    print(monster_cards[searchcard])
    strengthinput = enterbox('Enter strength')
    speedinput = enterbox('Enter speed')
    stealthinput = enterbox('Enter stealth')
    cunninginput = enterbox('Enter cunning')
    del monster_cards[searchcard]
    monster_cards[searchcard] = {
        'strength': [strengthinput],
        'speed': [speedinput],
        'stealth': [stealthinput],
        'cunning': [cunninginput]
    }
    print(monster_cards[searchcard])
elif editcard == 'No':
    print('ur mum')


