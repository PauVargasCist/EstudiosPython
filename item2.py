"""
Ejercicio 2
Crea un programa en Python que solicite al usuario:
1. Ingresar un número entero del 1 al 9.
2. Que ingrese números secuenciales partiendo por 1, pero saltándose aquellos que sean múltiplos del
valor ingresado al comienzo.
3. En caso de ingresar un valor erróneo, enviar un mensaje indicando el error y el número que
correspondía ingresar
"""
#pedir el ingreso del número al usuario
numeroSolicitado = int(input("Por favor ingrese un número entero del 1 al 9: "))

contador = 1

#bucle while
while contador <= 10:

#se debe verificar si el número del conteo es múltiplo del ingresado en primera instancia
  if contador % numeroSolicitado == 0:
    contador +=1
    continue
 
  entrada= int(input("Ingrese el siguiente número: "))

 #verificar que la entrada coincide con el contador ingresado
  if entrada == contador:
    contador += 1 #si corresponde se autoincrementa 
    print("número correcto")
  else:
    print(f"incorrecto, el  número correcto es: {contador}") 

    continuar = input("quieres continuar jugando?(si/no): ").lower()
    if continuar != 'si':
      print("juego finalizado")
      break
    else:
      print("entonces sigue jugando")

