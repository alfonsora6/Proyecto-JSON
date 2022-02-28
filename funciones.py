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
    '''
    print(menu)
    opcion=int(input("Selecciona una opción: "))
    while opcion<1 or opcion>5:
        print("Error, el número de la opción debe estar comprendido entre el 1 y el 5")
        opcion=int(input("Selecciona una opción: "))
    return opcion

#Ejercicio 1
def listar_peliculas(datos):
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