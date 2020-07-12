def mincomb(estadia):
    tiempo = 0
    while estadia < 0:
        estadia = int(input("ingrese un valor valido para su estadia: "))
    while estadia <= 480:
        mincomb = 0
    while estadia > 480:
        for i in range (1,estadia):
            tiempo = tiempo + 480
            while estadia < tiempo:
                mincomb = (5000*i)
    return resultado

### preograma principal ###
x = int(input("Hola! cuantos minutos se quedará?: "))
resultado = (mincomb(x))
print(resultado)




