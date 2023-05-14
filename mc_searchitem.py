from easygui import *
from mc_dictionary_v1 import monster_cards


while True:
    searchcard = enterbox('Search any card from the library')
    if searchcard in monster_cards:
        #this got a bit funky to program
        msgbox(f"The {searchcard}combo exists")
    else:
        msgbox(f'The combo {searchcard} does not exist.')
        break

editcard = buttonbox('Would you like to edit this card')



