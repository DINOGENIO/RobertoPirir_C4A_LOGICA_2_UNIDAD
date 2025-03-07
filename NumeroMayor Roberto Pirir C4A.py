"""
Crear un programa el cual pida 3 números y
muestre en pantalla  cual es el mayor de los tres.

Roberto Pirir
C4A
"""

#Definir las variables con valor inicial 0
num1 = 0 #Valor inicial 0
num2 = 0 #Valor inicial 0
num3 = 0 #Valor inicial 0
#Pedimos los datos para las variables
#Se define que tipo de variables son.
num1 = int(input("Ingrese el primer numero: ")) #Ingresar el valor 
num2 = int(input("Ingrese el segundo numero: ")) #Ingresar el valor 
num3 = int(input("Ingrese el tercer numero: ")) #Ingresar el valor
#Condiciones IF ELSE
#SOLO ENTEROS
#No tocaremos el tema de booleanos o str. ya que son valores muy dificiles de tratar
print("************CONDICIÓN IF-ELSE*****************")

if num1 < 0 or num2 < 0 or num3 < 0:
    print("Algún numero es negativo")
else:
    if num1 < 0 and num2 < 0 and num3 < 0:
                print("Algún número es negativo")
    else:
        if num1 > num2 and num1 > num3:
            print("El numero {} es el mayor".format(num1))
        else:
            if num2 < num1 and num3 < num1:
                print("El numero {} es el mayor".format(num1))
            else:
                if num2 > num1 and num2 > num3:
                    print("El numero {} es el mayor".format(num2))
                else:
                    if num1 < num2 and num3 < num2:
                        print("El numero {} es el mayor".format(num2))
                    else:
                        if num3 > num1 and num3 > num2:
                            print("El numero {} es el mayor".format(num3))
                        else:
                            if num1 < num3 and num2 < num3:
                                print ("El numero {} es el mayor".format(num3))
                            else:
                                if num1 == num2 and num1 == num3:
                                    print("Los numeros son iguales")
"""
if num1 < 0 and num2 < 0 or num1 < 0 and num3 < 0 or num2 < 0 and num1 < 0 or num2 < 0 and num3 < 0 or num3 < 0 and num2 < 0 or num3 < 0 and num1 < 0:
    print ("Uno de los numeros es negativo")
"""                    
"""
^
*
*

No usar esto, si no quieres tener flotantes o negativos.
"""
