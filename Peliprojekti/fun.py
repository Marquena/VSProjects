import json
import ini

pel = ini.pelaaja
def tietoja():
    f = open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/welcome.txt")
    print(f.read())
def exitgame():
    #poistuu pelistä
    open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","w").close()
    save_data = {
            "pelaaja": "",
            "ika":0,
            "phase":0,
            "lvl": 0,
            "inv":{}  
            }
    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","w") as save:
        json.dump(save_data,save)
    exit()
def updatedata():
    #Päivittää obj pelaajan tiedot
    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","r")as save:
        ac = json.load(save)
    pel.name = ac["pelaaja"]
    pel.age = ac["ika"]
    pel.phase = ac["phase"]
    pel.lvl = ac["lvl"]
    pel.inv = ac["inv"]
def savegame():
    save_data = {
        "pelaaja": pel.name,
        "ika":pel.age,
        "phase":pel.phase,
        "lvl": pel.lvl,
        "inv":pel.inv
        }
    
    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","w") as save:
        json.dump(save_data,save)
def removefrominv(item):
    #poistaa asian hahmon inventorysta
    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","r")as save:
        ac = json.load(save)
    a=0
    for i in ac["inv"]:
        if i["nimi"] == item:
            ac["inv"].remove(ac["inv"][a])
            with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","w") as save:
                json.dump(ac,save)
            break

        a+=1
def search(item):
    #etsii itemin inventorysta True/False
    x = 0
    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","r")as save:
        ac = json.load(save)
    for i in ac["inv"]:
        if i["nimi"] != item:
            x=False
        else:
            x=True
            break
    return x

def menu():

    pel = ini.pelaaja

    pel.lvl = 0
    pel.phase = 0
    pel.inv = []
    pel.name = input("Mikä on nimesi?\n>>> ")
    pel.age = int(input("Kuinka vanha olet?\n>>> "))

    if pel.age <12:
        print("OLet liian nuori pelaamaan.")
        exit()
    print("Tervetuloa peliin!")

    print(f"NIMI: {pel.name}\nIKÄ: {pel.age}")

    menu_lp = True
    while menu_lp:
        print("\n\nMENU\n-------\n1. Pelaa\n2. Tietoja\n3. Exit")
        menu_input = int(input(">>> "))
        if menu_input == 1:
            print("peli alkaa")
            savegame()
            input(">>> ")
            break
        elif menu_input ==2:
            tietoja()
            input(">>> ")
        elif menu_input==3:
            print("heihei")
            exit()
    savegame()
    with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","r") as save:
        data=json.load(save)
    print(data['pelaaja'],data['ika'])
def l1(phase):
    ph = phase
    while True:
        if ph ==0:
            print("Kävelet tavernaan jossa on miehiä, mitä teet?")
            ss=int(input("1. hakkaat ensimmäisen\n2. Tilaat juoman\n3. kävelet ulos\n>>> "))
            if ss == 1:
                print("sinut tyrmättiin ja elämäsi on ohi")
                input(">>> ")
                exitgame()
            elif ss==2:
                print("Baarin vieressä on lapio, otatko sen mukaasi?")
                sa = int(input("1. Kyllä\n2. Ei\n>>> "))
                if sa == 1:
                    print("Olet saanut hienon lapion")
                    pel.inv.append(ini.lapio)
            else:
                print(" ")
            ph+=1
            pel.phase = ph
            savegame()
        elif ph==1:
            print("Kävelet ulos tavernasta, mitä teet?")
            ss = int(input("1. Juokset mereen\n2. Jatkat itään\n3. Jatkat länteen\n>>> "))
            if ss ==1:
                print("Hukuit")
                input(">>> ")
                exitgame()
            elif ss==2:
                savegame()
                print("Vastaasi tulee kauppias joka yrittää myydä sinulle lapiotaan. Ostatko lapion?")
                ac = int(input("1. Kyllä\n2. Ei\n>>> "))
                if ac == 1:
                    if search("lapio"):
                        print("sinulla on nyt kaksi lapiota")
                        input(">>> ")
                        print("lähtiessäsi pois kauppiaan luota, kaadut kahden lapion painosta, ja lyöt pääsi kiveen\n Menehdyit")
                        input(">>> ")
                        exitgame()
                    else:
                        pel.inv.append(ini.lapio)
                        print("sait hienon lapion")
                        input(">>> ")
                else:
                    savegame()
                    print("Kieltäydyt, ja lähdet takaisin, ja kohti länttä.")
                    input(">>> ")
                    print("Kävelet pitkin pimeää metsäpolkua")
                    input(">>> ")
            elif ss==3:
                print("Kävelet pitkin pimeää metsäpolkua")
                input(">>> ")
            ph=0
            pel.phase = ph
            pel.lvl = 1
            savegame()
            break
            
def l2(phase):
    ph = phase
    while True:
        if ph==0:
            print("Näet edessäsi mökin")
            ss = int(input("1. Kävelet ovesta sisään\n2. Kurkkaat talon ikkunasta\n3. Alat kaivamaan kuoppaa(?????)\n>>> "))
            if ss==1:
                print("Kävellessäsi ovesta sisään, päällesi hyökkää viisi aseistautunutta kissaa\nJa menehdyt")
                input(">>> ")
                exitgame()
            elif ss==2:
                print("juuri kun nostat päätäsi, ikkunasta lentää kukkaruukku suoraan päin naamaasi\nJa menehdyt")
                input(">>> ")
                exitgame()
            elif ss==3:
                if search("lapio"):
                    print("Alat jostain syystä kaivamaan lapiollasi maata, ja löydät haudatun säkin")
                    print("Olet saanut pussillisen kuivattua kalaa")
                    pel.inv.append(ini.kalapussi)
                    removefrominv("lapio")
                    savegame()
                else:
                    print("Alat kaivamaan kuoppaa käsilläsi tuloksetta")
                ph+=1
            savegame()
        elif ph==1:
            print("Talosta tulee kolme kissaa ulos tutkimaan hiipparia (sinua)")
            input(">>> ")
            if search("kalapussi"):
                print("Kissat tuijottavat löytämääsi kalapussia nälkäisenä")
                ss=int(input("1. Heitä kissoille pussi\n2. Syö kalat itse\n>>> "))
                if ss==1:
                    print("kissat saivat syödäkseen\nVoitit pelin!!")
                    input(">>> ")
                    exitgame()
                else:
                    print("Kissat hyppäävät päällesi nälkäisen vihan valloittamana, ja syövät sinut kalapussin sijaan.")
                    input(">>> ")
                    exitgame()
            else:
                print("Kissat hyppäävät päällesi nälkäisen vihan valloittamana, ja syövät sinut kalapussin sijaan.")
                input(">>> ")
                exitgame()        
def peli(taso, phase):
    if taso ==0:
        l1(phase)
        pel.lvl = taso+1
    elif taso==1:
        l2(phase)
        pel.lvl = taso+1