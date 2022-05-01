#-------------------------------------------------------------------------------
# Name:        Asimilador léxico
# Purpose:     Presentar la colección completa de métodos, clases y
#               dependencias utiles para añadir terminológica a la
#               memoria de IAN
#
# Author:      Fellow
#
# Created:     15/04/2019
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

def asimilar(file_db : str,
             data: str,
             srch_fntn: callable = lambda *dmmy: False):

    with open(file_db,
              'a+',
              encoding='utf-8',
              errors='ignore') as file:
        for line in data.split('\n'):
            if line != '' and not srch_fntn(file_db,line):
                file.write(line + '\n')