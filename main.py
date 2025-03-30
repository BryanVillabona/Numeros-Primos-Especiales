from menu import mostrar_menu, pedir_opcion
from numeros import *


while True:
    mostrar_menu()
    opc = pedir_opcion()
    match opc:
        case 1:
            limite = int(input("Digite un rango a calcular: "))
            encontrar_primos_gemelos(limite)
        case 2:
            limite = int(input("Digite un rango a calcular: "))
            encontrar_primos_palindromicos(limite)
        case 3:
            print("Saliendo...")
            break
        case _:
            print("Error. Elija una opción válida")  
