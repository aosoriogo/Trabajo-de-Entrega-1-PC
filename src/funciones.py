# Aqui se almacenan las funciones que se reusan pero no hacen parte directa de la logica
import datetime as dt
import csv
import os

def mostrar_menu():
    """
    Correcciones:
        se movio la funcion de main.py a funciones.py
        se realiza la lectura de la respuesta desde esta funcion
    """
    print("\n--- ¡BIENVENIDOS AL MENÚ INTERACTIVO DE INSULINE LOGIC! ---")
    print("1. Ver cantidad de datos")
    print("2. Filtrar pacientes en riesgo")
    print("3. Guardar resultados filtrados")
    print("4. Cargar resultados guardados")
    print("5. Ver historial")
    print("6. Funcionalidad opcional")
    print("7. Salir")
    return input("Seleccione una opción: ")

def logger():
    pass

def guardar_historial(opcion, resultado):
    """
    Correcciones realizadas:
        se movio la funcion de main.py a funciones.py
        se cambio el if-elif-else por un match->case (No es recomendable usar if en cadenas de mas de 3 opciones)
        se agrego un caso por defecto al match->case que levanta un error indicando que no existe ese caso
        se movio la apertura del archivo hasta despues del match->case (El archivo debe abrirse y cerrarce en el menor numero de operaciones posibles)
    """
    match opcion:
        case 'a':
            t = 'Buscar dato'
            res = resultado
        case '1':
            t = 'Visualizar datos'
            res = resultado
        case '2':
            t = 'Pacientes en riesgo'
            res = len(resultado)
        case '3':
            t = 'Guardar filtro'
            res = len(resultado)
        case '4':
            t = 'Cargar resultados'
            res = len(resultado)
        case '5':
            t = 'Visualizar historial'
            res = resultado
        case '6':
            t = 'Funcionalidad opcional'
            res = resultado
        case _:
            raise ValueError("Opcion no definida")
        
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(dir, "resultados/historial.csv"), mode='a', encoding='utf-8') as hist:
        r = str(res) + ' resultados'
        guardar = csv.writer(hist, delimiter=",")
        guardar.writerow([dt.datetime.now().strftime("%Y-%m-%d %H:%M"), t, r])


