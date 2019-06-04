#encodind: utf-8

print ("""***************************
SEPA CUALES SON LOS NUMEROS QUE SON DIVISIBLES POR 7 

Y LOS MULTIPLOS DE 5, EN EL INTERVALO  [1500,2700]
***************************""")

print("Tarea 1: Numeros divisibles por 7")

print("La tarea 2: Numeros  que son multiplos de 5") #Los ultimos tres print son las instrucciones o para que funciona el programa.

opc = int(input("Seleccione tarea\n")) # Se declara una variable llamada opc para que el usuario elija una de las dos tareas posibles.

while 1 and 2: 
	if (opc == 1):
		n = 1500
		for n in range(1500,2700):
			if n %7 == 0:
				print (n)
			n += n
		
	if (opc == 2):
		a=1500
		for a in range(1500,2700):
			if a %5 == 0:
				print (a)
			a += a
	print("*SE LE DEJA AL LECTOR COMPROBAR PARA CADA NUMERO DE LA LISTA*")
	n += 1
	a += 1		
	