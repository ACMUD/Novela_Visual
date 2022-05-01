#Fondo
image Fo = "Fondo.png"
image Av = "Aventura.png"
image Co = "Comedia.png"
image Fa = "Fantasia.png"
image Te = "Terror.png"
image Ac = "Acción.png"
image Th = "Thriller.png"
image Ro = "Romance.png"
image Cf = "Ciencia_Ficción.png"
image Dr = "Drama.png"
image Mi = "Misterio.png"

#Personajes
define I = Character('IAN', color="#21618C")

label start:
    scene Fo
    with fade
    #Persistencia
    python:
        import os.path
        ##Variables estaticas
        #Personaje
        if os.path.isfile('Nombres.txt') != True:
            n = open('Nombres.txt','w')
            n.write("Jean-M Peter-M Andrea-F Andres-M Robert-M Jackson-M Daniel-M Dunhan-M Victoria-F Eliot-M Carolina-F Maria-F Brayan-M Santiago-M Juana-F Sebastian-M Jennifer-F Ricardo-M")
            n.close()
        if os.path.isfile('Profesiones.txt') != True:
            p = open('Profesiones.txt','w')
            p.write("pirata-U oficinista-U hechicera-F estudiante-U soldado-U cantante-U escritor-M astronauta-U investigador-M periodista-U sicario-M conductor-M alpinista-U futbolista-U programador-M animador-M artista-F actriz-F")
            p.close()
        #Verbo Modal
        vM = ['debe','quiere','tiene que']
        #Verbo
        if os.path.isfile('Verbos.txt') != True:
            v = open('Verbos.txt','w')
            v.write("viajar/1-0,4,1/ sabotear/0-3,3,2/ encantar/2-3,3,3/ sobrevivir/1-1,0,4/ vengar/0-1,3,5/ destruir/0-2,2,6/ enamorar/0-1,3,7/ salvar/0-3,3,8/ heredar/0-2,4,9/ investigar/0-3,3,10/ descubrir/1-0,3,8/ asesinar/1-1,1,4/ triunfar/1-0,1,2,3/ escapar/3-0,0,5/ superar/1-1,0,3/ exorcizar/1-3,3,4/ escapar/3-0,3,4/ fingir/1-0,3,6/ desvelar/1-0,3,10/")
            v.close()
        #Complemento
        cM = ['con','a']
        if os.path.isfile('Sujetos.txt') != True:
            s = open('Sujetos.txt','w')
            s.write("reina-1-2-1-la/ prisionero-1-3-1-el/ reliquia-2-3-1-la/ tesoro-2-3-1-el/ vaca-1-3-2-la/ niño-1-1-2-el/ oficina-2-3-2-la/ trafico-2-3-2-el/ elfa-1-3-3-la/ dragon-1-3-3-el/ gema-2-3-3-la/ mundo-2-3-3-el/ criatura-1-3-4-la/ asesino-1-3-4-el/ masacre-2-3-4-la/ cementerio-2-3-4-el/ mafia-1-3-5-la/ padrino-1-2-5-el/ pistola-2-3-5-la/ crimen-2-3-5-el/ momia-1-3-6-la/ vampiro-1-3-6-el/ epidemia-2-3-6-la/ apocalipsis-2-2-6-el/ amante-1-1-7-la/ amigo-1-3-7-el/ rosa-2-3-7-la/ amor-2-3-7-el/ IA-1-3-8-la/ marciano-1-3-8-el/ nave-2-3-8-la/ planeta-2-3-8-el/ madrastra-1-3-9-la/ esposo-1-3-9-el/ enfermedad-2-3-9-la/ destino-2-3-9-el/ sospechosa-1-3-10-la/ detective-1-3-10-el/ investigacion-2-3-10-la/ misterio-2-3-10-el/ organizacion-2-3-1-la/ gema-2-3-3-la/ elixir-2-3-3-el/ portal-2-3-8-el/ desafio-2-3-el/ impostor-1-1-6-el/ ataque-2-1-5-el/ inundacion-2-1-9-la/ dimension-2-1-3-la/")
            s.close()
        #Lugar
        if os.path.isfile('Lugar.txt') != True:
            l = open('Lugar.txt','w')
            l.write("una misteriosa isla*-5000,5000/una fiesta*-5000,5000/el bosque alado*-5000,0/un campo de concentracion*1939,1945/Polonia*1025,5000/una villa*-5000,5000/Francia*481,5000/los restos de una colonia*-5000,5000/la casa familiar*0,5000/las ruinas de una antigua civilzacion*0,5000/la Atlantida*-5000,-2000/el dorado*-5000,1000/Agartha*-5000,5000/Transilvania*1000,1800/la Antartida*-5000,5000/Londres*43,5000/la capital*-5000,5000/la reunion*0,5000/")
            l.close()
        #Fecha
        if os.path.isfile('Fecha.txt') != True:
            f = open('Fecha.txt','w')
            f.write("el medioevo*476,1492/la segunda guerra mundial*1939,1945/la noche de los muertos*1921,5000/la revolucion francesa*1789,1799/conquista de america*1492,1800/guerra fria*1950,1990/primera guerra mundial*1914,1918/conquista africa*1800,1910/guerra de los cien años*1337,1453/guerra de los mil días*1899, 1902/carrera espacial*1955,1975/renacimiento*1300,1600/")
            f.close()
    #Creación de Sinopsis
    I "¡Hola, soy IAN!"
    I "Elige el género de tu historia:"
    menu:
        "Aventura":
            $g = '1'
            scene Av
            with fade
        "Comedia":
            $g = '2'
            scene Co
            with fade
        "Fantasía":
            $g = '3'
            scene Fa
            with fade
        "Terror":
            $g = '4'
            scene Te
            with fade
        "Acción":
            $g = '5'
            scene Ac
            with fade
        "Thriller":
            $g = '6'
            scene Th
            with fade
        "Romance":
            $g = '7'
            scene Ro
            with fade
        "Ciencia Ficción":
            $g = '8'
            scene Cf
            with fade
        "Drama":
            $g = '9'
            scene Dr
            with fade
        "Misterio":
            $g = '10'
            scene Mi
            with fade
    ##Creación de listas
    python:
        ##Personaje
        #Nombre
        n = open('Nombres.txt','r')
        nM = n.read()
        n.close()
        nombre = []
        aux2 = ''
        while nM != '':
            aux = nM[0]
            if aux != '-':
                aux2 += aux
            else:
                nom = aux2
                aux2 = ''
                nM = nM[1:]
                gen = nM[0]
                nombre.append([nom,gen])
                nM = nM[1:]
            nM = nM[1:]
        #Profesion
        p = open('Profesiones.txt','r')
        pF = p.read()
        p.close()
        Profesion = []
        aux2 = ''
        while pF != '':
            aux = pF[0]
            if aux != '-':
                aux2 += aux
            else:
                pro = aux2
                aux2 = ''
                pF = pF[1:]
                gen = pF[0]
                Profesion.append([pro,gen])
                pF = pF[1:]
            pF = pF[1:]
        ##Verbo
        v = open('Verbos.txt','r')
        vB = v.read()
        v.close()
        verbo = []
        aux2 = ''
        while vB != '':
            aux = vB[0]
            if aux != '/':
                aux2 += aux
            else:
                nom = aux2
                aux2 = ''
                vB = vB[1:]
                t1 = vB[0]
                vB = vB[2:]
                t2 = vB[0]
                vB = vB[2:]
                aP = vB[0]
                vB = vB[2:]
                tH = ''
                while vB[0] != '/':
                    tH += vB[0]
                    vB = vB[1:]
                verbo.append([nom,t1,t2,aP,tH])
                vB = vB[1:]
            vB = vB[1:]
        ##Sujeto
        s = open('Sujetos.txt','r')
        sJ = s.read()
        s.close()
        sujeto = []
        aux2 = ''
        while sJ != '':
            aux = sJ[0]
            if aux != '-':
                aux2 += aux
            else:
                nom = aux2
                aux2 = ''
                sJ = sJ[1:]
                tp = sJ[0]
                sJ = sJ[2:]
                sP = sJ[0]
                sJ = sJ[2:]
                tH = ''
                while sJ[0] != '-':
                    tH += sJ[0]
                    sJ = sJ[1:]
                sJ = sJ[1:]
                pre = ''
                while sJ[0] != '/':
                    pre += sJ[0]
                    sJ = sJ[1:]
                sujeto.append([nom,tp,sP,tH,pre])
                sJ = sJ[1:]
            sJ = sJ[1:]
        ##Lugar
        l = open('Lugar.txt','r')
        lG = l.read()
        l.close()
        lugar = []
        aux2 = ''
        while lG != '':
            aux = lG[0]
            if aux != '*':
                aux2 += aux
            else:
                lug = aux2
                aux2 = ''
                lG = lG[1:]
                while lG[0] != ',':
                    aux2 += lG[0]
                    lG = lG[1:]
                fI = aux2
                aux2 = ''
                lG = lG[1:]
                while lG[0] != '/':
                    aux2 += lG[0]
                    lG = lG[1:]
                fF = aux2
                aux2 = ''
                lugar.append([lug,fI,fF])
            lG = lG[1:]
        ##Fecha
        f = open('Fecha.txt','r')
        fC = f.read()
        f.close()
        fecha = []
        aux2 = ''
        while fC != '':
            aux = fC[0]
            if aux != '*':
                aux2 += aux
            else:
                nom = aux2
                aux2 = ''
                fC = fC[1:]
                while fC[0] != ',':
                    aux2 += fC[0]
                    fC = fC[1:]
                fI = aux2
                aux2 = ''
                fC = fC[1:]
                while fC[0] != '/':
                    aux2 += fC[0]
                    fC = fC[1:]
                fF = aux2
                aux2 = ''
                fecha.append([nom,fI,fF])
            fC = fC[1:]
    #Adicion de nuevos elementos
    ##Variables a usar
    $nombreP = ''
    $ProfesionP = ''
    $edadP = ''
    $verboM = ''
    $verboP = ''
    $compF = ''
    $sujetoU = ''
    $ProfesionS = ''
    $verboS = ''
    $sujetoD = ''
    $lugarS = ''
    $fechaS = ''
    I "¿Quieres hacer tu historia más personalizada?"
    menu:
        "Sí":
            jump Escritura
        "No":
            jump Adicion

