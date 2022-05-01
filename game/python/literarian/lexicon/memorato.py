#-------------------------------------------------------------------------------
# Name:        Rememorador léxico
# Purpose:     Presentar la colección completa de métodos, clases y
#               dependencias utiles para buscar terminologia en la
#               memoria de IAN
#
# Author:      Fellow
#
# Created:     15/04/2019
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

def conmemorar(file_db: str, data: str) -> int:
    with open(file_db,
              encoding='utf-8',
              errors='ignore') as file:
        return file.read().find(data.replace('\n',''))

def rememorar(file_db: str, data: str) -> bool:
    return conmemorar(file_db,data) != -1

def remembrar(file_db: str,
              criterio: str,
              pivote: (int,str) = 0,
              obteniendo: (int,str,list((int,str))) = -1) -> list:
    from os.path import exists

    if exists(file_db):
        with open(file_db,
                  encoding='utf-8',
                  errors='ignore') as file:
            all_data = file.read()
    else:
        all_data = file_db

    all_data = [i.split('\t')
                for i in all_data.split('\n')
                if i != '' and
                   i != '\n']
    head = tuple(all_data[0])
    all_data.pop(0)

    if type(pivote) == str:
        assert pivote in head, ("Error de pivote: en la cabecera del " +
                                "archivo debe estar incluido el pivote")
        pivote = head.index(pivote)

    if type(obteniendo) in [int, str]:
        # list(obteniendo) puede convertir un str en una lista
        #  de char, por eso [obteniendo]
        obteniendo = [obteniendo]

    for i,c in enumerate(obteniendo): #i: index, c: column
        if type(c) == str:
            assert c in head, ("Error de obtencion: en la cabecera del " +
                                f'archivo debe estar incluido {c}')
            obteniendo[i] = head.index(c)

        if type(c) == int:
            if c == -1:
                obteniendo = [k for k in range(len(head)) if k != pivote]
                break

            else:
                assert c < len(head) and c >= 0, ("Error de obtencion: " +
                                "indice de cabecera fuera de rango " +
                                f'[0, {len(head) - 1}]')

    return_data = {head[j]:[] for j in obteniendo}

    for i,r in enumerate(all_data):
        if r[pivote] == criterio:
            for j,c in enumerate(r):
                if j in obteniendo and c not in return_data[head[j]]:
                    return_data[head[j]].append(c)

    return return_data