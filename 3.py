#encodind: utf-8

import random
puntero = random.randint(0,9)
oportunidades = 0
while True:
		numero = int(input("Elige un numero en el intervalo [0,9]\n"))
		if numero == puntero:
			print("LE ATINASTE!!!")
			break
		else:
			print("Introduce un numero otra vez")
			oportunidades += 1
			print("numero de oportunidades es:" +str(oportunidades))
print("¡BIEN ADIVINADO!")