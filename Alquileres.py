# MÓDULO: GESTIÓN DE ALQUILERES
# Archivo: alquileres.py

from datetime import datetime

ARCHIVO_ALQUILERES = "alquileres.txt"
PRECIO_POR_MINUTO = 50  # Se puede ajustar este valor a lo que necesites

def registrar_alquiler():
    """
    Registra el retiro de una bicicleta por parte de un cliente.
    """
    print("\n===== NUEVO ALQUILER =====")
    dni = input("Ingrese el DNI del cliente: ")
    id_bici = input("Ingrese el ID de la bicicleta: ")
    
    # Capturamos la hora actual exacta en formato texto
    hora_inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    estado = "En curso"
    hora_fin = "Pendiente"
    
    # Formato a guardar: DNI;ID_BICI;HORA_INICIO;HORA_FIN;ESTADO
    with open(ARCHIVO_ALQUILERES, "a") as archivo:
        archivo.write(f"{dni};{id_bici};{hora_inicio};{hora_fin};{estado}\n")
        
    print("\nAlquiler registrado exitosamente. Hora de inicio guardada.\n")

def calcular_tiempo_uso(hora_inicio_str, hora_fin_str):
    """
    Calcula la diferencia en minutos entre dos fechas/horas.
    """
    formato = "%d/%m/%Y %H:%M:%S"
    
    try:
        inicio = datetime.strptime(hora_inicio_str, formato)
        fin = datetime.strptime(hora_fin_str, formato)
        
        diferencia = fin - inicio
        minutos_totales = int(diferencia.total_seconds() / 60)
        
        # Si la entrega es súper rápida (menos de 1 min), cobramos 1 min mínimo
        if minutos_totales == 0:
            minutos_totales = 1
            
        return minutos_totales
        
    except ValueError:
        return 0

def calcular_importe(minutos):
    """
    Calcula el total a pagar en base al tiempo de uso.
    """
    return minutos * PRECIO_POR_MINUTO

def devolver_bicicleta():
    """
    Registra la devolución, calcula el tiempo y muestra el importe.
    """
    print("\n===== DEVOLUCIÓN DE BICICLETA =====")
    dni_buscar = input("Ingrese el DNI del cliente que devuelve la bici: ")
    
    lineas = []
    encontrado = False
    
    try:
        with open(ARCHIVO_ALQUILERES, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                
                # Buscamos que coincida el DNI y que el estado sea "En curso"
                # datos = [DNI, ID_BICI, HORA_INICIO, HORA_FIN, ESTADO]
                if datos[0] == dni_buscar and datos[4] == "En curso":
                    
                    hora_inicio = datos[2]
                    # Capturamos la hora actual de devolución
                    hora_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    
                    minutos_uso = calcular_tiempo_uso(hora_inicio, hora_fin)
                    importe_total = calcular_importe(minutos_uso)
                    
                    print("\n--- RESUMEN DE DEVOLUCIÓN ---")
                    print(f"Bicicleta devuelta: {datos[1]}")
                    print(f"Tiempo total de uso: {minutos_uso} minutos.")
                    print(f"IMPORTE A COBRAR: ${importe_total}")
                    print("-----------------------------")
                    
                    # Actualizamos los datos para guardarlos en el txt
                    datos[3] = hora_fin
                    datos[4] = "Finalizado"
                    encontrado = True
                
                # Volvemos a armar la línea separada por punto y coma
                nueva_linea = ";".join(datos) + "\n"
                lineas.append(nueva_linea)
                
        # Si encontramos y modificamos el alquiler, reescribimos el archivo
        if encontrado:
            with open(ARCHIVO_ALQUILERES, "w") as archivo:
                for linea in lineas:
                    archivo.write(linea)
            print("\nDevolución completada y guardada en el registro.\n")
        else:
            print("\nNo se encontró un alquiler 'En curso' para ese DNI.\n")
            
    except FileNotFoundError:
        print("\nTodavía no hay un archivo de alquileres creado. Registre un alquiler primero.\n")
