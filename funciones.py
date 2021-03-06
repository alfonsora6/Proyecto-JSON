import json
import sys

def leer_json(fichero):
    try:
        with open(fichero) as f:
            datos=json.load(f)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit(0)

def menu():
    menu='''
    1- Listar todas las películas y mostrar su sipnosis.
    2- Mostrar cuantas sesiones tiene cada cine.
    3- Ver el reparto de una película.
    4- Filtrar películas por género.
    5- Mostrar géneros de una película (Se debe especificar el cine).
    6- Salir
    '''
    print(menu)
    opcion=int(input("Selecciona una opción: "))
    while opcion<1 or opcion>6:
        print("Error, el número de la opción debe estar comprendido entre el 1 y el 6")
        opcion=int(input("\nSelecciona una opción: "))
    return opcion

#Ejercicio 1
def listar_peliculas_y_sipnosis(datos):
    peliculas=[]
    sipnosis=[]
    for pelicula,sipno in datos.get("peliculas").items():
        peliculas.append(pelicula)
        sipnosis.append(sipno.get("sipnosis"))
    return peliculas,sipnosis

#Ejercicio 2
def contar_sesiones(datos):
    cines=[]
    sesiones=[]
    for cine,sesion in datos.get("cines").items():
        cines.append(cine)
        sesiones.append(len(sesion.get("sesiones")))
    return cines,sesiones

#Ejercicio 3
def mostrar_peliculas(datos):
    peliculas=[]
    for pelicula in datos.get("peliculas"):
        peliculas.append(pelicula)
    print("\nLista de películas:")
    for pelicula in peliculas:
        print("-",pelicula)


def mostrar_reparto(datos,pelicula):
    reparto=[]
    if pelicula in datos.get("peliculas"):
        for actor in datos.get("peliculas").get(pelicula).get("reparto"):
            reparto.append(actor)
        return reparto
    else:
        print("No hay ninguna película con el nombre indicado.")
        reparto=False
        return reparto
        
#Ejercicio 4
def mostrar_generos(datos):
    lista=[]
    for pelicula in datos.get("peliculas"):
        for genero in datos.get("peliculas").get(pelicula).get("genero"):
            if genero not in lista:
                lista.append(genero)
    return lista

def mostrar_peliculas_por_genero(datos,genero):
    lista=[]
    a=False
    peliculas=list(datos.get("peliculas").keys())

    for pelicula in peliculas:
        if genero in datos.get("peliculas").get(pelicula).get("genero"):
            lista.append(pelicula)
            a=True
    
    if a==False:
        lista=False
        print("No hay ningún género con el nombre indicado.")
    return lista

#Ejercicio 5
def mostrar_cines(datos):
    cines=[]
    for cine in datos.get("cines"):
        cines.append(cine)
    return cines

def mostrar_cartelera(datos):
    try:
        cartelera=[]
        cine=input("\nIntroduce un cine: ")
        for pelicula in datos.get("cines").get(cine).get("peliculas"):
            cartelera.append(pelicula)
        print("\nPelículas disponibles en %s:"%cine)
        for pelicula in cartelera:
            print("-",pelicula)
    except:
        print("Error, cine incorrecto.")
        cartelera=False
        return cartelera

def mostrar_generos_de_una_pelicula(datos):
    try:
        pelicula=input("Introduce una película: ")
        generos=[]
        for genero in datos.get("peliculas").get(pelicula).get("genero"):
            generos.append(genero)
        print("\nGéneros de %s:"%pelicula)
        for genero in generos:
            print("-",genero)
    except:
        print("Error, película incorrecta.")