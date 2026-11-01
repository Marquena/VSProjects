def listadd(jono):
    määrä = 0
    for i in range(len(jono)):
        määrä +=jono[i]
        i+=1
    return määrä

num =[1,2,3,4,5]
print(listadd(num))