tiedot = {"EFHK":"Helsinki-Vantaa",
          "EFOU":"Oulu",
          "EFRO":"Rovaniemi"}

while True:
    print("Haluatko: \n1. Syöttää uuden lentoaseman.\n2. Hakea jo syötetyn lentoaseman.\n3. Lopettaa")
    q = (input(">>> "))
    if q == 1:
        asema = input("Anna aseman nimi: ")
        koodi = input("Anna ICAO-koodi: ")
        tiedot[koodi] = asema
    elif q==2:
        haku = input("Anna ICAO-koodi: ")
        if haku in tiedot:
            print(f"koodi kuuluu {tiedot[haku]}-lentoasemalle")
        else:
            print("koodia ei löydy")
    else:
        break
