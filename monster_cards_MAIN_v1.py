from easygui import *
from mc_dictionary_v1 import monster_cards





def welcome_options():
    useroptions = buttonbox('What would you like to do?', choices= ['Add Card', 'Remove Card', 'Search Cards', 'Print Card List',])
    if useroptions == 'Add Card':
        add_card(monster_cards)
    elif useroptions == 'Remove Card':
        remove_card(monster_cards)
    elif useroptions == 'Search Cards':
        search_card(monster_cards)
    #elif useroptions == 'Print Card List':
        #print_card_list()







def add_card(monster_cards):
    while True:
        cardname = enterbox('Enter the name of the card you would like to add')
        
        while True:
            strength = int(enterbox('Enter the strength of the character'))
            if strength >= 25:
                msgbox("You can't enter a number greater than 25 strength")
            else:
                break
        
        while True:
            speed = int(enterbox('Enter the speed of the character'))
            if speed >= 25:
                msgbox("You can't enter a number greater than 25 speed")
            else:
                break

        while True:
            stealth = int(enterbox('Enter the stealth of the character'))
            if stealth >= 25:
                msgbox("You can't enter a number greater than 25 stealth")
            else:
                break

        while True:
            cunning = int(enterbox('Enter the cunning of the character'))
            if cunning >= 25:
                msgbox("You can't enter a number greater than 25 cunning6")
            else:
                break


        monster_cards[cardname] = {
            'strength': [strength],
            'speed': [speed],
            'stealth': [stealth],
            'cunning': [cunning]
        }


def remove_card(monster_cards):
    removeitem = enterbox('Enter the name of the item you would like to remove')

    while True:
        if removeitem in monster_cards:
            del monster_cards[removeitem]
            print(monster_cards)
            break
        for key, value in monster_cards.items():
            print(f"{key}: {value}")
        else:
            msgbox('That is not a valid card, please try again')

def search_card(monster_cards):
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
        abilityamount = enterbox(f'Enter new value for {ability}')
        realability = ability.split(' ')[0]
        monster_cards[searchcard][realability.lower()] = [abilityamount]
        print(monster_cards[searchcard])
    elif editcard == 'Exit':
        welcome_options()





welcome_options()