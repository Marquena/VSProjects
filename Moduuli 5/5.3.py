pienin = 0
suurin = 0
x = 0
while x==0:
    num = str(input("Anna joku numero: "))
    if (num == ""):
        print ("pienin luku: ", pienin, "suurin luku: ", suurin)
        x = 1
        break
    num = float(num)
    if num<pienin or pienin <=0:
        pienin = num
    elif num > suurin or suurin >=0:
        suurin = num
