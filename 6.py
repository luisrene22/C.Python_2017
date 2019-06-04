print("Programa contador de pares e impares")
numeros = int(input("INGRESE LOS NUMEROS SIN ESPACIOS \n "))

def contar_pares (numeros):
	numeros = str (numeros)
	par = 0
	for elemento in numeros:
		elemento = int(elemento)
		if elemento %2 == 0:
			par = par + 1
	return par

def contar_impares (numeros):
	numeros = str (numeros)
	impar = 0
	for elemento in numeros:
		elemento = int(elemento)
		if elemento %2 != 0:
			impar = impar + 1
	return impar

pares = contar_pares(numeros)
impares = contar_impares(numeros)

print("Número de números pares",pares,)
print("Número de números impares",impares)