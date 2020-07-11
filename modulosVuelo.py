def mincomb(estadia):
    while estadia < 0:
        estadia = int(input("ingrese un valor valido para su estadia: "))
    if estadia <= 480:
        mincomb = 0
    if estadia > 480:
        for i in range (1,estadia,480):
                mincomb = (5000*i)
        return mincomb

### preograma principal ###
x = int(input("Hola! cuantos minutos se quedará?: "))
print (mincomb(x))



