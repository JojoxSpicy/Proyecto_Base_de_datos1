import funciones
import os
# Menú principal
while True:

    print("Bienvenido al sistema de inicio de sesión y registro")
    print("1. Ingresar como Usuario")
    print("2. Ingresar como Personal")
    print("3. Registrarse como un Nuevo Usuario")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        os.system('cls')
        resultado = funciones.login_usuario()
    elif opcion == "2":
        os.system('cls')
        resultado = funciones.login_personal()
    elif opcion == "3":
        os.system('cls')
        resultado = funciones.registro_usuario()
    elif opcion == "4":
        os.system('cls')
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
