print("Bienvenidos al sistema")
clientes={}
while True:
    print("Menú")
    print("1.Registrar clientes")
    print("2.Mostrar clientes")
    print("3.Buscar clientes")
    print("4.Actualizar clientes")
    print("5.Eliminar clientes")
    print("6.Salir")
    opcion=str(input("Elija una opción: "))
    if opcion=="1":
        RUC = str(input("Ingrese el RUC de la empresa: "))
        empresa = str(input("Ingrese el nombre de la empresa: "))
        clientes[RUC]=empresa
    elif opcion=="2":
        print(clientes)
    elif opcion=="3":
        busqueda=str(input("Ingrese la RUC del cliente que esta buscando: "))
        print("Resultado: ",clientes.get(busqueda, "No se ha encontrado el cliente"))
    elif opcion=="4":
        name=input("Ingrese la RUC del cliente a modificar: ")
        newname=input("Ingrese el nuevo nombre del cliente")
        clientes[name]=newname
    elif opcion=="5":
        eliminar=str(input("Ingrese la RUC del cliente que desea eliminar: "))
        del clientes[eliminar]
    elif opcion=="6":
        print("Usted acaba de salir")
        break