label Escritura:
    I "¿Qué deseas añadir?"
    menu:
        "Personaje":
            jump Personaje
        "Acción":
            jump Verbo
        "Sujeto":
            jump Sujeto
        "Lugar":
            jump Lugar
        "Fecha":
            jump Fecha

label Personaje:
    python:
        eD = True
        while(eD):
            nombreP = renpy.input("¿Qué nombre deseas para el personaje?")
            nombreP = nombreP.strip()
            aux = 0
            for i in range(0,len(nombre)):
                if nombreP.lower() == nombre[i][0].lower():
                    aux = 1
            if aux == 0 and nombreP != '':
                eD = False

    I "¿Es masculino o femenino?"
    menu:
        "Femenino":
            $genero = 'F'
            $vA = 'a'
        "Masculino":
            $genero = 'M'
            $vA = ''
    python:
        n = open('Nombres.txt','a')
        n.write(" " + nombreP + "-" + genero)
        n.close()
    I "¿Deseas añadir alguna profesión a [nombreP]?"
    menu:
        "Sí":
            python:
                eD = True
                while(eD):
                    ProfesionP = renpy.input("¿Cuál es la profesión de [nombreP]?")
                    ProfesionP = ProfesionP.strip()
                    aux = 0
                    for i in range(0,len(Profesion)):
                        if ProfesionP.lower() == Profesion[i][0].lower():
                            aux = 1
                    if aux == 0 and ProfesionP != '':
                        eD = False
            I "¿Cuál de las frases tiene sentido?"
            menu:
                "un [ProfesionP]":
                    $genero = 'M'
                "una [ProfesionP]":
                    $genero = 'F'
                "ambos":
                    $genero = 'U'
            python:
                p = open('Profesiones.txt','a')
                p.write(" " + ProfesionP + "-" + genero)
                p.close()
            I "¿Deseas añadir una edad a [nombreP]?"
            menu:
                "Sí":
                    $edadP = renpy.input("¿Qué edad tiene [nombreP]?")
                    $edadP = edadP.strip()
                    jump Extra
                "No":
                    jump Extra
        "No":
            I "¿Deseas añadir una edad a [nombreP]?"
            menu:
                "Sí":
                    $edadP = renpy.input("¿Qué edad tiene [nombreP]?")
                    $edadP = edadP.strip()
                    jump Extra
                "No":
                    jump Extra

