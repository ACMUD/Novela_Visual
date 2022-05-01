#-------------------------------------------------------------------------------
# Name:        Overtura
# Purpose:     Módulo de expresiones comunes para abrir una narración
#
# Author:      Fellow
#
# Created:     19/04/2005
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

from random import choice

expresione = [["La historia que quiero contar comienza así:\n",
               "¿Quieres que continue?",
               "De acuerdo, pero entonces ambientaré adecuadamente el asunto"],
              ["Empecemos con la historia: \n\"",
               "¿Te parece si sigo?",
               "Vale. Sin embargo, empezaré a narrar... mejorcito"]]
len_expr = len(expresione)
redator = None

def update_redator():
    global redator
    if not redator:
        redator = get_expr_generator()
    else:
        redator = None

def get_expr_generator():
    for i in choice(expresione): yield i

def get_expr():
    try:
        return redator.send(None)
    # Si redator es None saltará la excepción por carecer del método send
    # Si el generador no tiene más retornos saltará la excepción (inmanejable)
    #  lanzada por el generador (StopIteration)
    except:
        update_redator()
        return get_expr()