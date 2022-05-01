init:
    ## Facilitadores
    $ next_dial = ''
    $ next_val = None

    ## Arquitectura Orientada a Servicios
    python:
        import sys
        sys.path.insert(0,'../game')
        from python import (url_recourse_maker,
                            GENEROS,
                            get_lexer)
        from python.literarian.redator.expresione.salute import get_expr as Isalut

    ## Personajes
    define IAN = Character('IAN', color="#023")

    ## Constantes
    python:
        for g in GENEROS:
            renpy.image('bg %s' % g,url_recourse_maker([f'/bg_genero/{g}.png'], 'bg'))

    python:
        musica_genero = {}
        for g in GENEROS:
            musica_genero[g] = url_recourse_maker([f'/sinopsis/{g}.ogg'], 'musc')

    image bg IAN think dim:
        Flatten(url_recourse_maker(['/choice_genero/choice_genero.png'],'bg'))
        alpha 0.5

    ## Estilos
    style menu:
        align (0.5, 0.5)

    style menu_button:
        area (0,0,800,40)
        idle_background '/gui/button/choice_idle_background.png'
        hover_background '/gui/button/choice_hover_background.png'

    style menu_button_text:
        color '#44f'
        align (0.5, 0.5)
        hover_color '#ccf'

## Pantallas Orientada a Servicios
screen screen_choice(title,items):
    window:
        style 'menu'
        vbox:
            text title align (0.5, 0.5)
            for i in items:
                button:
                    style 'menu_button'
                    text i style 'menu_button_text'
                    action [Return(i)]

label start:
    scene bg IAN think dim
    with fade
    $ next_dial = Isalut()
    IAN "[next_dial]"
    jump choice_genero

label choice_genero:
    stop music fadeout 1.0
    call screen screen_choice("¿Qué tipo de historia le gustaria leer?",GENEROS)
    $ genero = _return
    jump sinopsis

label sinopsis:
    $ renpy.show('bg %s' % genero, at_list = [top])
    $ renpy.music.set_volume(0.2, channel='music')
    $ renpy.music.play(musica_genero[genero],
                       channel='music',
                       loop=True,
                       synchro_start=True,
                       fadein=1)
    python:
        from python.literarian.redator.expresione.overture import get_expr as IOver
        next_dial = IOver()
    python:
        from python.literarian.redator.logline import write
        from python.literarian.lexicon.memorato import remembrar
        next_dial += write(get_lexer,remembrar,[genero])
    IAN "[next_dial]"
    scene bg IAN think dim
    with fade
    $ next_dial = IOver()
    call screen screen_choice("[next_dial]",["Sí, dale","No, mejor volvamos a empezar"])
    $ next_val = _return
    $ next_dial = IOver()
    if next_val == "Sí, dale":
        IAN "[next_dial]"
    else:
        IAN "Entiendo..."
        jump choice_genero