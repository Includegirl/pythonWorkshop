""" Ya sabemos que existen los 'strings' y sabemos que existen
operadores como se explico en la sesión 1 de este taller.
¡Ahora... vamos a hacer una combinación de ambos!
"""

# Concatenación, en ocaciones queremos unir varios 
# strings y convertirlos en uno. Ejemplo:

print "Bienvenidos " + "al taller de " + "programación"

# ¿Porqué la siguiente linea de código de error?
# Hint: Tipos de variables
print "Me voy a comer " + 2 + " pedazos de pizza"
# ¿Qué aprendimos para resolver este problema?

##### EJERCICIO 1 #####
# ¿Cuántos pedazos de pizza te vas a comer tu?
# Escribe un string que diga cuántas te vas a comer
# e imprímela

""" ¿Qué pasa con la combinación de variables y 'strings'?
Al hacer esta acción existe un buen método con el operador %
"""
# Observar ¿Cuál es la función de %s?
string_1 = "Xiomara"
string_2 = "7"
print "No se porque %s. 'ordenó pizza para %s personas." % (string_1, string_2)

##### EJERCICIO 2 #####
# Complete el siguiente programa: http://bit.ly/1GiBnCG

""" El operador % sustituye %s con la variable correspondiente en el orden en que aparezcan """
