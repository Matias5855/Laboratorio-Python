# MÓDULO: GESTIÓN DE CLIENTES
# Sistema de alquiler de bicicletas

ARCHIVO_CLIENTES = "clientes.txt"

def validar_dni(dni):
    # Función para validar el formato del DNI
    while True:
        if len(dni) == 8 and dni.isdigit():
            return True
        else:
            print("DNI inválido. Debe tener 8 dígitos.")
            print("completar con ceros a la izquierda si es necesario.")
            dni = input("Ingrese su DNI: ")

def validar_nombre(nombre):
    # Función para validar el nombre del cliente
    while True:
        if nombre.replace(" ", "").isalpha():
            return True
        else:
            print("Nombre inválido. Debe contener solo letras.")
            nombre = input("Ingrese su nombre: ")

def validar_email(email):
    # Función para validar el formato del email
    while True:
        if "@" in email and "." in email:
            return True
        else:
            print("Email inválido. Debe contener '@' y '.'")
            email = input("Ingrese su email: ")

def validar_telefono(telefono):
    # Función para validar el formato del número de teléfono
    while True:
        if telefono.isdigit() and len(telefono) >= 7:
            return True
        else:
            print("Número de teléfono inválido. Debe contener solo dígitos y tener al menos 7 dígitos.")
            telefono = input("Ingrese su número de teléfono: ")

def registrar_cliente():
    # Función para registrar un nuevo cliente
    dni = input("Ingrese su DNI: ").strip()
    while not validar_dni(dni):
        dni = input("Ingrese su DNI: ").strip()
    if existe_cliente(dni):
        print("El cliente ya está registrado.")
        return
    nombre = input("Ingrese su nombre: ").strip()
    while not validar_nombre(nombre):
        nombre = input("Ingrese su nombre: ").strip()
    email = input("Ingrese su email: ").strip()
    while not validar_email(email):
        email = input("Ingrese su email: ").strip()
    telefono = input("Ingrese su número de teléfono: ") .strip()
    while not validar_telefono(telefono):
        telefono = input("Ingrese su número de teléfono: ").strip()

    try:
        with open(ARCHIVO_CLIENTES, "a") as archivo:
            archivo.write(dni + ";" + nombre + ";" + email + ";" + telefono + "\n")
        print("Cliente registrado correctamente.")

    except FileNotFoundError:
        print("Error al abrir el archivo.")

def buscar_cliente(dni):
    # Función para buscar un cliente por DNI
    try:
        with open(ARCHIVO_CLIENTES, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                if datos[0] == dni:
                    return {"dni": datos[0],"nombre": datos[1],"email": datos[2],"telefono": datos[3]}

    except FileNotFoundError:
        return None
    return None

def consultar_cliente():
    """
    Consulta un cliente por DNI.
    """
    dni = input("Ingrese DNI del cliente: ").strip()
    cliente = buscar_cliente(dni)
    if cliente is None:
        print("Cliente no encontrado.")
        return
    print("\n===== CLIENTE =====")
    print("DNI:", cliente["dni"])
    print("Nombre:", cliente["nombre"])
    print("Email:", cliente["email"])
    print("Teléfono:", cliente["telefono"])

def mostrar_clientes():
    # Función para mostrar todos los clientes registrados
    try:
        with open(ARCHIVO_CLIENTES, "r") as archivo:
            print("===== CLIENTES =====")
            for linea in archivo:
                datos = linea.strip().split(";")
                print("DNI:", datos[0])
                print("Nombre:", datos[1])
                print("Email:", datos[2])
                print("Teléfono:", datos[3])
                print("---------------------------")

    except FileNotFoundError:
        print("No existen clientes registrados.")

def eliminar_cliente():
    # Función para eliminar un cliente por DNI
    dni = input("Ingrese el DNI del cliente: ").strip()
    lineas = []
    eliminado = False

    try:
        with open(ARCHIVO_CLIENTES, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                if datos[0] == dni:
                    eliminado = True
                else:
                    lineas.append(";".join(datos) + "\n")

        with open(ARCHIVO_CLIENTES, "w") as archivo:
            archivo.writelines(lineas)
        if eliminado:
            print("Cliente eliminado correctamente.")
        else:
            print("No existe un cliente con ese DNI.")
    except FileNotFoundError:
        print("No existen clientes registrados.")
        
def existe_cliente(dni):
    # Función para verificar si un cliente existe por DNI
    cliente = buscar_cliente(dni)
    if cliente is None:
        return False
    return True

#Menu
def menu_clientes():
    while True:
        print("========== GESTIÓN DE CLIENTES ==========")

        print("1. Registrar cliente")
        print("2. Consultar cliente")
        print("3. Mostrar clientes")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            consultar_cliente()
        elif opcion == "3":
            mostrar_clientes()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")