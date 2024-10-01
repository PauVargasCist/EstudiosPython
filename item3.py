"""
Ejercicio 3
Un año bisiesto es un año con 366 días en vez de 365. Cada 4 años, febrero tiene un día más. Esto se
hace porque un año oficialmente no tiene 365 días, sino 365,25 días. Añadiendo un día cada 4 años, se
soluciona este problema. Sin embargo, la regla no se aplica a los años de siglo a menos que sean
divisibles por 400. Por ejemplo, 1900 no fue un año bisiesto porque es divisible por 100 pero no por 400,
mientras que 2000 sí fue un año bisiesto porque es divisible por 400.
Cree un programa en Python que permita:
1. Pedir al usuario el año de nacimiento de una persona.
2. Pedir al usuario el año de muerte de la persona.
3. Si la persona sigue viva, el año de muerte será 0. En este caso, el programa debe reemplazar el 0
por el año actual.
4. Calcular la cantidad de años bisiestos que la persona ha vivido.
5. Mostrar la cantidad de años bisiestos calculados en el paso anterior.
"""

#1. Pedir al usuario el año de nacimiento de una persona.

anioNacimiento = int(input("por favor, ingrese su año de nacimiento: "))
anioMuerte = int(input("por favor, ingrese el año de muerte si corresponde. Si no corresponde poner año de muerte, ingrese un 0: "))

if anioMuerte == 0:
 anioMuerte= 2024


cantidadBisiestos = 0
for anio in range(anioNacimiento,anioMuerte+1):
   if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
      cantidadBisiestos +=1

print("La cantidad de años bisiestos que ha vivido son: ", cantidadBisiestos)
       



