#Gestion de Alquileres

from datetime import datetime
from clientes import buscar_cliente
from bicicletas import buscar_bicicleta
from bicicletas import cambiar_estado

ARCHIVO_ALQUILERES = "alquileres.txt"
TARIFA_HORA = 3000  # Tarifa por hora de alquiler

def registrar_alquiler():
    dni = input("Ingrese DNI del cliente: ")
    cliente = buscar_cliente(dni)
    if cliente is None:
        print("Cliente no encontrado. Debe registrarse primero.")
        return
    
    codigo = input("Ingrese código de la bicicleta: ")
    bicicleta = buscar_bicicleta(codigo)
    if bicicleta is None:
        print("Bicicleta no encontrada.")
        return
    
    if bicicleta["estado"] != "Disponible":
        print("La bicicleta no está disponible para alquiler.")
        return
    
    if existe_alquiler_activo(codigo):
        print("La bicicleta ya posee un alquiler activo.")
        return
    
    fecha_inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(ARCHIVO_ALQUILERES, "a") as archivo:
        archivo.write(f"{dni};{codigo};{fecha_inicio};-;Activo\n")
        
    cambiar_estado(codigo, "Alquilada")
    print("Alquiler registrado exitosamente.")

def buscar_alquiler_activo(codigo):
    """
    Busca un alquiler activo por código de bicicleta.
    """
    try:
        with open(ARCHIVO_ALQUILERES, "r") as archivo:
            for linea in archivo:
                # Si hay una línea vacía, la salta
                if not linea.strip():
                    continue
                
                # Esto limpia los espacios invisibles de cada dato enviado por tu compañero
                datos = [d.strip() for d in linea.split(";")]
                
                # Validamos que la línea tenga las 5 partes y que esté Activo
                if len(datos) >= 5 and datos[1] == codigo and datos[4] == "Activo":
                    alquiler = {
                        "dni": datos[0],
                        "codigo": datos[1],
                        "fecha_inicio": datos[2],
                        "fecha_fin": datos[3],
                        "estado": datos[4]
                    }
                    return alquiler
    except FileNotFoundError:
        print("No hay registros de alquileres.")
    return None

def existe_alquiler_activo(codigo):
    """
    Verifica si una bicicleta posee un alquiler activo.
    """
    alquiler = buscar_alquiler_activo(codigo)

    if alquiler is None:
        return False
    return True

def calcular_tiempo_uso(fecha_inicio, fecha_fin):

    formato = "%d/%m/%Y %H:%M:%S"

    try:

        inicio = datetime.strptime(fecha_inicio, formato)
        fin = datetime.strptime(fecha_fin, formato)
        diferencia = fin - inicio
        horas = diferencia.total_seconds() / 3600

        if horas < 1:
            horas = 1
        return horas

    except ValueError:
        return 0

def calcular_importe(horas):
    """Calcula el importe a pagar según las horas de uso."""
    return horas * TARIFA_HORA

def registrar_devolucion():
    """
    Registra la devolución de una bicicleta.
    """
    codigo = input("Ingrese código de la bicicleta: ")
    alquiler = buscar_alquiler_activo(codigo)

    if alquiler is None:
        print("No existe un alquiler activo para esa bicicleta.")
        return

    fecha_fin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    horas = calcular_tiempo_uso(alquiler["fecha_inicio"], fecha_fin)
    importe = calcular_importe(horas)
    cambiar_estado(codigo, "Disponible")
    actualizar_alquiler(codigo, fecha_fin)

    print("===== DEVOLUCIÓN =====")
    print("codigo de bicicleta:", codigo)
    print("Tiempo de uso:", round(horas, 2), "horas")
    print("Importe: $", round(importe, 2))
    print("Devolución registrada correctamente.")

def actualizar_alquiler(codigo, fecha_fin):
    lineas = []
    with open(ARCHIVO_ALQUILERES, "r") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue
                
            
            datos = [d.strip() for d in linea.split(";")]

            if len(datos) >= 5 and datos[1] == codigo and datos[4] == "Activo":
                datos[3] = fecha_fin
                datos[4] = "Finalizado"

            lineas.append(";".join(datos) + "\n")

    with open(ARCHIVO_ALQUILERES, "w") as archivo:
        archivo.writelines(lineas)

def mostrar_alquileres():
    """
    Muestra todos los alquileres registrados.
    """
    try:
        with open(ARCHIVO_ALQUILERES, "r") as archivo:
            print("======= ALQUILERES =======")
            hay_alquileres = False
            for linea in archivo:
                # 1. Ignoramos líneas vacías limpiándolas primero con .strip()
                if not linea.strip():
                    continue
                
                # 2. Primero aplicamos .strip() a la línea entera para eliminar el "\n" del final, y luego hacemos el split
                datos = [d.strip() for d in linea.strip().split(";")]
                
                # 3. Control de seguridad
                if len(datos) < 5:
                    continue

                hay_alquileres = True
                print("DNI       :", datos[0])
                print("Bicicleta :", datos[1])
                print("Inicio    :", datos[2])
                print("Fin       :", datos[3])
                print("Estado    :", datos[4])
                print("------------------------------")
            
            if not hay_alquileres:
                print("No hay alquileres válidos registrados para mostrar.")

    except FileNotFoundError:
        print("No existen alquileres registrados.")

#Menu
def menu_alquiler():
    while True:
        print("========== GESTIÓN DE ALQUILERES ==========")
        print("1. Registrar alquiler")
        print("2. Registrar devolución")
        print("3. Mostrar alquileres")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_alquiler()
        elif opcion == "2":
            registrar_devolucion()
        elif opcion == "3":
            mostrar_alquileres()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")