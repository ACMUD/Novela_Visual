#-------------------------------------------------------------------------------
# Name:        Línea lógica
# Purpose:     Módulo de redacción de línea lógica
#
# Author:      Fellow
#
# Created:     15/04/2019
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

""" Módulo: Redactor de línea logica de IAN

Se vale de la memoria para generar una logline.

Referencia:
    La línea lógica (logline) de una historia es en literatura
     la reducción silogistica de la trama a sus minimos
     arquetípicos:
        - protagonista
        - acción
        - objetivo
        - contexto locativo y temporal
        - elemento de oposición
"""

class redator:
    # los dominios a los que acude la sintaxis para escribir
    voc_domain = ['nombres',
                  'verbos_modal',
                  'verbos',
                  'complementos',
                  'lugares',
                  'fechas']
    # las sintaxis que usará el redactor para escribir
    sintax = [(0,1,2,3,'en',4,'durante',5),
              ('durante',5,',',0,1,2,3,'en',4)]

    def __init__(self,
                 get_lex: str,
                 memor_view: callable,
                 sesgos: list = []):
        self.lexico = get_lex(self.voc_domain)
        self.sesgos = ['None'] + sesgos
        self.memory = memor_view
        self.letter = ''

    def shuffler(self, domain: (list,str) = voc_domain) -> list:
        if type(domain) == list:
            deck = {}
            for i in domain:
                deck.update(self.shuffler(i))
            return deck

        deck = []
        for i in self.sesgos:
            deck.extend(self.memory(self.lexico[domain],
                                    i,
                                    'género_l',
                                    domain)[domain])

        from random import shuffle
        shuffle(deck)
        return {domain: deck}

    def chooser(self, vocab: (dict,list)) -> str:
        if type(vocab) == dict:
            return {i:
                    self.chooser(vocab[i])
                    for i in vocab}

        from random import choice
        return choice(vocab)

    def writer(self) -> str:
        _sintax = self.chooser(self.sintax)
        self.letter = ''

        for i in _sintax:
            if type(i) == str:
                self.letter += i
            elif type(i) == int:
                self.letter += self.chooser(
                                    self.shuffler(
                                         self.voc_domain[i]
                                                 )
                                           )[self.voc_domain[i]]
            self.letter += ' '
        self.letter = self.letter[0].upper() + self.letter[1:-1]
        return self.letter

def write(get_lex: callable,
          memor_view: callable,
          sesgos: list = []) -> str:
    # Estructura básica de escritura:
    #   + Nombre
    #   + Verbo_modal
    #   + Verbo
    #   + Complemento {[con,por] {,articulo,posesivo}_,a la _,al _}
    #   + Preposicion {en}
    #   + Lugar
    #	+ Preposicion {durante}
    #   + Fecha
    r = redator(get_lex,memor_view,sesgos)
    return r.writer()