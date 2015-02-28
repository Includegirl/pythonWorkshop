# En el ejercicio anterior
#     def square(n):
#     n es un parámetro de la función 'square'.
# Un parámetro actúa como el nombre de una variable
# a ser pasada como argumento.

# En el ejemplo anterior, llamamos la función 'square' con el argumento 10.
# En esta instancia la función fue llamada con la variable n,
# la cual tiene el valor de 10.

# Una función puede requerir los parámetros que desees,
# pero cuando hagas el llamado de esta funcion
# debes pasarle los argumentos de manera que concuerden.

#### EJERCICIO 1 ####
# Este ejercicio fue tomado diréctamente del curso codecademy.com
# Mira la función 'power'. La misma toma dos argumentos, la base y el exponente, y eleva el primero a la potencia
# del segundo, ahoa mismo no funciona, debido a que le faltan sus parámetros.

# Sustituye los blancos con los parámetros 'base' y 'exponent'
# y llama la función con una base de 2 a la potencia de 5.

def power(___, ___):  # Añade tus parámetros aquí
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(__,__)  # Añade tus argumentos aquí!
