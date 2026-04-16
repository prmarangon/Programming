
import requests

def robar_carta(id_baraja):
    url_robo = f"https://www.deckofcardsapi.com/api/deck/{id_baraja}/draw/?count=1"
    respuesta_robo = requests.get(url_robo)

    datos_cartas = respuesta_robo.json()
    return datos_cartas

valores_cartas = {
    "2": 2, "3": 3, "4": 4, "5": 5,"6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "JACK": 11,
    "QUEEN": 12, "KING": 13, "ACE": 14
}

url = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
respuesta = requests.get(url)

datos_baraja = respuesta.json()
id_baraja = datos_baraja['deck_id']

datos_cartas = robar_carta(id_baraja)

vidas = 3

carta1 = datos_cartas['cards'][0]['value']
palo_carta1 = datos_cartas['cards'][0]['suit']

print(f"\nLa carta que ha salido es el {carta1} de {palo_carta1}.")

print(f"\n¿Cómo crees que será la siguiente carta?")
opcion = int(input("1. Mayor\n2. Menor\n"))

while vidas > 0:

    datos_cartas = robar_carta(id_baraja)

    carta2 = datos_cartas['cards'][0]['value']
    palo_carta2 = datos_cartas['cards'][0]['suit']

    print(f"\nLa siguiente carta es el {carta2} de {palo_carta2}.")

    match opcion:

        case 1:

            if valores_cartas[carta1] < valores_cartas[carta2]:
                print(f"¡Tienes razón, así que puedes continuar!")

            else:
                vidas -= 1 

                if vidas > 0:
                    print(f"¡Te equivocaste! Ahora te quedan {vidas} vidas.")
                
                else:
                    print(f"¡Oh no! Te equivocaste y has perdido todas tus vidas.")

        case 2:

            if valores_cartas[carta1] > valores_cartas[carta2]:
                print(f"¡Tienes razón, así que puedes continuar!")

            else:
                vidas -= 1 

                if vidas > 0:
                    print(f"\n¡Te equivocaste! Ahora te quedan {vidas} vidas.")
                
                else:
                    print(f"¡Oh no! Te equivocaste y has perdido todas tus vidas!")

        case _:
            print("Tienes que elegir una opción.")

    if vidas > 0:
        print(f"\n¿Cómo crees que será la siguiente carta?")
        opcion = int(input("1. Mayor\n2. Menor\n"))
        
    carta1 = carta2