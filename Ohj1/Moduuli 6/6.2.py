list = []

lp = True
while lp:
    luku = (input("Anna luku: "))
    if luku=="":
        break
    else:
        list.append(int(luku))
        list.sort()
list.sort(reverse=True)
i = 0
for i in range(5):
    print(list[i])
    i+=1

