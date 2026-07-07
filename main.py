from clientes import registrar_cliente, mostrar_clientes, eliminar_cliente

clientes = []

while True:
    print("\n---Menú Clientes---")
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Eliminar cliente")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente(clientes)
    elif opcion == "2":
        mostrar_clientes(clientes)
    elif opcion == "3":
        # Pedimos el DNI en el menú y llamamos a tu función original
        dni_buscar = input("Ingrese el DNI del cliente a eliminar: ")
        eliminar_cliente(clientes, dni_buscar)
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
