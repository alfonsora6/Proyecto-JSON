from funciones import *
fichero=leer_json("cine.json")

respuesta=menu()
while respuesta!=5:
    
    #Ejercicio 1
    if respuesta==1:
        peliculas,sipnosis=listar_peliculas(fichero)
        for pelicula,sipno in zip(peliculas,sipnosis):
            print("\n\nNombre de la película:",pelicula,"\n\nSipnosis:",sipno)
    
    #Ejercicio 2
    elif respuesta==2:
        cines,sesiones=contar_sesiones(fichero)
        for cine,sesion in zip(cines,sesiones):
            print("\nCine:",cine,"\nNúmero de sesiones:",sesion)
    #elif respuesta==3:
    #elif respuesta==4:
    #elif respuesta==5:

    respuesta=menu()
    