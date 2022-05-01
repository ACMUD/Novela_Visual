#-------------------------------------------------------------------------------
# Name:        Salutaciones
# Purpose:     Módulo de expresiones comunes de salutación
#
# Author:      Tatterdemalion
#
# Created:     19/09/1999
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

import random as rd

expresione = ["¡Hola, soy IAN!",
              "¡Saludos! Mi nombre es IAN"]
len_expr = len(expresione)

def get_expr():
    return expresione[rd.randint(0,len_expr-1)]