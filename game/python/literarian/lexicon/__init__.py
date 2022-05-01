#-------------------------------------------------------------------------------
# Name:        Léxico init
# Purpose:     Presentar la colección completa de métodos, clases y
#               dependencias utiles para ser la memoria terminológica
#               de IAN
#
# Author:      Fellow
#
# Created:     15/04/2019
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

# nombres, género_b: sexo biologico, género_l: género literario
INIT_NOMBRES = ('nombres\tgénero_b\tgénero_l\n' +
                'Jean\tM\tNone\nPeter\tM\tNone\nAndrea\tF\tNone\n' +
                'Andres\tM\tNone\nRobert\tM\tNone\nJackson\tM\tNone\n' +
                'Daniel\tM\tNone\nDunhan\tM\tNone\nVictoria\tF\tNone\n' +
                'Eliot\tM\tNone\nCarolina\tF\tNone\nMaria\tF\tNone\n' +
                'Brayan\tM\tNone\nSantiago\tM\tNone\nJuana\tF\tNone\n' +
                'Sebastian\tM\tNone\nJennifer\tF\tNone\nRicardo\tM\tNone\n' +
                'Jean\tF\tAventura\nDave\tM\tAventura\nPhileas\tM\tAventura\n' +
                'Peter\tM\tComedia\nSimon\tM\tComedia\nBeti\tF\tComedia\n' +
                'Legolas\tM\tFantasía\nLucifer\tM\tFantasía\n' +
                'Lucifer\tF\tFantasía\nGabriel\tM\tFantasía\n' +
                'Natalia\tF\tTerror\nJack\tM\tTerror\nDexter\tM\tTerror\n' +
                'John\tM\tAcción\nMs. Smith\tF\tAcción\n' +
                'Mr. Smith\tM\tAcción\nJames\tM\tAcción\n' +
                'Robert\tM\tSuspenso\nAna\tF\tSuspenso\nJeff\tM\tSuspenso\n' +
                'Amelia\tF\tRomance\nJuliana\tF\tRomance\n' +
                'Alejandro\tM\tRomance\n' +
                'Mark\tM\tCiencia Ficción\nMarie\tF\tCiencia Ficción\n' +
                'Elon\tM\tCiencia Ficción\n' +
                'Juan\tM\tDrama\nChristopher\tM\tDrama\nVictoria\tF\tDrama\n' +
                'Alice\tF\tMisterio\nEliot\tM\tMisterio\nAgatha\tF\tMisterio\n')

# profesiones, género_a: género articular, género_l: género literario
INIT_PROFESIONES = ('profesiones\tgénero_a\tgénero_l\n' +
                    'pirata\tU\tNone\npirata\tU\tAventura\n' +
                    'pirata\tU\tFantasía\npirata\tU\tCiencia Ficción\n' +
                    'oficinista\tU\tNone\n' +
                    'hechicera\tF\tNone\nhechicero\tM\tNone\n' +
                    'hechicera\tF\tFantasía\nhechicero\tM\tFantasía\n' +
                    'hechicera\tF\tAventura\nhechicero\tM\tAventura\n' +
                    'estudiante\tU\tNone\n' +
                    'soldado\tU\tNone\nsoldado\tU\tAcción\n' +
                    'soldado\tU\tCiencia Ficción\nsoldado\tU\tAventura\n' +
                    'cantante\tU\tNone\n' +
                    'escritora\tF\tNone\nescritor\tU\tNone\n' +
                    'astronauta\tU\tNone\nastronauta\tU\tAcción\n' +
                    'astronauta\tU\tCiencia Ficción\nastronauta\tU\tTerror\n' +
                    'investigadora\tF\tNone\ninvestigador\tM\tNone\n' +
                    'investigadora\tF\tTerror\ninvestigador\tM\tTerror\n' +
                    'investigadora\tF\tSuspenso\ninvestigador\tM\tSuspenso\n' +
                    'investigadora\tF\tCiencia Ficción\n' +
                    'investigador\tM\tCiencia Ficción\n' +
                    'investigadora\tF\tTerror\ninvestigador\tM\tTerror\n' +
                    'periodista\tM\tDrama\nperiodista\tF\tDrama\n' +
                    'periodista\tM\tMisterio\nperiodista\tF\tMisterio\n' +
                    'sicario\tM\tNone\nsicaria\tF\tNone\n' +
                    'sicario\tM\tAcción\nsicaria\tF\tAcción\n' +
                    'sicario\tM\tCiencia Ficción\n' +
                    'sicaria\tF\tCiencia Ficción\n' +
                    'sicario\tM\tAventura\nsicaria\tF\tAventura\n' +
                    'sicario\tM\tTerror\nsicaria\tF\tTerror\n' +
                    'conductor\tM\tNone\nconductora\tF\tNone\n' +
                    'conductor\tM\tAcción\nconductora\tF\tAcción\n' +
                    'alpinista\tU\tNone\nalpinista\tU\tAventura\n' +
                    'futbolista\tU\tNone\n' +
                    'programador\tM\tNone\nprogramadora\tF\tNone\n' +
                    'programador\tM\tComedia\nprogramadora\tF\tComedia\n' +
                    'animadora\tF\tNone\nanimador\tM\tNone\n' +
                    'animadora\tF\tComedia\nanimador\tM\tComedia\n' +
                    'animadora\tF\tTerror\nanimador\tM\tTerror\n' +
                    'artista\tU\tNone\n' +
                    'actriz\tF\tNone\nactor\tM\tNone\n')

