from easygui import *
from mc_dictionary_v1 import monster_cards


choices = []

for cardnames in monster_cards:
    choices.append(cardnames)
        
        
        
removeitem = choicebox('Which card would you like to delete?', choices=choices)

while True:
    if removeitem in monster_cards:
        del monster_cards[removeitem]
        print(monster_cards)
        break
    for key, value in monster_cards.items():
        print(f"{key}: {value}")
    else:
        msgbox('That is not a valid card, please try again')
