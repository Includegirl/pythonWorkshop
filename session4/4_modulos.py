# Un módulo es un archivo que contiene definiciones (varibles y funciones)
# que pueden ser utilizadas una vez se hace 'import' del módulo

#### EJERCICIO 1 ####
# Corre la siguiente línea de código:
print sqrt(5)

# Automáticamente aparecerá el siguiente error:
# "NameError: name 'sqrt' is not defined."
# Porque Python aún no sabe lo que es sqrt-aún.

# Existe un módulo de Python llamado 'math' el cual
# incluye una serie de funciones y variables, dónde sqrt() 
# es una de ellas. Para accesar a estas funciones, lo único
# que necesitas la palabra clase 'import'.

# Cuando simplemente haces 'import' de un módulo de esta manera
# decimos que estamos haciendo un 'import' genérico.

# Sólo necesitas hacer dos cosas:
#    1. Escribir 'import math' antes de la función de 'sqrt()', 
#    2. Poner 'math.' antes de 'sqrt()', por lo que la función tendrá la forma de
#       math.sqrt(). Esto le dice a Python que no solo importe la función 'math', pero 
#       obtener la función 'sqrt()' a travéz de 'math'

#### EJERCICIO 2 ####
# Llama a math para que puedas correr la línea 6

