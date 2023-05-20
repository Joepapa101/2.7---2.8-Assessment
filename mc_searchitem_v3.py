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
    ability = buttonbox('What abilities would you like to change', choices=['Strength', 'Speed', 'Stealth', 'Cunning'])
    print(monster_cards[searchcard])
    abilityamount = enterbox(f'Enter new value for {ability}')
    monster_cards[searchcard][ability.lower()] = [abilityamount]
    print(monster_cards[searchcard])
elif editcard == 'No':
    print('ur mum')

###change log = edited 'editcard' section'