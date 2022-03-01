from funciones import *
fichero=leer_json("cine.json")

respuesta=menu()
while respuesta!=6:
    
    #Ejercicio 1
    if respuesta==1:
        peliculas,sipnosis=listar_peliculas_y_sipnosis(fichero)
        for pelicula,sipno in zip(peliculas,sipnosis):
            print("\n\nNombre de la película:",pelicula,"\n\nSipnosis:",sipno)
    
    #Ejercicio 2
    elif respuesta==2:
        cines,sesiones=contar_sesiones(fichero)
        for cine,sesion in zip(cines,sesiones):
            print("\nCine:",cine,"\nNúmero de sesiones:",sesion)
    
    #Ejercicio 3
    elif respuesta==3:
        peliculas=mostrar_peliculas(fichero)
        pelicula=input("\nIntroduce una película: ")
        reparto=mostrar_reparto(fichero,pelicula)
        if reparto != False:    
            print("\nReparto de %s:\n"%pelicula)
            for actor in reparto:
                print("-",actor)

    #Ejercicio 4
    elif respuesta==4:
        generos=mostrar_generos(fichero)
        print("\nGÉNEROS:")
        for gen in generos:
            print("-",gen)
        print("")
        genero=input("Introduce un género: ")
        peliculas=mostrar_peliculas_por_genero(fichero,genero)
        if peliculas != False:
            print("\nPelículas que pertenecen al género %s:\n"%genero)
            for pelicula in peliculas:
                print("-",pelicula)

    #Ejercicio 5        
    elif respuesta==5:
        cines=mostrar_cines(fichero)
        print("\nLISTADO DE CINES:")
        for cine in cines:
            print("-",cine)
        cartelera=mostrar_cartelera(fichero)
        
        if cartelera!=False:
            genero=mostrar_generos_de_una_pelicula(fichero)
    
    respuesta=menu()

print("Has salido del programa.")