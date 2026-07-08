#Modulo Estadisticas
from alquiler import calcular_tiempo_uso

ARCHIVO_ALQUILERES = "alquileres.txt"

def mostrar_estadisticas():
    """
    Muestra estadísticas de utilización de las bicicletas.
    """
    estadisticas = {}
    try:
        with open(ARCHIVO_ALQUILERES, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                if len(datos) != 5:
                    continue

                codigo = datos[1]

                if codigo not in estadisticas:
                    estadisticas[codigo] = {"alquileres": 0,"horas": 0}

                estadisticas[codigo]["alquileres"] += 1

                if datos[4] == "Finalizado":
                    horas = calcular_tiempo_uso(datos[2],datos[3])
                    estadisticas[codigo]["horas"] += horas

                promedio = 0

                if estadisticas[codigo]["alquileres"] > 0:

                    promedio = (estadisticas[codigo]["horas"] /estadisticas[codigo]["alquileres"])
        
        if len(estadisticas) == 0:
            print("No existen alquileres registrados.")
            return

        print("========== ESTADÍSTICAS ==========")

        for codigo in estadisticas:
            print("Código bicicleta :", codigo)

            print("Cantidad de alquileres :",estadisticas[codigo]["alquileres"])

            print("Horas totales de uso :",round(estadisticas[codigo]["horas"], 2))

            print("Tiempo promedio por alquiler :",round(promedio, 2))
            print("----------------------------------")

    except FileNotFoundError:
        print("No existe el archivo de alquileres.")

#menu
def menu_estadisticas():

    while True:
        print("\n========== ESTADÍSTICAS ==========")
        print("1. Mostrar estadísticas")
        print("2. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_estadisticas()
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")