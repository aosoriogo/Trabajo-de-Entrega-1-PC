
# Aqui se almacenan las funciones que se reusan pero no hacen parte directa de la logica
import datetime as dt
import csv
import os

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def guardar_historial(opcion: int, valor, resultados):
    """
    Correcciones realizadas:
        se movio la funcion de main.py a utilidades.py
        se cambio el if-elif-else por un match->case (No es recomendable usar if en cadenas de mas de 3 opciones)
        se agrego un caso por defecto al match->case que levanta un error indicando que no existe ese caso
        se movio la apertura del archivo hasta despues del match->case (El archivo debe abrirse y cerrarce en el menor numero de operaciones posibles)
    """
    
    match opcion:
        case 1:
            t = 'Cargar dataset'
        case 2:
            t = 'Buscar coincidencia'
        case 3:
            t = 'Estadisticas basicas'
        case 4:
            t = 'Filtrar por'
        case '2':
            t = 'Pacientes en riesgo'
        case '3':
            t = 'Guardar filtro'
        case '4':
            t = 'Cargar resultados'
        case '5':
            t = 'Visualizar historial'
        case '6':
            t = 'Funcionalidad opcional'
        case _:
            raise ValueError("Opcion no definida")
    

    resultados = str(resultados) + " resultados"
    
    cadena = [dt.datetime.now().strftime("%Y-%m-%d %H:%M"), t, valor, resultados]

    with open(os.path.join(DIR, "resultados/historial.csv"), mode='a', encoding='utf-8') as hist:

        guardar = csv.writer(hist, delimiter=",")
        guardar.writerow(cadena)

def guardar_dataset(datos):
    while True:
        archivo = input("Digite el nombre del archivo a guardar sin extension: ")
        if "." in archivo:
            print("No utilice puntos ni caracteres especiales")
            continue
        else:
            archivo += ".csv"
            ruta = os.path.join(DIR, f"resultados\\{archivo}")
            with open(ruta, mode='w', newline='', encoding='utf-8') as busqueda:
                headers = list(datos[0].keys())
                #print(headers) #Linea de prueba
                wr = csv.DictWriter(busqueda, headers, delimiter=",")
                wr.writeheader()
                wr.writerows(datos)
                return True
        return False

def guardar_stadisticas_dataset():
    pass
        