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

expresione = [["es una persona {desc}",
              "con un dominio emocional {desc}, honestamente",
              "es {desc}, eso sí",
              "y {desc}.",
              "Dentro de todo, se puede decir que es {desc}; y eso está bien"]]
len_expr = len(expresione)
redator = None
vocab = None
descrip = [["muy introvertida",
            "un poco introvertida",
            "extrovertida",
            "muy extrovertida",
            "demasiado extrovertida"],
           ["pesimo",
            "regular",
            "normal",
            "bueno",
            "excelente"],
           ["muy poco amable",
            "un poco amable",
            "amable... a veces",
            "muy amable",
            "super amable"],
           ["casi nunca nota como es con los demás",
            "no siempre se percata de su trato a los demás",
            "normalmente trata bien a los demás",
            "tiene empatia",
            "es super perceptivo al hablar con los demás"],
           ["un poco lento...",
            "cerrado de mente",
            "bastante promedio con sus ideas",
            "listo... no una lumbrera, pero si lo suficiente para destacar",
            "super-inteligente y creativo"]]

def update_redator():
    global redator
    if not redator:
        redator = get_expr_generator()
    else:
        redator = None

def update_vocab(new_vocab: list):
    global vocab
    if type(new_vocab) == str:
        new_vocab = new_vocab.split('\n')
    if type(new_vocab) == list and len(new_vocab) == len(expresione[0]) + 1:
        new_vocab = new_vocab[1:]
    if redator and not vocab:
        vocab = None
    else:
        if not new_vocab:
            vocab = [0 for i in range(len_expr)]
        else:
            vocab = new_vocab

def get_descriptor(i: int,value_person: int) -> str:
    if i == 5:
        return descrip[i][value_person + 39 // 27]
    return descrip[i][value_person // 25]

def get_expr_generator():
    for i,z in enumerate(list(zip(choice(expresione),vocab))):
        yield z[0].replace('{desc}',
                         get_descriptor(i,int(z[1])))

def get_expr(new_vocab: list = None) -> str:
    update_vocab(new_vocab)
    try:
        return redator.send(None)
    # Si redator es None saltará la excepción AttributeError por
    #  carecer del método send
    # Si el generador no tiene más retornos saltará la excepción
    #  StopIteration lanzada por el generador
    except (StopIteration,AttributeError):
        update_redator()
        return get_expr(new_vocab)