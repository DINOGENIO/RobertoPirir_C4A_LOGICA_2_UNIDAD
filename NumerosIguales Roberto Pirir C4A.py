"""
Crear un programa el cual pida 3 números
y debe mostrar la cantidad de iguales o bien sin son diferentes.

Roberto Pirir
C4A
"""
#Definir variables como 0 de inicial
num1 = 0
num2 = 0
num3 = 0
#Pedir valores
num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un segundo valor: "))
num3 = int(input("Ingrese un tercer valor: "))
#If - Else
if num1 < 0 or num2 < 0 or num3 < 0:
    print("Algún número es negativo")
else: #num1
    if num1 == num2 and num1 != num3:
        print("Hay 2 numeros iguales")
        print("Hay 1 numero diferente")
    else:
        if num1 == num3 and num1 != num2:
            print("Hay 2 numeros iguales")
            print("Hay 1 numero diferente")
        else:
            if num1 == num3 and num1 == num2:
                print("todos los numeros son iguales")
            else:
                if num1 != num2 and num1 != num3:
                    print("Hay 2 numeros iguales")
                    print("Hay 1 numero diferente")
                else:
                    if num2 == num1 and num2 != num3:
                        print("Hay 2 numeros iguales")
                        print("Hay 1 numero diferente")
                    else:
                        if num2 != num1 and num2 == num3:
                            print("Hay 2 numeros iguales")
                            print("Hay 1 numero diferente")
                        else:
                            if num2 !=num1 and num2 != num3:
                                print("Todos los numeros son diferentes")
                            else:
                                if num2 == num3 and num2 != num1:
                                    print("Hay 2 numeros iguales")
                                    print("Hay 1 numero diferente")
                                else:
                                    if num3 == num2 and num3 != num1:
                                        print("Hay 2 numeros iguales")
                                        print("Hay 1 numero diferente")
                                    else:
                                        if num3 == num1 and num3 != num2:
                                            print("Hay 2 numeros iguales")
                                            print("Hay 1 numero diferente")
                                        else:
                                            if num3 == num2 and num3 != num1:
                                                print("Hay 2 numeros iguales")
                                                print("Hay 1 numero diferente")
                                            else:
                                                if num3 != num1 and num3 != num2:
                                                    print("Todos los numeros son diferentes")
                                    
                                            
                                    
                
