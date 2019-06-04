#!/usr/bin/python
 
class Calculadora:
  def __init__(self, uno, dos):
    self.numero = uno
    self.numerito = dos
 
  def Suma(self):
    print ("La suma de los 2 numeros es :: ", (self.numero+self.numerito))
 
  def Resta(self):
    print ("La resta de los 2 numeros es :: ", (self.numero-self.numerito))
 
  def Multiplicacion(self):
    print ("La multiplicacion de los 2 numeros es :: ", (self.numero*self.numerito))
 
  def Division(self):
    try:
      print("La division de los 2 numeros es  ", (self.numero/self.numerito))
    except Exception:
      print("No se puede dividir con cero!\n")
 
  def __del__(self):
    self.numero = None
    self.numerito = None
 
try:
 
  primero=int(raw_input("inserta un Numero :: "))
  segundo=int(raw_input("Inserta otro Numero :: "))
 
  Objeto=Calculadora(primero,segundo)
 
  try:
    opcion=int(input("Desea\n1 - Sumar\n2 - Restar\n3 - Nultiplicar\n4 - Dividir\n"))
    if (opcion == 1):
      Objeto.Suma()
    elif (opcion == 2):
      Objeto.Resta()
    elif (opcion == 3):
      Objeto.Multiplicacion()
    elif (opcion == 4):
      Objeto.Division()
    else:
      print("Debes elegir o uno o dos\n")
 
  except Exception:
      print ("Debes Insertar un numero!")
 
except Exception:
 
  print ("Debes Insertar solamente Numeros!\n")