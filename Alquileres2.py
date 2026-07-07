def mostrar_estadisticas():
    """
    Lee el registro de alquileres y muestra estadísticas de uso por bicicleta.
    """
    print("\n===== ESTADÍSTICAS DE USO DE BICICLETAS =====")
    
    # Diccionario para agrupar los datos. 
    # Formato esperado: {'ID_BICI': {'viajes': 0, 'minutos': 0}}
    estadisticas = {}
    
    try:
        with open(ARCHIVO_ALQUILERES, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                
                # Validamos que la línea tenga los 5 datos esperados
                if len(datos) == 5:
                    id_bici = datos[1]
                    estado = datos[4]
                    
                    # Si es la primera vez que leemos esta bici, la agregamos al diccionario
                    if id_bici not in estadisticas:
                        estadisticas[id_bici] = {"viajes": 0, "minutos": 0}
                    
                    # Sumamos 1 a la cantidad de viajes (esté en curso o finalizado)
                    estadisticas[id_bici]["viajes"] += 1
                    
                    # Si el alquiler ya terminó, calculamos y sumamos los minutos
                    if estado == "Finalizado":
                        hora_inicio = datos[2]
                        hora_fin = datos[3]
                        
                        # Reutilizamos la función que ya creamos antes
                        minutos_uso = calcular_tiempo_uso(hora_inicio, hora_fin)
                        estadisticas[id_bici]["minutos"] += minutos_uso
        
        # Una vez que terminamos de leer el archivo, mostramos los resultados
        if not estadisticas:
            print("Todavía no hay alquileres registrados.")
            return
            
        for id_bici, stats in estadisticas.items():
            print(f"Bicicleta ID: {id_bici}")
            print(f"  - Cantidad de veces alquilada: {stats['viajes']}")
            print(f"  - Tiempo total de uso: {stats['minutos']} minutos")
            print("---------------------------------------------")
            
    except FileNotFoundError:
        print("\nTodavía no hay un archivo de alquileres para analizar.\n")
