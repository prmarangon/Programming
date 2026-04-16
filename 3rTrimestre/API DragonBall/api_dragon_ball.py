import requests
import random

def get_random_character():
    id = random.randint(1,44)
    url = f"https://dragonball-api.com/api/characters/{id}"

    request = requests.get(url)
    character = request.json()
    return character

def fight(character1, character2):
    while character1 == character2:
        character2 = get_random_character()

    print(f"\n{character1['name']} vs {character2['name']}")

    tie = True
    while tie:

        if int(character1['ki'].replace('.', '')) > int(character2['ki'].replace('.', '')):
            print(f"{character1['name']} wins!")
            tie = False
            return character1
        
        elif int(character1['ki'].replace('.', '')) == int(character2['ki'].replace('.', '')):
            print("It's a tie!")
            tie = True
        else:
            print(f"{character2['name']} wins!")
            tie = False
            return character2


#-----------------------------
#-------  TOURNAMENT   -------
#-----------------------------

def tournament():
    characters = []
    for i in range(8):
        character = get_random_character()
        while character in characters:
            character = get_random_character()
        characters.append(character)

    print("Welcome to the Dragon Ball Tournament!")
    print("The fighters are:")
    for character in characters:
        print(character['name'])

    while len(characters) > 1:
        next_round = []
        for i in range(0, len(characters), 2):
            winner = fight(characters[i], characters[i+1])
            next_round.append(winner)
        characters = next_round

    print(f"The champion is {characters[0]['name']}!")

tournament()


            