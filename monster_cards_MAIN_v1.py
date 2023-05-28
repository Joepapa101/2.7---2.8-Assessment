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
    elif useroptions == 'Print Card List':
        card_list(monster_cards)




def add_card(monster_cards):
   

def remove_card(monster_cards):
    choices = []
    for cardnames in monster_cards:
        choices.append(cardnames)
            
            
    removeitem = choicebox('Which card would you like to delete?', choices=choices)

    while True:
        if removeitem in monster_cards:
            del monster_cards[removeitem]
            break
        for key, value in monster_cards.items():
            print(f"{key}: {value}")
        else:
            msgbox('That is not a valid card, please try again')
    
    welcome_options()

def search_card(monster_cards):
    choices = []
    cardnames = list(monster_cards.keys())

    for cardnames in monster_cards:
        choices.append(cardnames)
           
    searchcard = choicebox('Which card would you like to choose?', choices=choices)
    abilities = monster_cards[searchcard]

       
    while True:  
        editcard = buttonbox(f'{searchcard} has {monster_cards[searchcard]["strength"]} strength,\
    {monster_cards[searchcard]["speed"]} speed, {monster_cards[searchcard]["stealth"]} stealth,\
    {monster_cards[searchcard]["cunning"]} cunning. ', choices=['Edit', 'Delete', 'Exit'])
        if editcard == 'Edit':
            ability = buttonbox('What abilities would you like to change', choices=[f'Strength ({monster_cards[searchcard]["strength"]})\
    ', f'Speed ({monster_cards[searchcard]["speed"]})', f'Stealth ({monster_cards[searchcard]["stealth"]})', f'Cunning ({monster_cards[searchcard]["cunning"]})',])
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

        elif editcard == 'Delete':
            del monster_cards[searchcard]
            break
        
        elif editcard == 'Exit':
            break
    
    welcome_options()




def card_list(monster_cards):
    for monster, i in monster_cards.items():
        print(f"Monster: {monster}")
        print(f"Strength: {i['strength']}")
        print(f"Speed: {i['speed']}")
        print(f"Stealth: {i['stealth']}")
        print(f"Cunning: {i['cunning']}")
        print()
    
    welcome_options()


welcome_options()