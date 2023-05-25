from easygui import *
from mc_dictionary_v1 import monster_cards


choices = []
cardnames = list(monster_cards.keys())

for cardnames in monster_cards:
    choices.append(cardnames)
    print(choices)
    
    
    
searchcard = choicebox('Which card would you like to choose?', choices=choices)
abilities = monster_cards[searchcard]


        
while True:  
    editcard = buttonbox(f'{searchcard} has {monster_cards[searchcard]["strength"]} strength,\
 {monster_cards[searchcard]["speed"]} speed, {monster_cards[searchcard]["stealth"]} stealth,\
 {monster_cards[searchcard]["cunning"]} cunning. ', choices=['Edit', 'Delete', 'Exit'])
    if editcard == 'Edit':
        ability = buttonbox('What abilities would you like to change', choices=[f'Strength ({monster_cards[searchcard]["strength"]})\
', f'Speed ({monster_cards[searchcard]["speed"]})', f'Stealth ({monster_cards[searchcard]["stealth"]})', f'Cunning ({monster_cards[searchcard]["cunning"]})',])
        print(monster_cards[searchcard])
            #above 25 limit loop
        while True:
            abilityamount = enterbox(f'Enter new value for {ability}')
            if not abilityamount.isdigit():
                msgbox('Enter an integer')
            elif int(abilityamount) >= 25:
                msgbox("You can't enter a number above 25")
            else:
                break
        realability = ability.split(' ')[0]
        monster_cards[searchcard][realability.lower()] = int(abilityamount)
        print(monster_cards[searchcard])

    elif editcard == 'Delete':
        del monster_cards[searchcard]
        break
    
    elif editcard == 'Exit':
        break








