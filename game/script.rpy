label start:
    #Persistencia
    python:
        import os.path
        ##Variables estaticas
        #Personaje
        if os.path.isfile('Nombres.txt') != True:
            n = open('Nombres.txt','w')
            n.write("Jean-M Peter-M Andrea-F Andres-M Robert-M Jackson-M Daniel-M Dunhan-M Victoria-F Eliot-M")
            n.close()
        if os.path.isfile('Profeciones.txt') != True:
            p = open('Profeciones.txt','w')
            p.write("pirata-U oficinista-U hechicera-F estudiante-U soldado-U cantante-U escritor-M astronauta-U futbolista-U periodista-U")
            p.close()
        #Verbo Modal
        vM = ['debe','quiere','tiene que']
        #Lugar
        if os.path.isfile('Lugar.txt') != True:
            l = open('Lugar.txt','w')
            l.write("una misteriosa isla*-5000,5000/una fiesta*-5000,5000/el bosque alado*-5000,0/un campo de concentracion*1939,1945/Polonia*1025,5000/una villa*-5000,5000/Francia*481,5000/los restos de una colonia*-5000,5000/la casa familiar*0,5000/las ruinas de una antigua civilzacion*0,5000/")
            l.close()
        #Fecha
        if os.path.isfile('Fecha.txt') != True:
            f = open('Fecha.txt','w')
            f.write("el medioevo*476,1492/la segunda guerra mundial*1939,1945/la noche de los muertos*1921,5000/la revolucion francesa*1789,1799/")
            f.close()
    #Creación de Sinopsis
    "Elija el tipo de genero que desea"
    menu:
        "Aventura":
            $g = "Aventura"
        "Comedia":
            $g = "Comedia"
        "Fantasia":
            $g = "Fantasia"
        "Terror":
            $g = "Terror"
        "Acción":
            $g = "Acción"
        "Thriller":
            $g = "Thriller"
        "Romance":
            $g = "Romance"
        "Ciencia Ficción":
            $g = "Ciencia Ficción"
        "Drama":
            $g = "Drama"
        "Misterio":
            $g = "Misterio"
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
        #Profecion
        p = open('Profeciones.txt','r')
        pF = p.read()
        p.close()
        profecion = []
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
                profecion.append([pro,gen])
                pF = pF[1:]
            pF = pF[1:]
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
    $profecionP = ''
    $edadP = ''
    $verboM = ''
    $lugarS = ''
    $fechaS = ''
    "¿Desea añadir algun dato adicional?"
    menu:
        "Si":
            jump Escritura
        "No":
            jump Adicion
            
label Escritura:
    "¿Que desea añadir?"
    menu:
        "Personaje":
            jump Personaje
        "Lugar":
            jump Lugar
        "Fecha":
            jump Fecha

label Personaje:
    python:
        nombreP = renpy.input("¿Que nombre desea ponerle al personaje?")
        nombreP = nombreP.strip()
    "¿Es masculino o femenino?"
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
    "¿Desea añadir alguna profeción al personaje?"
    menu:
        "Si":
            python:
                profecionP = renpy.input("¿Que profeción desea ponerle al personaje?")
                profecionP = profecionP.strip()
            "¿Cúal de las siguientes fraces tienen sentido?"
            menu:
                "un [profecionP]":
                    $genero = 'M'
                "una [profecionP]":
                    $genero = 'F'
                "ambos":
                    $genero = 'U'
            python:
                p = open('Profeciones.txt','a')
                p.write(" " + profecionP + "-" + genero)
            "¿Desea añadir una edad al personaje?"
            menu:
                "Si":
                    $edadP = renpy.input("¿Que edad desea ponerle al personaje?")
                    $edadP = edadP.strip()
                    jump Extra
                "No":
                    jump Extra 
        "No":
            "¿Desea añadir una edad al personaje?"
            menu:
                "Si":
                    $edadP = renpy.input("¿Que edad desea ponerle al personaje?")
                    $edadP = edadP.strip()
                    jump Extra
                "No":
                    jump Extra

label Lugar:
    python:
        lugarS = renpy.input("¿En que lugar desea que transcurra gran parte de la historia?")
        lugarS = lugarS.strip()
        fI = renpy.input("¿En que año se fundo [lugarS]?")
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
    "¿[lugarS] desaparece o desaparecio en algun momento?"
    menu:
        "Si":
            python:
                fF = renpy.input("¿En que año desaparecio [lugarS]?")
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
    "¿Desea añadir algun año especifico o un suceso relevante?"
    menu:
        "Año especifico":
            $fechaS = renpy.input("¿En que año desea que transcurra gran parte de la historia?")
            $fechaS = fechaS.strip()
        "Suceso relevante":
            python:
                fechaS = renpy.input("¿Cual es el suceso?")
                fechaS = fechaS.strip()
                fI = renpy.input("¿En que año inicio?")
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
                fF = renpy.input("¿En que año finalizo?")
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
    "¿Desea añadir algo mas?"
    menu:
        "Si":
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
        if profecionP == '':
            ran = random.randint(0,(len(profecion)-1))
            while profecion[ran][1] != genero and profecion[ran][1] != 'U':
                ran = random.randint(0,(len(profecion)-1))
            profecionP = profecion[ran][0]
        if edadP == '':
            ran = random.randint(20,80)
            edadP = str(ran)
        if verboM == '':
            ran = random.randint(0,(len(vM)-1))
            verboM = vM[ran]
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
    "[nombreP], un[vA] [profecionP] de [edadP] años [verboM] *Verbo* *Complemento* en [lugarS] durante [fechaS]"
    "¿Desea repetir el proceso?"
    menu:
        "Si":
            jump start
        "No":
            return