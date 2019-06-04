import random

#Ejercicio 1
print('\t\t EJERCICIO 1\n')
print ("""*************************************
    NUMEROS DIVISIBLES ENTRE 7 
         Y MULTIPLOS DE 5
*************************************""")
i = 1500
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

#Ejercicio 2
print('\t\t EJERCICIO 2\n')
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

#Ejercicio 3
print('\t\t EJERCICIO 3\n')
print ("""*************************************
        ADIVINA!! el numero [0,9]
*************************************""")
numero  = random.randint(1, 9) #número aleatorio de 0 a 9
while True:
    num_usuario = int(input('Ingresa un numero del 1 al 9: '))
    if numero == num_usuario:
        print('Bien adivinado')
        break

#Ejercicio 4
print('\t\t EJERCICIO 4\n')
print ("""*************************************
        PATRON VISUAL
*************************************""")
for i in range(9):
    if i == 0 or i == 8:
        print('*')
    elif i == 1 or i == 7:
        print('>>')
    elif i == 2 or i == 6:
        print('***')
    elif i == 3 or i == 5:
        print('>>>>>>>>')
    else:
        print('**********')

#Ejercicio 5
print('\t\t EJERCICIO 5\n')
print ("""*************************************
        INVERSOR DE PALABARAS 
*************************************""")
cadena = str(input("INGRESA PALABRA \n "))
print(cadena [::-1])
    

#Ejercicio 6
print('\t\t EJERCICIO 6\n')
print ("""*************************************
    CONTADOR DE PARES E IMPARES [1,9]
*************************************""")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = 0
impares = 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print('Número de números pares: ', pares)
print('Número de numeros impares ', impares)

#Ejercicio 7
print('\t\t EJERCICIO 7\n')
print ("""*************************************
        VERIFICADOR DE CLASES DE DATOS
*************************************""")
datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"clase":'V','section':'A'}]

for i in datalist:
    print('El elemento: \t{0}\t  es de tipo:\t {1} '.format(i, type(i)))

#Ejercicio 8
print('\t\t EJERCICIO 8\n')
for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end=' ')

#Ejercicio 9
print('\t\t EJERCICIO 9\n')
print ("""*************************************
    SEPA EL FACTORIAL DE CUALQUIER NUMERO!!!
*************************************""")
n = int(input('Ingresa un número: '))

if n >= 0:
    
    if n == 0 or n == 1:
        print('El factorial de {0} es {1}'.format(n, 1))
    
    else:
        i = 1
        factorial = 1
        while i <= n:
            factorial *= i
            i += 1
        print('El factorial de {0} es {1}'.format(n, factorial))
        
else:
    print('Sólo se puede calcular el factorial a un número positivo :\ ')

#Ejercicio 10
print('\t\t EJERCICIO 10\n')
print ("""*************************************
    ESCRIBA OMITIENDO LAS VOCALES
*************************************""")
cadena = input('Ingresa una cadena: ')
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
cadena_sin_vocales = ''

for i in cadena: 
    if i in vocales:
        continue
    else: 
        cadena_sin_vocales += i 
        
print(cadena_sin_vocales)


