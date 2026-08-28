lp=0
while lp==0:
    tmi = float(input("Anna tuumamäärä: "))
    if tmi >0:
        print(tmi, "tuumaa on",f"{tmi*2.54:10.2f}", "senttimetriä")
    else:
        lp=1
        break