label Verbo:
    python:
        eD = True
        while(eD):
            verboP = renpy.input("¿Qué acción desea añadir?")
            verboP = verboP.strip()
            aux = 0
            for i in range(0,len(verbo)):
                if verboP.lower() == verbo[i][0].lower():
                    aux = 1
            if aux == 0 and verboP != '':
                eD = False
    $var = 0
    python:
        if verboP.find('ar') == -1 and verboP.find('er') == -1 and verboP.find('ir') == -1:
            var = 1
    if var != 0:
        I "La palabra que escribió no es una acción (Verbo), vuelva a escribirla en infinitivo"
        jump Verbo
    I "¿Cúal de las siguientes frases tiene sentido?"
    menu:
        "[verboP] con el fantasma en Inglaterra":
            $t1 = '1'
        "[verboP] con la espada en Inglaterra":
            $t1 = '2'
        "ambos":
            $t1 = '3'
        "ninguno":
            $t1 = '0'
    menu:
        "[verboP] al fantasma en Inglaterra":
            $t2 = '1'
        "[verboP] a la espada en Inglaterra":
            $t2 = '2'
        "ambos":
            $t2 = '3'
        "ninguno":
            $t2 = '0'
    python:
        pO = verboP[:(len(verboP)-2)] + 'o'
        pC = verboP[:(len(verboP)-3)] + 'ctor'
        pD = verboP[:(len(verboP)-1)] + 'dor'
        pE = verboP[:(len(verboP)-2)] + 'ero'
    I "¿Cúal de las siguientes palabras tienen sentido?"
    menu:
        "[pO]":
            $aP = '1'
        "[pC]":
            $aP = '2'
        "[pD]":
            $aP = '3'
        "[pE]":
            $aP = '4'
        "ninguno":
            $aP = '0'
    python:
        v = open('Verbos.txt','a')
        v.write(" " + verboP + "/" + t1 + "-" + t2 + "," + aP + "," + g + "/")
        v.close()
    jump Extra

