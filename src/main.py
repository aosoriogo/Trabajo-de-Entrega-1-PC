# AQUÍ VA LO NUEVO (Entrega 2)
# Solo el MENÚ y llamadas a funciones
from logica import cargar_dataset_completo

# Definimos la ruta al archivo de 200+ registros
RUTA_DATASET = "Data/diabetes_COMPLETO.csv"

# MENÚ INTERACTIVO
def mostrar_menu():
    print("\n--- ¡BIENVENIDOS AL MENÚ INTERACTIVO DE INSULINE LOGIC! ---")
    print("1. Ver cantidad de datos")
    print("2. Filtrar pacientes en riesgo")
    print("3. Guardar resultados filtrados")
    print("4. Cargar resultados guardados")
    print("5. Ver historial")
    print("6. Funcionalidad opcional")
    print("7. Salir")

def menu_interactivo(dataset):
    if not dataset:
        print("No hay dataset cargado.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print(f"Total de registros: {len(dataset)}")
            guardar_historial(opcion, 1)
        elif opcion == "2":
            resultados = filtrar_pacientes(dataset)
            print(f"Se encontraron {len(resultados)} pacientes en riesgo")
            for r in resultados:
                print(r)
            guardar_historial(opcion, resultados)
        elif opcion == "3":
            resultados = filtrar_pacientes(dataset)
            ruta = input("Ingrese nombre del archivo (ej: resultados.csv o resultados.json): ")
            guardar_resultados(resultados, ruta)
            print("Resultados guardados correctamente")
            guardar_historial(opcion, resultados)
        elif opcion == "4":
            ruta = input("Ingrese ruta del archivo a cargar: ")
            datos_cargados = cargar_resultados(ruta)

            if datos_cargados:
                print(f"Se cargaron {len(datos_cargados)} registros:")
                for d in datos_cargados:
                    print(d)
                guardar_historial(opcion, datos_cargados)
            else:
                print("No se pudieron cargar los datos")
        elif opcion == "5":
            # Historial
            historial = visualizar_hisorial()
            print('Historial de consultas')
            h = 0
            for fila in historial:
                if fila == []:
                    continue
                else:
                    print(fila)
                    h += 1
            guardar_historial(opcion, h)
        elif opcion == "6":
            # Funcionalidad opcional
            print("Funcionalidad opcional no implementada aún")
            guardar_historial(opcion, 0)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo")

# FUNCIONALIDAD 1 
import json 
import csv
# Filtro de datos
def filtrar_pacientes(datos):
    return [d for d in datos if d["Glucose"]>125 or d["BMI"]>30 ]
#Guardar resultados
def guardar_resultados(datos, ruta):
    if not datos:
        print("No hay datos")
        return
    if ruta.endswith(".csv"):
        claves = datos[0].keys()
        with open(ruta, "w", newline="", encoding="utf-8" ) as archivo:
            writer = csv.DictWriter(archivo, fieldnames=claves)
            writer.writeheader()
            writer.writerows(datos)
    elif ruta.endswith(".json"):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)
#Cargar resultados 
def cargar_resultados(ruta):
    if ruta.endswith(".csv"):
        return cargar_dataset_completo(ruta)
    elif ruta.endswith(".json"):
        with open(ruta, encoding='utf-8') as archivo:
            return json.load(archivo)

# FUNCIONALIDAD 2
#Visualizar el historial
def visualizar_hisorial():
    with open("resultados/historial.csv", mode='r', encoding='utf-8') as archivo:
        datos = csv.reader(archivo, delimiter=",")
        return list(datos)
#Guardar historial
import datetime as dt
import csv
def guardar_historial(opcion, resultado):
    with open("resultados/historial.csv", mode='a', encoding='utf-8') as hist:
        if opcion == '1':
            t = 'Visualizar datos'
            res = resultado
        elif opcion == '2':
            t = 'Pacientes en riezgo'
            res = len(resultado)
        elif opcion == '3':
            t = 'Guardar filtro'
            res = len(resultado)
        elif opcion == '4':
            t = 'Cargar resultados'
            res = len(resultado)
        elif opcion == '5':
            t = 'Visualizar historial'
            res = resultado
        elif opcion == '6':
            t = 'Funcionalidad opcional'
            res = resultado
        r = str(res) + ' resultados'
        guardar = csv.writer(hist, delimiter=",")
        guardar.writerow([dt.datetime.now().strftime("%Y-%m-%d %H:%M"), t, r])
#FUNCIONALIDAD OPCIONAL



# EJECUCIÓN
# Llamemos a la función y guardemos el resultado
dataset = cargar_dataset_completo(RUTA_DATASET)

if dataset:
    print(f"Carga exitosa. Registros totales: {len(dataset)}")
else:
    print("Error al cargar el archivo.")

menu_interactivo(dataset)

