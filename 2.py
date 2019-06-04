#encodind: utf-8
print ("""*************************************
CONVERSOR DE TEMPERATURAS DE ºC a ºF 
         y DE ºF a ºC.
*************************************""")

opc = int(input("CONVERSION\n1.ºC a ºF\n2.ºF a ºC\n"))
if opc == 1:
	celsius = int(input("INGRESA LA TEMPERATURA\n"))
	f = celsius * (1.8) + 32
	print(int(f))
else:
	farenheit = int(input("INGRESA LA TEMPERATURA\n"))
	c = (farenheit - 32) / 1.8
	print(int(c))