label Sujeto:
    python:
        eD = True
        while(eD):
            sujetoU = renpy.input("¿Qué sujeto desea agregar?")
            sujetoU = sujetoU.strip()
            aux = 0
            for i in range(0,len(sujeto)):
                if sujetoU.lower() == sujeto[i][0].lower():
                    aux = 1
            if aux == 0 and sujetoU != '':
                eD = False
    I "¿Es un ser vivo u objeto?"
    menu:
        "Ser vivo":
            $tp = '1'
        "Objeto":
            $tp = '2'
    I "¿Cúal de las siguientes palabras tiene sentido?"
    menu:
        "el [sujetoU]":
            $pre = 'el'
            $pS = 'l'
            $preposicionS = ''
        "la [sujetoU]":
            $pre = 'la'
            $pS = ''
            $preposicionS = 'la'
    menu:
        "[pre] [sujetoU] de la pirata":
            $fP = '1'
            $pS = ''
        "[pre] [sujetoU] de los piratas":
            $fP = '2'
            python:
                if pS == '':
                    pF = 'as'
                    preposicionS = 'las'
                else:
                    pF = 'es'
                    preposicionS = 'los'
        "ambos":
            $fP = '3'
            python:
                import random
                ran = random.randint(1,2)
                fP = str(ran)
                if fP == 2:
                    if sujetoU[(len(sujetoU)-1):] != 'a' and sujetoU[(len(sujetoU)-1):] != 'e' and sujetoU[(len(sujetoU)-1):] != 'i' and sujetoU[(len(sujetoU)-1):] != 'o' and sujetoU[(len(sujetoU)-1):] != 'u':
                        if sujeto[ran][4] == 'la':
                            pF = 'as'
                            preposicionS = 'las'
                        else:
                            pF = 'es'
                            preposicionS = 'los'
                    else:
                        pF = 's'
                else:
                    pF = ''

    python:
        s = open('Sujetos.txt','a')
        s.write(" " + sujetoU + "-" + tp + "-" + fP + "-" + g + "-" + pre + "/")
        s.close()
    jump Extra

