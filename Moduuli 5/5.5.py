käyt = str(input("Syötä käyttäjänimi: "))
sal = str(input("Syötä salasana: "))
oik=0
count=0
while oik==0:
    käyt = str(input("Syötä käyttäjänimi: "))
    sal = str(input("Syötä salasana: "))
    if käyt =="python" and sal=="rules":
        print("Tervetuloa")
        break
    else:
        print("pääsy evätty")
    if count <5:
        count+=1
    else:
        print("liian monta väärää yritystä")
        break



