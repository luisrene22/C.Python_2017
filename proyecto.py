# -*- coding: utf-8 -*-
#PROGRAMA 1: Utilizando mis modulos
import numpy as np #Modulo para manejo de matrices y vectores, #siendo np un seudonimo para más abajo utilizarlo.
import matplotlib.pyplot as plt #Modulo para graficar funciones #Siendo plt un seudonimo para más abajo utilizarlo.
import math #Libreria para funciones y constantes usualmente #usadas en matematica

print("******************************************\nGRAFICADORA DE ECUACIONES DE SEGUNDO ORDEN\n******************************************")
print("recuede que son de la forma::AX^2 +BX + C")
i = int(input("Ingresa el rango del eje X::"))
j = int(input("Ingresa el rango del eje Y::"))
a = float(input("Ingresa la constante A::"))
b = float(input("Ingresa la constante B::"))
c = float(input("Ingresa la constante C::"))

datos = np.arange(i,j)#arange genera un vector que va desde el #numero i = "X"=eje horizontal que ingrese el usuario, hasta el #numero j = "Y"=eje vertical que ingrese el usuario.
x=datos

f = a*x**2 +b*x + c

type(f)

plt.plot(x ,f,"b--") #plt.plot(x,f,"b--") es para mandar graficar.
plt.show()#Es para que me muestre la grafica


#PROGRAMA 2: Juego del Ahorcado.

palabraAdivinar = ''
listaPalabraAdiv = []
listaPalabraMost = []
intentos = 3 
letra = ''
run = True

print("******************************************\nJUEGO DEL AHORCADO\n******************************************")
palabraAdivinar = input("Ingresa una palabra:: ")


listaPalabraAdiv = list(palabraAdivinar)

for item in listaPalabraAdiv:
    listaPalabraMost.append('_')

while run:

    print(' '.join(listaPalabraMost))


    letra = input("Da una letra: ")


    for num in range(100):
        print()


    fallo = False

    if letra not in listaPalabraAdiv:

        fallo = True
        intentos = intentos - 1
        print("FALLASTE! Te quedan {intentos} intentos".format(intentos=intentos))
    else:

        for key, value in enumerate(listaPalabraAdiv):
            if value == letra:
                listaPalabraMost[key] = value


    if intentos <= 0:
        run = False
        print('PERDISTE SUERTE LA PROXIMA, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
    elif listaPalabraAdiv == listaPalabraMost:
        run = False
        print('GANASTE!!, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