label Lugar:
    python:
        eD = True
        while(eD):
            lugarS = renpy.input("¿En qué lugar deseas que transcurra gran parte de la historia?")
            lugarS = lugarS.strip()
            aux = 0
            for i in range(0,len(lugar)):
                if lugarS.lower() == lugar[i][0].lower():
                    aux = 1
            if aux == 0 and lugarS != '':
                eD = False
        fI = renpy.input("¿En que año se fundó [lugarS]?")
        fI = fI.strip() + ' '
        feI = ''
        while fI[0] != ' ' and fI[0] != 'a' and fI[0] != 'd' and fI[0] != 'A' and fI[0] != 'D':
            feI += fI[0]
            fI = fI[1:]
        if fI[0] == ' ':
            fI = fI[1:]
        if fI != '':
            if fI[0] == 'a' or fI[0] == 'A':
                fechaI = -1 * int(feI)
            else:
                fechaI = int(feI)
        else:
            fechaI = int(feI)
    I "¿[lugarS] desaparece o desapareció en algún momento?"
    menu:
        "Sí":
            python:
                fF = renpy.input("¿En qué año desapareció [lugarS]?")
                fF = fF.strip() + ' '
                feF = ''
                while fF[0] != ' ' and fF[0] != 'a' and fF[0] != 'd' and fF[0] != 'A' and fF[0] != 'D':
                    feF += fF[0]
                    fF = fF[1:]
                if fF[0] == ' ':
                    fF = fF[1:]
                if fF != '':
                    if fF[0] == 'a' or fF[0] == 'A':
                        fechaF = -1 * int(feF)
                    else:
                        fechaF = int(feF)
                else:
                    fechaF = int(feF)
        "No":
            $fechaF = 5000
    python:
        l = open('Lugar.txt','a')
        l.write(lugarS + "*" + str(fechaI) + "," + str(fechaF) + "/")
        l.close()
    jump Extra

label Fecha:
    I "¿Deseas añadir algún año específico o un suceso relevante?"
    menu:
        "Año específico":
                $fechaS = renpy.input("¿En qué año deseas que transcurra gran parte de la historia?")
                $fechaS = fechaS.strip()
        "Suceso relevante":
            python:
                eD = True
                while(eD):
                    fechaS = renpy.input("¿Cuál es el suceso?")
                    fechaS = fechaS.strip()
                    aux = 0
                    for i in range(0,len(fecha)):
                        if fechaS.lower() == fecha[i][0].lower():
                            aux = 1
                    if aux == 0 or fechaS == '':
                        eD = False
                fI = renpy.input("¿En qué año inicio?")
                fI = fI.strip() + ' '
                feI = ''
                while fI[0] != ' ' and fI[0] != 'a' and fI[0] != 'd' and fI[0] != 'A' and fI[0] != 'D':
                    feI += fI[0]
                    fI = fI[1:]
                if fI[0] == ' ':
                    fI = fI[1:]
                if fI != '':
                    if fI[0] == 'a' or fI[0] == 'A':
                        fechaI = -1 * int(feI)
                    else:
                        fechaI = int(feI)
                else:
                    fechaI = int(feI)
                fF = renpy.input("¿En qué año finalizó?")
                fF = fF.strip() + ' '
                feF = ''
                while fF[0] != ' ' and fF[0] != 'a' and fF[0] != 'd' and fF[0] != 'A' and fF[0] != 'D':
                    feF += fF[0]
                    fF = fF[1:]
                if fF[0] == ' ':
                    fF = fF[1:]
                if fF != '':
                    if fF[0] == 'a' or fF[0] == 'A':
                        fechaF = -1 * int(feF)
                    else:
                        fechaF = int(feF)
                else:
                        fechaF = int(feF)
                f = open('Fecha.txt','a')
                f.write(fechaS + "*" + str(fechaI) + "," + str(fechaF) + "/")
                f.close()
    jump Extra

