from menu import mostrar_menu, pedir_opcion


while True:
    mostrar_menu()
    opc = pedir_opcion()
    match opc:
        case 1:
            num = int(input("Digite el limite superior: "))
            
        case 2:
            print("opcion2")
        case 3:
            print("Saliendo...")
            break
        case _:
            print("Error. Elija una opción válida")    