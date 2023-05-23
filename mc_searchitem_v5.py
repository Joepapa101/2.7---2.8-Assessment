from easygui import *
from mc_dictionary_v1 import monster_cards

while True:
    searchcard = enterbox('Search any card from the library')
    if searchcard in monster_cards:
        editcard = buttonbox(f'{searchcard} has {monster_cards[searchcard]["strength"]} strength,\
 {monster_cards[searchcard]["speed"]} speed, {monster_cards[searchcard]["stealth"]} stealth,\
 {monster_cards[searchcard]["cunning"]} cunning. ', choices=['Edit', 'Exit'])
        break
    else:
        msgbox(f'{searchcard} does not exist.')


if editcard == 'Edit':
    print(monster_cards[searchcard])
    ability = buttonbox('What abilities would you like to change', choices=[f'Strength ({monster_cards[searchcard]["strength"]})\
', f'Speed ({monster_cards[searchcard]["speed"]})', f'Stealth ({monster_cards[searchcard]["stealth"]})', f'Cunning ({monster_cards[searchcard]["cunning"]})'])
    print(monster_cards[searchcard])
    #above 25 limit loop
    while True:
        abilityamount = enterbox(f'Enter new value for {ability}')
        if abilityamount >= 25:
            msgbox("You can't enter a number above 25")
        elif not abilityamount.isdigit():
            print('Enter an integer')
        else:
            break
            
    realability = ability.split(' ')[0]
    monster_cards[searchcard][realability.lower()] = [abilityamount]
    print(monster_cards[searchcard])
elif editcard == 'Exit':
    print('ur mum')

#firstcombo.split(':')[1]
#Change-log - improved searchcard function
