"""
Ejercicio 4
Elige dos palabras del mismo largo en las que dos letras iguales no coincidan en la misma posición. Por 
ejemplo, si se eligen las palabras "morena" y "pelito", cualquier "m" que aparezca en una frase será 
reemplazada por una "p", las letras "o" se reemplazan por "e", "r" por "l", "e" por "i", "n" por "t" y "a" por "o".
Crea un programa que:
1. Permita al usuario elegir dos palabras que cumplan con las condiciones mencionadas anteriormente.
2. Solicite al usuario que ingrese una frase.
3. Reemplace las letras según la regla establecida a partir de las palabras elegidas.
4. Imprima la nueva frase con las letras reemplazadas
"""
#se pide al usuario ingresar las palabras

palabraUno = input("Ingrese la primera palabra: ")
palabraDos = input("Ingrese la segunda palabra: ")

#solicitar al usuario que ingrese una oración

frase = input("Ingrese una frase u oración: ")

#se crea la variable que almacena la nueva frase

fraseNueva = ""

for letra in frase:
    if letra in palabraUno:
        indice = palabraUno.index(letra)
        fraseNueva += palabraDos[indice]
    else:
        fraseNueva += letra

print("la frase modificada es: ", fraseNueva)