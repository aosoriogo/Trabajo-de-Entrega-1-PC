# AQUÍ VA LO NUEVO (Entrega 2)
# Lectura con csv.reader y estructuras de datos
import csv

def cargar_dataset_completo(ruta):
    lista_datos = [] 
    
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            # DictReader convierte cada fila en un diccionario
            lector = csv.DictReader(archivo)
            for fila in lector:
                for campo in ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]:
                    fila[campo] = float(fila[campo]) if fila[campo] else 0

                fila["Outcome"] = int(fila["Outcome"]) if fila["Outcome"] else 0
                lista_datos.append(fila)
        
        print(f"Carga exitosa: {len(lista_datos)} registros.")
        return lista_datos

    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo en la ruta: {ruta}")
        return None
