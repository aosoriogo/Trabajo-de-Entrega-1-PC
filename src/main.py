import os
import csv

import utilidades as util
import cli

#Configuraciones iniciales
#RUTA_DATASET = "Data\\diabetes_COMPLETO.csv"
RUTA_DATASET = "Data\\diabetes_COMPLETO.csv"
RUTA_HISTORIAL = "resultados\\historial.csv"
DIR_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Variables globales
dataset = []

#Funciones de la logica del programa
def cargar_dataset_completo():
    """
    Permite al usuario seleccionar un dataset entre el original y una busqueda guardada previamente
    y lo carga como una lista de diccionarios
    """
    global dataset
    dataset.clear()

    a = cli.selecionar_dataset()
    if a == 1:
        ruta = os.path.join(DIR_RAIZ, RUTA_DATASET)
    else:
        carpeta = os.path.join(DIR_RAIZ, "resultados")
        print("\n\nLista de archivos guardados: ")
        for j in os.listdir(carpeta):
            print(f"\t{j}")
        
        archivo = input("Digite nombre del archivo sin extension: ")
        if archivo == "historial":
            print("Acceso denegado, elija otro archivo")
            return False
        archivo += ".csv"
        ruta = os.path.join(carpeta, archivo)
        

    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            # DictReader convierte cada fila en un diccionario
            lector = csv.DictReader(archivo)
            for fila in lector:
                for campo in ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]:
                    fila[campo] = float(fila[campo]) if fila[campo] else 0

                fila["Outcome"] = int(fila["Outcome"]) if fila["Outcome"] else 0
                dataset.append(fila)
        
        print(f"Carga exitosa: {len(dataset)} registros.")
        cli.imprimir_dataset(dataset)
        return True
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo en la ruta: {ruta}")
        return []
    except Exception as err:
        print(f"Error carga dataset: {err}")
        return []
    
def buscar():
    '''
        busca un valor en el dataset e imprime todas las columnas que lo contienen junto con la cantidad de veces que se encontro
        permite elegir si buscar coincidencias exactas o cualquier coincidencia
    '''

    global dataset

    #tomar entradas del usuario
    busqueda = []
    print("\nElegiste BUSCAR\n")

    a = input("digite criterio busqueda: ")
    b = input("digite 1 para busqueda exacta y 2 para busqueda extendida: ")
    
    #realizar busquedas y agregar coincidencias a nueva lista
    if b == "1": 
        for linea in dataset:
            for celda in linea.values():
                try:
                    if float(a) == float(celda):
                        busqueda.append(linea)
                        break
                except:
                    print("Fila erronea, pasando a la siguiente")
                    continue
    else:
        for linea2 in dataset:
            w = [str(v) for v in linea2.values()]
            r = " ".join(w)

            if a in r:
                busqueda.append(linea2)

    
    #Imprimir resultados y numero de coincidencias totales
    if len(busqueda) == 0:
        print("\nNo se encontraron coincidencias\n")
        return
    
    print(f"\nSe encontraron {len(busqueda)} resultados\n") 
    cli.imprimir_dataset(busqueda)

    util.guardar_historial(2, a, len(busqueda))
    util.guardar_dataset(busqueda)

def estadisticas_basicas():
    '''imprime el valor maximo, minimo y promedio de la columna seleccionada'''

    global dataset

    maximo = None
    minimo = None
    suma = 0
    contador = 0

    print("\nElegiste ESTADÍSTICAS BÁSICAS\n")

    columna = cli.menu_estadisticas()

    for fila in dataset:
        try:
            valor = float(fila[columna])
        except:
            continue

        if maximo is None or valor > maximo:
            maximo = valor
        if minimo is None or valor < minimo:
            minimo = valor 

        suma += valor 
        contador += 1

    if contador > 0:
        promedio = suma/contador
        print(f"Máximo: {maximo} · Mínimo: {minimo} · Promedio: {round(promedio,1)}")
    else:
        print("No hay datos en la columna")

    util.guardar_historial(3,columna,f"Maximo: {maximo} | media: {promedio} | minimo: {minimo} | {contador}")

    
def filtro():
    '''
        filtra los datos encontrando los valores de una columna mayores al valor 
        que ingrese el usuario.
    '''

    global dataset

    filtro_l = [] #cambie de filtro a filtro_l para evitar colision en la llamada recursiva

    print("\nElegiste FILTRAR POR CONDICIÓN\n")

    x, y = cli.menu_filtro()

    for fila in dataset:
        try:
            if float(fila[x]) >= y:
                filtro_l.append(fila)
        except:
            continue

    filtro_l.sort(key=lambda a: a[x])

    print(f"\nSe filtraron {len(dataset)-len(filtro_l)} resultados\n\n")
    
    cli.imprimir_dataset(filtro_l)

    util.guardar_historial(4, x, f"mayores a {y}: {len(filtro_l)}")

    if len(filtro_l) > 1:
        cli.save_dataset(filtro_l)

def visualizar_historial():

    with open(os.path.join(DIR_RAIZ, RUTA_HISTORIAL), mode='r', encoding='utf-8') as archivo:
        datos = csv.reader(archivo, delimiter=",")
        cli.imprimir_historial(datos)
        return True

#funcion principal
def app():
    while True:
        #verificando que haya un dataset cargado, si no lo hay obliga a cargar uno si lo hay muestra el menu
        if dataset == None or len(dataset)<=1:
            opcion = 1
        else:
            opcion = cli.menu_interactivo()

        #Toma la opcion seleccionada en el menu y corre la funcion correspondien
        match opcion:
            case 1:
                cargar_dataset_completo()
            case 2:
                buscar()
            case 3:
                estadisticas_basicas()
            case 4:
                filtro()
            case 5:
                visualizar_historial()
            case 6:
                print("Elegiste SALIR DEL PROGRAMA")
                break
            case 'e':
                print("Error: Solo se aceptan valores numericos")
            case _:
                print("Opción no válida. Intenta nuevamente.")


if __name__ == '__main__':
    app()