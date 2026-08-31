import fun

p_name = input("Mikä on nimesi?\n>>> ")
p_age = int(input("Kuina vanha olet?\n>>> "))

if p_age <12:
    print("OLet liian nuori pelaamaan.")
    exit()
print("Tervetuloa peliin!")
print(f"NIMI: {p_name}\nIKÄ: {p_age}")

menu_lp = True
while menu_lp:
    print("\n\nMENU\n-------\n1. Pelaa\n2. Tietoja\n3. fantsuu \n4. Exit")
    menu_input = int(input(">>> "))
    if menu_input == 1:
        #eioo viel mitää tääl
        print("ei viel mitää")
        input(">>> ")
    elif menu_input ==2:
        fun.tietoja()
        input(">>> ")
    elif menu_input ==3:
        print("huuhaa")
        input(">>> ")
    elif menu_input==4:
        print("heihei")
        menu_lp=False