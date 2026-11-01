def pariton(jono):
    i = 0
    for i in range(len(jono)):
        if len(jono)<i:
            break
        elif jono[i]%2==0:
            jono.remove(jono[i])
    return jono

num = [1,2,3,4,5,6,7,8,9,10]

ab = pariton(num)
print(ab)