import json
import ini

pel = ini.pelaaja
def tietoja():
    f = open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/welcome.txt")
    print(f.read())
def exitgame():
    save_data = {
        "pelaaja": pel.name,
        "ika":pel.age,
        "phase":pel.phase,
        "lvl": pel.lvl,
        "inv":pel.inv
        }
        
    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","w") as save:
        json.dump(save_data,save)
    exit()
def setting():
    print("ei mitää")
    
def menu():

    pel = ini.pelaaja

    pel.lvl = 0
    pel.phase = 0
    pel.inv = []
    pel.name = input("Mikä on nimesi?\n>>> ")
    pel.age = int(input("Kuina vanha olet?\n>>> "))

    if pel.age <12:
        print("OLet liian nuori pelaamaan.")
        exit()
    print("Tervetuloa peliin!")
    print(f"NIMI: {pel.name}\nIKÄ: {pel.age}")

    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.txt","w")as terve:
        terve.write(pel.name)
        terve.write(f"\n{pel.age}")

    menu_lp = True
    while menu_lp:
        print("\n\nMENU\n-------\n1. Pelaa\n2. Tietoja\n3. fantsuu \n4. Exit")
        menu_input = int(input(">>> "))
        if menu_input == 1:
            print("peli alkaa")
            input(">>> ")
            break
        elif menu_input ==2:
            tietoja()
            input(">>> ")
        elif menu_input ==3:
            setting()
            input(">>> ")
        elif menu_input==4:
            print("heihei")
            exit()
    save_data = {
        "pelaaja": pel.name,
        "ika":pel.age,
        "phase":pel.phase,
        "lvl": pel.lvl,
        "inv":pel.inv
        }
    
    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","w") as save:
        json.dump(save_data,save)
    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","r") as save:
        data=json.load(save)
    print(data['pelaaja'],data['ika'])
def l1(phase):
    tav = ini.huone("taverna","lapio")
    if phase ==0:
        print("Kävelet tavernaan jossa on miehiä, mitä teet?")
        ss=int(input("1. hakkaat ensimmäisen\n2. Tilaat juoman\n3. kävelet ulos\n>>> "))
        if ss == 1:
            print("sinut tyrmättiin ja elämäsi on ohi")
            input(">>> ")
            exitgame()
        elif ss==2:
            print("Baarin vieressä on lapio, otatko sen mukaasi?")
            sa = input("1. Kyllä\n2. Ei\n>>> ")
            if sa ==1:
                print("Olet saanut hienon lapion")
                pel.inv.append("lapio")
        elif ss==3:
            phase=1
    elif phase==1:
        print("Kävelet ulos tavernasta, mitä teet?")
        ss = input("1. Juokset mereen\n2. Jatkat itään\n3. Jatkat länteen")
        if ss ==1:
            print("Hukuit")
            input(">>> ")
            exitgame()
        elif ss==2:
            print("Vastaasi tulee susilauma ja sinut syödään elävältä")
            input(">>> ")
            exitgame()
        elif ss==3:
            print("Kävelet pitkin pimeää metsäpolkua")
            input(">>> ")
        phase+=1
def l2(phase):
    mökki = ini.huone("mökki","tiirikka")
        
def peli(taso, phase):
    if taso ==0:
        l1(phase)
        taso+=1
    elif taso==1:
        l2(phase)