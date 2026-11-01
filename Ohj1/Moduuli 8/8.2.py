nimet=set()
while True:
    nimi = (input("Anna nimi: "))
    if nimi=="":
        break
    else:
        if nimi in nimet:
            print("Aiemmin syötetty nimi")
            nimet.add(nimi)
        else:
            print("Uusi nimi")
            nimet.add(nimi)

print(nimet)
