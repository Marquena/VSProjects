yks = int(input("anna ensimmäinen kokonaisluku: "))
kaks = int(input("anna toinen kokonaisluku: "))
kol = int(input("anna kolmas kokonaisluku: "))

summa = yks+kaks+kol
tulo = yks*kaks*kol
ka = summa/3

print("Summa on: ", summa)
print("Tulo on: ", tulo)
print(f"{'Keskiarvo on: '}:{ka:10.2f}")