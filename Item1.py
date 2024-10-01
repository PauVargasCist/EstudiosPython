"""
Ejercicio 1
Debes crear un programa que dibuje una matriz, según las siguientes consideraciones:
1. Solicitar la cantidad de filas.
2. Solicitar la cantidad de columnas.
3. Dibujar las filas y columnas solicitadas
"""
#pedir la cantidad de filas y columnas 
filas = int(input("Por favor ingrese la cantidad de filas que desea generar: "))
columnas = int(input("Por favor ingrese la cantidad de columnas que desea generar: "))

for i in range(filas):
 print("+"+"---+"*columnas)
 print("|   "*columnas+"|")

print("+"+"---+"*columnas)