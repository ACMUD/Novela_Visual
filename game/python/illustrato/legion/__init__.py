#-------------------------------------------------------------------------------
# Name:        Legion init
# Purpose:     Presentar la colección completa de métodos, clases y
#               dependencias utiles para la ilustracion de personajes
#               con personalidad de IAN
#
# Author:      Quaere Gipsy
#
# Created:     01/09/0909
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

""" Paquete: Ilustración de personajes de IAN

Empaqueta aquellos métodos, clases y dependencias que realizan
la ilustración de personajes.

Referencia:
    "Mi nombre es Legión, pues somos muchos", Marcos 5:9
        (En referencia a los muchos personajes que el paquete
         debe crear)
"""

def create(gen_b: str, gen_l: str, url: str = None):
    cuerpos = {'M': {None: [i+1 for i in range(7) if i not in [4,5]],
                     'Aventura': [],
                     'Comedia': [],
                     'Fantasía': [5],
                     'Terror': [],
                     'Acción': [],
                     'Suspenso': [],
                     'Romance': [],
                     'Ciencia Ficción': [],
                     'Drama': [],
                     'Misterio': []},
               'F': {None: [i+1 for i in range(9) if i not in [4]],
                     'Aventura': [],
                     'Comedia': [],
                     'Fantasía': [5],
                     'Terror': [],
                     'Acción': [],
                     'Suspenso': [],
                     'Romance': [],
                     'Ciencia Ficción': [],
                     'Drama': [],
                     'Misterio': [6]}}

    pelo = {'M': [None] + [i+1 for i in range(2)],
            'F': [i+1 for i in range(1)]}

    import random as rd
    num_cuerpo = rd.choice(cuerpos[gen_b][gen_l] +
                           cuerpos[gen_b][None])
    num_pelo = rd.choice(pelo[gen_b])

    import os
    if not url:
        url = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
    os.system(f'"{url}/personaxe.py" {gen_b} {num_cuerpo} {num_pelo}')