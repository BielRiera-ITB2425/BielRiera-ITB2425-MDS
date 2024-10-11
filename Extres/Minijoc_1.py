import random

def endevina_el_numero():
    # Generar un número aleatori entre 1 i 100
    numero_secret = random.randint(1, 100)
    intents = 0
    max_intents = 10

    print("Benvingut al joc 'Endevina el número'!")
    print(f"Intenta endevinar el número entre 1 i 100. Tens {max_intents} intents.")

    while intents < max_intents:
        try:
            # Demanar al jugador que introdueixi un número
            resposta = int(input("Introdueix el teu número: "))
            intents += 1

            if resposta < 1 or resposta > 100:
                print("El número ha de ser entre 1 i 100. Torna a intentar.")
            elif resposta < numero_secret:
                print("Més alt! Intenta de nou.")
            elif resposta > numero_secret:
                print("Més baix! Intenta de nou.")
            else:
                print(f"Felicidades! Has endevinat el número {numero_secret} en {intents} intents.")
                break
        except ValueError:
            print("Si us plau, introdueix un número vàlid.")

    if intents == max_intents:
        print(f"Ho sento! No has pogut endevinar el número. Era {numero_secret}.")

if __name__ == "__main__":
    endevina_el_numero()