label Extra:
    I "¿Deseas añadir algo más?"
    menu:
        "Sí":
             jump Escritura
        "No":
            jump Adicion

label Adicion:
    python:
        import random
        if nombreP == '':
            ran = random.randint(0,(len(nombre)-1))
            nombreP = nombre[ran][0]
            genero = nombre[ran][1]
            vA = ''
            if genero == 'F':
                vA = 'a'
        if ProfesionP == '':
            ran = random.randint(0,(len(Profesion)-1))
            while Profesion[ran][1] != genero and Profesion[ran][1] != 'U':
                ran = random.randint(0,(len(Profesion)-1))
            ProfesionP = Profesion[ran][0]
        if edadP == '':
            ran = random.randint(20,80)
            edadP = str(ran)
        if verboM == '':
            ran = random.randint(0,(len(vM)-1))
            verboM = vM[ran]
        if verboP == '':
            ran = random.randint(0,(len(verbo)-1))
            while g != verbo[ran][4]:
                ran = random.randint(0,(len(verbo)-1))
            verboP = verbo[ran][0]
            t1 = verbo[ran][1]
            t2 = verbo[ran][2]
        if compF == '':
            ran = random.randint(0,1)
            aux = 0
            if t1 != '0' and t2 != '0':
                compF = cM[ran]
                aux = ran + 1
            elif t1 == '0':
                compF = cM[1]
                aux = 2
            else:
                compF = cM[0]
                aux = 1
        if sujetoU == '':
            if aux == 1:
                if t1 == '3':
                    ran = random.randint(1,2)
                    t1 = str(ran)
                ran = random.randint(0,len(sujeto)-1)
                while sujeto[ran][1] != t1 or sujeto[ran][3] != g:
                    ran = random.randint(0,len(sujeto)-1)
                sujetoU = sujeto[ran][0]
                pS = ''
                preposicionS = sujeto[ran][4]
            else:
                if t2 == '3':
                    ran = random.randint(1,2)
                    t2 = str(ran)
                ran = random.randint(0,len(sujeto)-1)
                while sujeto[ran][1] != t2 or sujeto[ran][3] != g:
                    ran = random.randint(0,len(sujeto)-1)
                sujetoU = sujeto[ran][0]
                pS = ''
                preposicionS = ''
                if sujeto[ran][4] == 'el':
                    pS = 'l'
                else:
                    preposicionS = sujeto[ran][4] + ' '
            if sujeto[ran][4] == 'la':
                gen = 'F'
            else:
                gen = 'M'
            fP = sujeto[ran][2]
            if fP == '3':
                ran = random.randint(1,2)
                fP = str(ran)
            if fP == 2:
                if sujetoU[(len(sujetoU)-1):] != 'a' and sujetoU[(len(sujetoU)-1):] != 'e' and sujetoU[(len(sujetoU)-1):] != 'i' and sujetoU[(len(sujetoU)-1):] != 'o' and sujetoU[(len(sujetoU)-1):] != 'u':
                    if sujeto[ran][4] == 'la':
                        pF = 'as'
                    else:
                        pF = 'es'
                else:
                    pF = 's'
            else:
                pF = ''
        if ProfesionS == '':
            ran = random.randint(0,(len(Profesion)-1))
            ProfesionS = Profesion[ran][0]
            gen = Profesion[ran][1]
            pV = ''
            pU = ''
            pA = ''
            preposicionU = ''
            if gen == 'U':
                ran = random.randint(0,1)
                if ran == 0:
                    gen = 'M'
                else:
                    gen = 'F'
            if gen == 'M' and fP == '1':
                pU = 'l'
            else:
                if fP == 1:
                    preposicionU = 'la '
                else:
                    pV = 's'
                    if ProfesionS[(len(ProfesionS)-1):] != 'a' and ProfesionS[(len(ProfesionS)-1):] != 'e' and ProfesionS[(len(ProfesionS)-1):] != 'i' and ProfesionS[(len(ProfesionS)-1):] != 'o' and ProfesionS[(len(ProfesionS)-1):] != 'u':
                        if Profesion[ran][1] == 'F':
                            pA = 'as'
                        else:
                            pA = 'es'
                    else:
                        pA = 's'
                    if gen == 'M':
                        preposicionU = 'los '
                    else:
                        preposicionU = 'las '
        if verboS == '':
            ran = random.randint(0,(len(verbo)-1))
            while verbo[ran][3] == '0':
                ran = random.randint(0,(len(verbo)-1))
            verboS = verbo[ran][0]
            aP = verbo[ran][3]
            if aP == '1':
                if gen == 'M':
                    verboS = verboS[:(len(verboS)-2)] + 'o'
                else:
                    verboS = verboS[:(len(verboS)-2)] + 'a'
            elif aP == '2':
                if gen == 'M':
                    verboS = verboS[:(len(verboS)-2)] + 'ctor'
                    pV = 'es'
                else:
                    verboS = verboS[:(len(verboS)-2)] + 'ctora'
            elif aP == '3':
                if gen == 'M':
                    verboS = verboS[:(len(verboS)-1)] + 'dor'
                    pV = 'es'
                else:
                    verboS = verboS[:(len(verboS)-1)] + 'dora'
            else:
                if gen == 'M':
                    verboS = verboS[:(len(verboS)-2)] + 'ero'
                else:
                    verboS = verboS[:(len(verboS)-2)] + 'era'
        if sujetoD == '':
            ran = random.randint(0,(len(sujeto)-1))
            while sujeto[ran][1] != '2' or sujeto[ran][3] != g:
                ran = random.randint(0,(len(sujeto)-1))
            sujetoD = sujeto[ran][0]
            pD = ''
            preposicionD = ''
            if sujeto[ran][4] == 'el':
                pD = 'l'
            else:
                preposicionD = sujeto[ran][4] + ' '
        if lugarS == '':
            ran = random.randint(0,(len(lugar)-1))
            lugarS = lugar[ran][0]
            fechaI = int(lugar[ran][1])
            fechaF = int(lugar[ran][2])
        if fechaS == '':
            intervalo = abs(fechaI + fechaF)
            fechaR = random.randint(0,intervalo)
            fechaR = fechaR + fechaI
            opc = []
            aux = 0
            for i in range (0,(len(fecha)-1)):
                if fechaR >= int(fecha[i][1]) and fechaR <= int(fecha[i][2]):
                    aux += 1
                    opc.append(fecha[i][0])
            if aux == 0:
                if fechaR < 0:
                    fechaS = str(abs(fechaR)) + ' a.C.'
                else:
                    fechaS = str(fechaR) + ' d.C.'
            else:
                ran = random.randint(0,len(opc))
                if ran == len(opc):
                    if fechaR < 0:
                        fechaS = str(abs(fechaR)) + ' a.C.'
                    else:
                        fechaS = str(fechaR) + ' d.C.'
                else:
                    fechaS = opc[ran]
    "[nombreP], un[vA] [ProfesionP] de [edadP] años [verboM] [verboP] [compF][pS] [preposicionS] [sujetoU] de[pU] [preposicionU][ProfesionS][pA], [verboS][pV] de[pD] [preposicionD][sujetoD] en [lugarS] durante [fechaS]"
    "¿Desea repetir el proceso?"
    menu:
        "Si":
            jump start
        "No":
            return