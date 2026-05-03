# AQUÍ VA LO NUEVO (Entrega 2)
# Lectura con csv.reader y estructuras de datos
import csv

def cargar_datos(ruta_archivo):
    """
    Carga el dataset usando csv.DictReader.
    Retorna una LISTA donde cada elemento es un DICCIONARIO (Fila).
    """
    lista_pacientes = []
    
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            # DictReader usa la primera fila como llaves del diccionario automáticamente
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                # Cada 'fila' es un diccionario: {'Pregnancies': '6', 'Glucose': '148', ...}
                lista_pacientes.append(fila)
        
        print(f"Éxito: Se cargaron {len(lista_pacientes)} registros.")
        return lista_pacientes

    except FileNotFoundError:
        print("Error: No se encontró el archivo CSV.")
        return []
