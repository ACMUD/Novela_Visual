#-------------------------------------------------------------------------------
# Name:        Expresiones init
# Purpose:     Presentar la colección completa de métodos, clases y
#               dependencias utiles para la redacción de expresiones
#               comunes con selección aleatoria de IAN
#
# Author:      Tatterdemalion
#
# Created:     19/09/1999
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

""" Paquete: Redactor de expresiones de IAN

Empaqueta aquellos métodos, clases y dependencias que realizan
las redacción de expresiones. Cada módulo en el paquete cuenta
con al menos un método para realizar una petición de expresión
y opcionalmente un diccionario de expresiones.

Referencia:
    get_expr (callable -> (str,list)):
        método para realizar una petición
    expresione (list -> (str,list)):
        diccionario de expresiones
    len_expr (int):
        tamaño de expresione
"""