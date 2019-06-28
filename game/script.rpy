label start:
    
    "Que tipo de historia le gustaria leer:"    
    #Reglas
    menu:
        "Aventura":
            $genero = "Aventura"
        "Comedia":
            $genero = "Comedia"
        "Fantasia":
            $genero = "Fantasia"
        "Terror":
            $genero = "Terror"
        "Acción":
            $genero = "Acción"
        "Thriller":
            $genero = "Thriller"
        "Romance":
            $genero = "Romance"
        "Ciencia Ficción":
            $genero = "Ciencia Ficción"
        "Drama":
            $genero = "Drama"
        "Misterio":
            $genero = "Misterio"
    
    python:
        #Librerias
        import random
        
        #Axiomas
        Personaje = [['Aventura' , 'Jean'],['Aventura' , 'Dave'],['Aventura' , 'Phileas'],['Comedia','Peter'],['Comedia','Simon'],['Comedia','Beti'],['Fantasia','Legolas'],['Fantasia','Lucifer'],['Fantasia','Gabriel'],['Terror','Natalia'],['Terror','Jack'],['Terror','Dexter'],['Acción','John'],['Acción','Ms. Smith'],['Acción','James'],['Thriller','Robert'],['Thriller','Ana'],['Thriller','Jeff'],['Romance','Amelia'],['Romance','Juliana'],['Romance','Alejandro'],['Ciencia Ficción','Mark'],['Ciencia Ficción','Marie'],['Ciencia Ficción','Elon'],['Drama','Juan'],['Drama','Christopher'],['Drama','Victoria'],['Misterio','Alice'],['Misterio','Eliot'],['Misterio','Agatha']]
        VerboM = [['Aventura' , 'tiene que'],['Comedia','quiere'],['Fantasia','debe'],['Terror','quiere'],['Acción','debe'],['Thriller','tiene que'],['Romance','quiere'],['Ciencia Ficción','debe'],['Drama','puede'],['Misterio','debe']]
        Verbo = [['Aventura' , 'viajar'],['Aventura' , 'llegar'],['Aventura' , 'partir'],['Comedia','lograr'],['Comedia','demostrar'],['Comedia','fingir'],['Fantasia','salvar'],['Fantasia','encontrar'],['Fantasia','vencer'],['Terror','evadir'],['Terror','exorcizar'],['Terror','matar'],['Acción','vengar'],['Acción','combatir'],['Acción','robar'],['Thriller','sobrevivir'],['Thriller','evadir'],['Thriller','encarar'],['Romance','enamorar'],['Romance','conquistar'],['Romance','compartir'],['Ciencia Ficción','crear'],['Ciencia Ficción','derrocar'],['Ciencia Ficción','destruir'],['Drama','redimir'],['Drama','perdonar'],['Drama','heredar'],['Misterio','descubrir'],['Misterio','resolver'],['Misterio','desenmascarar']]
        Complemento = [['Aventura' , 'con su compañero'],['Aventura' , 'a las ruinas'],['Aventura' , 'al tesoro'],['Comedia','su trabajo'],['Comedia','su madurez'],['Comedia','su experiencia'],['Fantasia','a la princesa'],['Fantasia','sus poderes'],['Fantasia','al villano'],['Terror','un asesino'],['Terror','un espiritu'],['Terror','un demonio'],['Acción','a su familia'],['Acción','su pasado'],['Acción','a la mafia'],['Thriller','al apocalipsis'],['Thriller','a la secta'],['Thriller','a la conspiración'],['Romance','su pareja'],['Romance','su amor'],['Romance','en San Valentin'],['Ciencia Ficción','un imperio'],['Ciencia Ficción','una IA'],['Ciencia Ficción','una realidad'],['Drama','una relación'],['Drama','un pecado'],['Drama','una enfermedad'],['Misterio','un caso'],['Misterio','un homicidio'],['Misterio','un hurto']]
        Lugar = [['Aventura' , 'una isla'],['Comedia','una oficina'],['Fantasia','un bosque'],['Terror','una cabaña'],['Acción','una metropoli'],['Thriller','una catedral'],['Romance','un pueblo'],['Ciencia Ficción','un planeta lejano'],['Drama','una villa'],['Misterio','el Londres']]
        Fecha = [['Aventura' , 'del siglo XV'],['Comedia','de la actualidad'],['Fantasia','del medioevo'],['Terror','de los 70´s'],['Acción','del siglo XX'],['Thriller','de la actualidad'],['Romance','de los 50´s'],['Ciencia Ficción','del futuro'],['Drama','del siglo I'],['Misterio','de los 20´s']]
        
        ##Personaje
        aux = 0
        gen = []
        for i in range (0,len(Personaje)):
            if genero == Personaje[i][0]:
                gen.append(Personaje[i][1])
                aux += 1
        if aux != 0:
            ran = random.randint(0,len(gen)-1)
            pR = gen[ran]            
            
        ##Verbo Modal
        for i in range (0,len(VerboM)):
            if genero == VerboM[i][0]:
                vM = VerboM[i][1]
        
        ##Verbo
        aux = 0
        gen = []
        for i in range (0,len(Verbo)):
            if genero == Verbo[i][0]:
                gen.append(Verbo[i][1])
                aux += 1
        if aux != 0:
            ran = random.randint(0,len(gen)-1)
            vB = gen[ran]
            
        ##Complemento
        aux = 0
        gen = []
        for i in range (0,len(Complemento)):
            if genero == Complemento[i][0]:
                gen.append(Complemento[i][1])
                aux += 1
        if aux != 0:
            ran = random.randint(0,len(gen)-1)
            cP = gen[ran]     
            
        ##Lugar
        for i in range (0,len(Lugar)):
            if genero == Lugar[i][0]:
                lG = Lugar[i][1]
                
        ##Fecha
        for i in range (0,len(Fecha)):
            if genero == Fecha[i][0]:
                fC = Fecha[i][1]
                
    if aux != 0:
        "[pR] [vM] [vB] [cP] en [lG] [fC]"
        menu:
            "Otra sinopsis":
                jump start
            "Terminar":
                return
    else:
        "El genero no se encuentra disponible"