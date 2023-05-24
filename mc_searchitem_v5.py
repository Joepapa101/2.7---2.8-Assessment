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


while True:
    editcard = buttonbox(monster_cards[editcard], choices=['Ok', 'Edit'])


    if editcard == 'Edit':
        ability = buttonbox('What abilities would you like to change', choices=[f'Strength ({monster_cards[editcard]["strength"]})\
    ', f'Speed ({monster_cards[editcard]["speed"]})', f'Stealth ({monster_cards[editcard]["stealth"]})', f'Cunning ({monster_cards[editcard]["cunning"]})',])
        print(monster_cards[editcard])
        #above 25 limit loop
        abilityamount = enterbox(f'Enter new value for {ability}')
        if int(abilityamount) >= 25:
            msgbox("You can't enter a number above 25")
        elif not abilityamount.isdigit():
            print('Enter an integer')
        realability = ability.split(' ')[0]
        monster_cards[editcard][realability.lower()] = [abilityamount]
        print(monster_cards[editcard])
    elif editcard == 'Ok':
        break

#firstcombo.split(':')[1]
#Change-log - improved searchcard function
