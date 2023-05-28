from easygui import *
from mc_dictionary_v1 import monster_cards


for monster, i in monster_cards.items():
    print(f"Monster: {monster}")
    print(f"Strength: {i['strength']}")
    print(f"Speed: {i['speed']}")
    print(f"Stealth: {i['stealth']}")
    print(f"Cunning: {i['cunning']}")
    print()