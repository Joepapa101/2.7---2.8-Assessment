"""
MONSTER CARDS VERSION 4
change-log: complies with pep8
By Josh Currie-Cook for NCEA
"""

from easygui import *
from mc_dictionary_v1 import monster_cards


def welcome_options():
    # Asks the user where to navigate in the program
    user_options = buttonbox(
        'What would you like to do?',
        choices=['Add Card', 'Remove Card', 'Search Cards',
                 'Print Card List', 'Exit'],
        title='Main Menu'
    )
    if user_options == 'Add Card':
        add_card(monster_cards)
    elif user_options == 'Remove Card':
        remove_card(monster_cards)
    elif user_options == 'Search Cards':
        search_card(monster_cards)
    elif user_options == 'Print Card List':
        card_list()
    elif user_options == 'Exit':
        exit(code=34)


def add_card(monster_cards):
    while True:
        # User input to obtain their desired name for their card
        card_name = enterbox('Enter the name of the card', title="Add Card")
        # Checks to see whether user has pressed cancel
        if card_name is None:
            welcome_options()
        # Card name checker, to check whether the user has entered a card name
        if card_name == '':
            msgbox('Please enter a name')
        else:
            break

    while True:
        # User enters the details of their monster card in the multienterbox
        fields = ['Strength', 'Speed', 'Stealth', 'Cunning']
        card_details = multenterbox(
            f'Enter the card details for {card_name}:',
            fields=fields, title='Add Card'
        )
        # Checks to see whether user has pressed cancel
        if card_details is None:
            welcome_options()

        strength, speed, stealth, cunning = card_details

        # User error checker, to check the user hasn't entered a string or digit above 25
        if strength == '' or speed == '' or stealth == '' or cunning == '':
            msgbox('Please enter something')
        elif not (strength.isdigit() and speed.isdigit() and stealth.isdigit() and cunning.isdigit()):
            msgbox('Please enter an integer in abilities.')
        elif int(strength) >= 25 or int(speed) >= 25 or int(stealth) >= 25 or int(cunning) >= 25:
            msgbox('Please enter a number below 25')
        else:
            break

    # Dictionary entry, adding the user inputs to a new entry in the dictionary
    monster_cards[card_name] = {
        'strength': int(strength),
        'speed': int(speed),
        'stealth': int(stealth),
        'cunning': int(cunning)
    }
    # Edit card buttonbox, allowing the user to edit what they have just entered
    # for a more accurate entry
    while True:
        edit_card = buttonbox(
            f'{card_name} has {monster_cards[card_name]["strength"]} strength, '
            f'{monster_cards[card_name]["speed"]} speed, '
            f'{monster_cards[card_name]["stealth"]} stealth, '
            f'{monster_cards[card_name]["cunning"]} cunning.',
            choices=['Edit', 'Exit'], title='Add Card'
        )

        # Checks to see whether user has pressed cancel
        if edit_card is None:
            welcome_options()
        # A buttonbox containing the abilities displaying the amount of abilities
        # for the user to select which one to edit
        if edit_card == 'Edit':
            ability = buttonbox(
                'What abilities would you like to change',
                choices=[
                    f'Strength ({monster_cards[card_name]["strength"]})',
                    f'Speed ({monster_cards[card_name]["speed"]})',
                    f'Stealth ({monster_cards[card_name]["stealth"]})',
                    f'Cunning ({monster_cards[card_name]["cunning"]})'
                ], title='Edit Card'
            )
            # Error checker for the user's input, checking the number isn't above 25
            while True:
                ability_amount = enterbox(f'Enter new value for {ability}', title='Edit Card')
                if not ability_amount.isdigit():
                    msgbox('Enter an integer', title='Edit Card')
                elif int(ability_amount) >= 25:
                    msgbox("You can't enter a number above 25", title='Edit Card')
                else:
                    break
            # Splitting the ability choice's title to figure out what input the user
            # pressed and making it into the 'real-ability' variable
            real_ability = ability.split(' ')[0]
            monster_cards[card_name][real_ability.lower()] = int(ability_amount)
        elif edit_card == 'Exit':
            break

    welcome_options()


def remove_card(monster_cards):
    # Compiling list for monster_cards dictionary
    choices = list(monster_cards.keys())
    # Displaying monster cards entries
    remove_item = choicebox('Which card would you like to delete?', choices=choices,
                            title='Remove Card')

    # If cancel is pressed
    if remove_item is None:
        welcome_options()

    # Checks if there is an item in monster_cards, if nothing is there,
    # the remove_card function returns to home screen
    while True:
        if remove_item in monster_cards:
            del monster_cards[remove_item]
            break
        else:
            msgbox('That is not a valid card, please try again', title='Remove Card')
            msgbox('Going back to home screen...')
            welcome_options()

    welcome_options()


def search_card(monster_cards):
    # Displays monster_card dictionary entry keys
    choices = list(monster_cards.keys())
    # User selects a dictionary entry to edit
    search_card = choicebox('Which card would you like to choose?', choices=choices,
                            title='Search Card')
    # Checks to see whether user has pressed cancel
    if search_card is None:
        welcome_options()
    abilities = monster_cards[search_card]

    # Displays monster stats
    while True:
        edit_card = buttonbox(
            f'{search_card} has {monster_cards[search_card]["strength"]} strength, '
            f'{monster_cards[search_card]["speed"]} speed, '
            f'{monster_cards[search_card]["stealth"]} stealth, '
            f'{monster_cards[search_card]["cunning"]} cunning.',
            choices=['Edit', 'Delete', 'Exit'], title='Edit Card'
        )
        # Allows the user to edit specific abilities of the selected monster
        if edit_card == 'Edit':
            ability = buttonbox(
                'What abilities would you like to change',
                choices=[
                    f'Strength ({monster_cards[search_card]["strength"]})',
                    f'Speed ({monster_cards[search_card]["speed"]})',
                    f'Stealth ({monster_cards[search_card]["stealth"]})',
                    f'Cunning ({monster_cards[search_card]["cunning"]})'
                ], title='Edit Card'
            )
            # Error checker for ability to check the user has not entered a number above 
            # 25 or a string
            while True:
                ability_amount = enterbox(f'Enter new value for {ability}',
                                          title='Edit Card')
                #checks to see if cancel is pressed, the program retuns to menu
                if ability_amount is None:
                    welcome_options()

                if not ability_amount.isdigit():
                    msgbox('Enter an integer', title='Edit Card')
                elif int(ability_amount) >= 25:
                    msgbox("You can't enter a number above 25", title='Edit Card')
                else:
                    break
            # Splitting the ability choice's title to figure out what input the user
            # pressed and making it into the 'real-ability' variable
            real_ability = ability.split(' ')[0]
            monster_cards[search_card][real_ability.lower()] = int(ability_amount)

        # Allows the user to delete a searched card
        elif edit_card == 'Delete':
            del monster_cards[search_card]
            break

        # Returns to the menu
        elif edit_card == 'Exit':
            break

    welcome_options()


def card_list():
    # Prints card list to console
    for monster, data in monster_cards.items():
        print(f"Monster: {monster}")
        print(f"Strength: {data['strength']}")
        print(f"Speed: {data['speed']}")
        print(f"Stealth: {data['stealth']}")
        print(f"Cunning: {data['cunning']}")
        print()

    welcome_options()


welcome_options()
