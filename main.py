def cargar_datos(nombre_archivo):
    datos = []
    with open(nombre_archivo, "r") as archivo:
        next(archivo)  
        for linea in archivo:
            fila = linea.strip().split(",")
            datos.append(fila)
    return datos
  
mis_datos = cargar_datos("diabetes_50FILAS.csv")
print(f"Se cargaron {len(mis_datos)} registros con éxito.")
print(mis_datos[0])

def buscar():
    busqueda = []
    a = input("digite criterio busqueda: ")
    b = input("digite 1 para busqueda exacta y 2 para busqueda extendida: ")
    
    if b == "1": 
        for linea in mis_datos:
            for celda in linea:
                if float(a) == float(celda):
                    busqueda.append(linea)
                    break
    else:
        for linea2 in mis_datos:
            r = " ".join(linea2)
            x = r
            if a in x:
                busqueda.append(linea2)

    print(f"Se encontraron {len(busqueda)} resultados")

    for linea in busqueda:
        print(linea)

def estadísticas_basicas():
    print("\n--- ESTADÍSTICAS BÁSICAS ---")
    print("Ingrese un número de acuerdo a la columna que desea analizar:")
    print("0: Embarazos")
    print("1: Glucosa")
    print("2: Presión arterial")
    print("3: Grosor de la piel")
    print("4: Insulina")
    print("5: IMC")
    print("6: Función de pedigrí de diabetes")
    print("7: Edad")
    print("8: Resultado")

    columna=int(input("Elige el número de columna: "))

    maximo = None
    minimo = None
    suma = 0
    contador = 0

    for fila in mis_datos:
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



def flitro():
    filtro = []
    print('Digite el numero de acuerdo a la columna la que desea filtrar: ')
    print("0: Embarazos")
    print("1: Glucosa")
    print("2: Presión arterial")
    print("3: Grosor de la piel")
    print("4: Insulina")
    print("5: IMC")
    print("6: Función de pedigrí de diabetes")
    print("7: Edad")
    print("8: Resultado")
    x = int(input())
    if x in [0, 1, 2, 3, 4,5 ,6 7, 8]
        y = int(input('Digite desde que valor desea filtrar: '))
        for fila in mis_datos:
            if fila[x] > y:
                filtro.append(fila)
    else:
        print('Digite un numero valido')
        filtro()
    filtro.sort(key=lambda a, a[x])
    print(f'Se filtraron {len(mis_datos)-len(filtro)} resultados')
    for linea in filtro:
        print(linea)
            
def menu_interactivo():
    while True:
        print("\n BIENVENIDOS AL MENÚ INTERACTIVO DE INSULINE_LOGIC!")
        print("Ingresa 1 si deseas BUSCAR")
        print("Ingresa 2 si deseas realizar ESTADÍSTICAS BÁSICAS")
        print("Ingresa 3 si deseas FILTRAR POR CONDICIÓN")
        print("Ingresa 4 si deseas SALIR DEL PROGRAMA")
        opcion = int(input("Ingresa una opción (1, 2, 3 o 4): "))
    
        match opcion:
            case 1:
                print("Elegiste BUSCAR")
                buscar()
            case 2:
                print("Elegiste ESTADÍSTICAS BÁSICAS")
                estadísticas_basicas()
            case 3:
                print("Elegiste FILTRAR POR CONDICIÓN")
            case 4:
                print("Elegiste SALIR DEL PROGRAMA")
                break
            case _:
                print("Opción no válida. Intenta nuevamente.")


menu_interactivo()


