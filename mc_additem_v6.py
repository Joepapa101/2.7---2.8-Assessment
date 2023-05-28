from easygui import *
from mc_dictionary_v1 import monster_cards

cardname = enterbox('Enter the name of the card')

while True:
    fields = ['Strength', 'Speed', 'Stealth', 'Cunning']
    card_details = multenterbox('Enter the card details here (do not exceed 25 characters):', fields=fields)

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


        

print(monster_cards)
