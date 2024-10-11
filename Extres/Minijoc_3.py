def tria_la_teva_aventura():
    print("Benvingut a 'Tria la teva aventura'!")
    print("Estàs en un bosc misteriós. Tens dues rutes davant teu.")
    print("1. Caminar pel camí de l'esquerra.")
    print("2. Caminar pel camí de la dreta.")

    eleccio1 = int(input("Tria 1 o 2: "))

    if eleccio1 == 1:
        print("Has triat el camí de l'esquerra.")
        print("De sobte, et trobes amb un ogre!")
        print("1. Combatre l'ogre.")
        print("2. Fugir cap a casa.")


        eleccio2 = input("Tria 1 o 2: ")

        if eleccio2 == '1':
            print("Has guanyat la batalla! L'ogre s'ha rendit.")
            print("Has trobat un tresor i ets ric!")
        elif eleccio2 == '2':
            print("Fugixes ràpidament! Arribes a casa, però et sents un poc covard.")
        else:
            print("Elecció no vàlida. El teu destí és incert.")

    elif eleccio1 == '2':
        print("Has triat el camí de la dreta.")
        print("T'has trobat amb una bella princesa.")
        print("1. Parlar amb ella.")
        print("2. Ignorar-la i seguir caminant.")

        eleccio2 = input("Tria 1 o 2: ")

        if eleccio2 == '1':
            print("La princesa et diu que necessita ajuda. Ets un heroi!")
            print("Has començat una gran aventura junts.")
        elif eleccio2 == '2':
            print("Decideixes ignorar la princesa i continuar. Et perds en el bosc.")
        else:
            print("Elecció no vàlida. Et quedes sol al bosc.")

    else:
        print("Elecció no vàlida. Et quedes immobilitzat en el bosc.")

if __name__ == "__main__":
    tria_la_teva_aventura()
