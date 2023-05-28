from easygui import *
from mc_dictionary_v1 import monster_cards

cardname = enterbox('Enter the name of the card')

while True:
    fields = ['Strength', 'Speed', 'Stealth', 'Cunning']
    card_details = multenterbox(f'Enter the card details for {cardname}:', fields=fields)

    strength = card_details[0]
    speed = card_details[1]
    stealth = card_details[2]
    cunning = card_details[3]
    
    print(strength, speed, stealth, cunning)

    if strength == '' or speed == '' or stealth == '' or cunning == '':
        msgbox('Plese enter something')
    
    elif not (strength.isdigit() or not speed.isdigit() or not stealth.isdigit() or not cunning.isdigit()):
        msgbox('Please enter an integer in abilities.')
    

    elif int(strength) >= 25 or int(speed) >= 25 or int(stealth) >= 25 or int(cunning) >= 25:
        msgbox('Please enter a number below 25')
    else:
        break


    
monster_cards[cardname] = {
    'strength': int(strength),
    'speed': int(speed),
    'stealth': int(stealth),
    'cunning': int(cunning)
}

while True:
    editcard = buttonbox(f'{cardname} has {monster_cards[cardname]["strength"]} strength,\
 {monster_cards[cardname]["speed"]} speed, {monster_cards[cardname]["stealth"]} stealth,\
 {monster_cards[cardname]["cunning"]} cunning. ', choices=['Edit', 'Exit'])
    if editcard == 'Edit':
        ability = buttonbox('What abilities would you like to change', choices=[f'Strength ({monster_cards[cardname]["strength"]})\
', f'Speed ({monster_cards[cardname]["speed"]})', f'Stealth ({monster_cards[cardname]["stealth"]})', f'Cunning ({monster_cards[cardname]["cunning"]})',])
        
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
        monster_cards[cardname][realability.lower()] = int(abilityamount) 
    elif editcard == 'Exit':
        break