# verbos_modal, género_l: género literario
INIT_VERBOS_MODAL = ('verbos_modal\tgénero_l\n' +
                     'debe\tNone\nquiere\tNone\n' +
                     'tiene que\tNone\npuede\tNone\n')

# verbos, género_l: género literario
INIT_VERBOS = ('verbos\tgénero_l\n' +
               'viajar\tNone\nviajar\tAventura\n' +
               'sabotear\tNone\nsabotear\tAcción\n' +
               'encantar\tNone\nencantar\tFantasía\n' +
               'sobrevivir\tNone\nsobrevivir\tSuspenso\n' +
               'vengar\tNone\nvengar\tAcción\n' +
               'destruir\tNone\ndestruir\tCiencia Ficción\n' +
               'enamorar\tNone\nenamorar\tRomance\n' +
               'salvar\tNone\nsalvar\tFantasía\n' +
               'heredar\tNone\nheredar\tDrama\n' +
               'investigar\tNone\ninvestigar\tMisterio\n' +
               'descubrir\tNone\ndescubrir\tMisterio\n' +
               'asesinar\tNone\nasesinar\tAcción\n' +
               'triunfar\tNone\n' +
               'escapar\tNone\nescapar\tAventura\n' +
               'superar\tNone\n' +
               'exorcizar\tNone\nexorcizar\tTerror\n' +
               'fingir\tNone\nfingir\tComedia\n' +
               'desvelar\tNone\n')

# complementos, género_l: género literario
INIT_COMPLEMENTOS = ('complementos\tgénero_l\n' +
                     'con un compañero\tAventura\n' +
                     'a las ruinas\tAventura\n' +
                     'al tesoro\tAventura\n' +
                     'al trabajo\tComedia\n' +
                     'con madurez\tComedia\n' +
                     'con experiencia\tComedia\n' +
                     'a la princesa\tFantasía\n' +
                     'con sus poderes\tFantasía\n' +
                     'al villano\tFantasía\n' +
                     'con un asesino\tTerror\n' +
                     'con un espiritu\tTerror\n' +
                     'con un demonio\tTerror\n' +
                     'con su familia\tAcción\n' +
                     'con su pasado\tAcción\n' +
                     'a la mafia\tAcción\n' +
                     'al apocalipsis\tSuspenso\n' +
                     'a la secta\tSuspenso\n' +
                     'a la conspiración\tSuspenso\n' +
                     'con su pareja\tRomance\n' +
                     'con amor\tRomance\n' +
                     'con un imperio\tCiencia Ficción\n' +
                     'con una IA\tCiencia Ficción\n' +
                     'con una realidad\tCiencia Ficción\n' +
                     'con una relación\tDrama\n' +
                     'con pecado\tDrama\n' +
                     'con una enfermedad\tDrama\n' +
                     'por un caso\tMisterio\n' +
                     'por un homicidio\tMisterio\n' +
                     'por un hurto\tMisterio\n')

