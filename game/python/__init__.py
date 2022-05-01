#-------------------------------------------------------------------------------
# Name:        Python IAN init
# Purpose:     Presentar la colección completa de métodos, clases y
#               dependencias de inicialización del proyecto IAN
#
# Author:      Tatterdemalion
#
# Created:     19/09/1999
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

import os

DIR_MAIN = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
if DIR_MAIN[-6:] == 'python':
    DIR_MAIN = DIR_MAIN[:-7] #\python = 7 chars
    if DIR_MAIN[-4:] !='game':
        DIR_MAIN += '/game'
DIR_DB = '/persistence'
DIR_IMAGE = '/images'
DIR_AUDIO = '/audio'
DIR_BG = '/background'
DIR_MUSIC = '/music'

FILE_GENEROS = '/generos.txt'

def url_recourse_maker(tree: list,
                       type_rcrs: str = None,
                       url: str = '') -> str:
    if url == '':
        if type_rcrs == 'db':
            tree = [DIR_MAIN,DIR_DB] + tree

        if type_rcrs == 'bg':
            tree = [DIR_MAIN,
                    DIR_IMAGE,
                    DIR_BG] + tree

        if type_rcrs == 'musc':
            tree = [DIR_MAIN,
                    DIR_AUDIO,
                    DIR_MUSIC] + tree

    if len(tree) != 0:
        return url_recourse_maker(tree[1:],
                                  type_rcrs,
                                  url + tree[0])

    return url

try:
    with open(url_recourse_maker([FILE_GENEROS],
                                 'db'),
              encoding='utf-8',
              errors='ignore') as file:
        GENEROS = [line.rstrip() for line in file]
except FileNotFoundError:
    raise FileNotFoundError("El archivo de generos literarios no está" +
                            "ubicado en la ubicación que esperaba (" +
                            f"{url_recourse_maker([FILE_GENEROS],'db')}")

from functools import partial
from python.literarian.lexicon import get_lex
get_lexer = partial(get_lex,url_recourse_maker)