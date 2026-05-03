# AQUÍ VA LO NUEVO (Entrega 2)
# Solo el MENÚ y llamadas a funciones
from logica import cargar_dataset_completo

# Definimos la ruta al archivo de 200+ registros
RUTA_DATASET = "Data/diabetes_COMPLETO.csv"

# Llamamos la función y guardamos el resultado
dataset = cargar_dataset_completo(RUTA_DATASET)

if dataset:
    print(f"Carga exitosa. Registros totales: {len(dataset)}")
else:
    print("Error al cargar el archivo.")

# Funcionalidad 1 
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