# lugares, género_l: género literario
INIT_LUGARES = ('lugares\tgénero_l\n' +
                'una misteriosa isla\tNone\n' +
                'una fiesta\tNone\n' +
                'el bosque alado\tNone\n' +
                'un campo de concentracion\tNone\n' +
                'Polonia\tNone\n' +
                'una villa\tNone\n' +
                'Francia\tNone\n' +
                'los restos de una colonia\tNone\n' +
                'la casa familiar\tNone\n' +
                'las ruinas de una antigua civilzacion\tNone\n' +
                'la Atlantida\tNone\n' +
                'el dorado\tNone\n' +
                'Agartha\tNone\n' +
                'Gilead\tNone\n' +
                'Transilvania\tNone\n' +
                'la Antartida\tNone\n' +
                'Londres\tNone\n' +
                'la capital\tNone\n' +
                'la reunion\tNone\n' +
                'una isla\tAventura\n' +
                'una oficina\tComedia\n' +
                'un bosque\tFantasía\n' +
                'una cabaña\tTerror\n' +
                'una metropoli\tAcción\n' +
                'una catedral\tSuspenso\n' +
                'un pueblo\tRomance\n' +
                'un planeta lejano\tCiencia Ficción\n' +
                'una villa\tDrama\n' +
                'el Londres\tMisterio\n')

# fechas, género_l: género literario
INIT_FECHAS = ('fechas\tgénero_l\n' +
               'el medioevo\tNone\n' +
               'la segunda guerra mundial\tNone\n' +
               'la noche de los muertos\tNone\n' +
               'la revolucion francesa\tNone\n' +
               'la conquista de america\tNone\n' +
               'la guerra fria\tNone\n' +
               'la primera guerra mundial\tNone\n' +
               'la conquista de africa\tNone\n' +
               'la guerra de los cien años\tNone\n' +
               'la guerra de los mil días\tNone\n' +
               'la carrera espacial\tNone\n' +
               'el renacimiento\tNone\n')

FILE_NOMBRES = '/nombres.txt'
FILE_PROFESIONES = '/profesiones.txt'
FILE_VERBOS_MODAL = '/verbos_modal.txt'
FILE_VERBOS = '/verbos.txt'
FILE_COMPLEMENTOS = '/complementos.txt'
FILE_LUGARES = '/lugares.txt'
FILE_FECHAS = '/fechas.txt'

def _url_maker(file,_) -> str:
    return __file__.replace('\\','/') + '/../../../../persistence' + file[0]

def get_lex(url_maker: callable,
            filtros: list((str,)) = None) -> str:
    return {i.replace('.txt',
                      '').replace('/',
                                  ''):
            url_maker([i],'db')
            for i in [FILE_NOMBRES,
                      FILE_PROFESIONES,
                      FILE_VERBOS_MODAL,
                      FILE_VERBOS,
                      FILE_COMPLEMENTOS,
                      FILE_LUGARES,
                      FILE_FECHAS]
            # si filtros es None (por defecto) devuelve todo el léxico
            if not filtros or
               # si filtros es una lista devuelve solo el léxico filtrado
               (type(filtros) == list and
                i.replace('.txt',
                          '').replace('/',
                                      '') in filtros)}

def main(url_maker: callable = _url_maker):
    from asimilato import asimilar
    from memorato import rememorar
    for i in [(FILE_NOMBRES,INIT_NOMBRES),
              (FILE_PROFESIONES,INIT_PROFESIONES),
              (FILE_VERBOS_MODAL,INIT_VERBOS_MODAL),
              (FILE_VERBOS,INIT_VERBOS),
              (FILE_COMPLEMENTOS,INIT_COMPLEMENTOS),
              (FILE_LUGARES,INIT_LUGARES),
              (FILE_FECHAS,INIT_FECHAS)]:
        asimilar(url_maker([i[0]],'db'),i[1],rememorar)

if __name__ == '__main__':
    main()