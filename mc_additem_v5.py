from easygui import *
from mc_dictionary_v1 import monster_cards

while True:
    fields = ['Cardname', 'Strength', 'Speed', 'Stealth', 'Cunning']
    card_details = multenterbox('Enter the card details here (do not exceed 25 characters):', fields=fields)

    cardname = card_details[0]
    strength = card_details[1]
    speed = card_details[2]
    stealth = card_details[3]
    cunning = card_details[4]
    
    print(strength, speed, stealth, cunning)
    
    
    if not strength.isdigit() or not speed.isdigit() or not stealth.isdigit() or not cunning.isdigit():
        msgbox('Please enter an integer in abilities.')
    

    if strength or speed or stealth or cunning >= 25:
        msgbox('Please enter a number below 25')
    else:
        break

    cardname, strength, speed, stealth, cunning = card_details

    
monster_cards[cardname] = {
    'strength': int(strength),
    'speed': int(speed),
    'stealth': int(stealth),
    'cunning': int(cunning)
}


        

print(monster_cards)
