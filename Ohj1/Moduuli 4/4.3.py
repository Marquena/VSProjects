suk = int(input("mikä on biologinen sukupuolesi?\n1. Mies\n2. Nainen\n>>> "))
hem = int(input("Mikä on hemoglobiiniarvosi?(g/l): "))

if suk==1:
    if hem<134:
        print("Hemoglobiiniarvosi ovat normaalia alhaisemmat")
    elif hem>195:
        print("Hemoglobiiniarvosi ovat normaalia korkeammat")
    else:
        print("Hemoglobiiniarvosi ovat normaalit")
elif suk==2:
    if 117<=hem<=175:
        print("Hemoglobiiniarvosi ovat normaalit")
    elif hem<117:
        print("Hemoglobiiniarvosi ovat normaalia alhaisemmat")
    elif hem>175:
        print("Hemoglobiiniarvosi ovat normaalia korkeammat")
    else:
        print("miten")
else:
    print("yritäs uusiks")
