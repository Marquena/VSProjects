hytti = int(input("mikä on hyttiluokkasi?\n1.LUX\2.A\n3.B\n4.C"))
if hytti == 1:
    print("LUX on parvekkeellinen hytti yläkannella")
elif hytti ==2:
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif hytti ==3:
    print("B on ikkunaton hytti autokannen yläpuolella")
elif hytti ==4:
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("virheellinen hyttiluokka")