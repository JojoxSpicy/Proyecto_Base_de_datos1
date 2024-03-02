# crear un while que pregunte que quieres hacer entre crear rutina,visualizarla o salir

import funciones
import os
import sys
from pymongo import MongoClient
import mysql.connector

# coneccion con la base de datos
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Siempresemeolvida1",
    database="Project_Gym"
)

cursor = conn.cursor()

cursor = conn.cursor(dictionary=True)

def interfazdepersonal():
    while True:
        os.system("cls")
        print("Bienvenido a la interfaz del Personal")
        print("1. Ver informacion sobre algun usuario")
        print("2. eliminar un usuario")
        print("3. salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system('cls')
            ver_info_personal()
            input("Presione Enter para continuar...")

        elif opcion == "2":
            os.system('cls')
            eliminar_usuario()
            input("Presione Enter para continuar...")
        elif opcion == "3":
            os.system('cls')
            print("saliendo del programa")
            print("\U0001F47A")
            sys.exit(0)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")




def ver_info_personal():
    print("Ver Información de un Usuario")

    # pregunta al personal si desea volver atras sin ver informacion
    opcion_volver_atras = input("¿Desea volver atrás sin ver la info de ningun usuario? (si/no): ").lower()

    if opcion_volver_atras == "si":
        print("Operación cancelada. No se ha consultado ninguna informacion.")
        return

    try:
        
        # Pedir al personal ingresar el ID del usuario
        id_usuario = int(input("Ingrese el ID del Usuario que desea consultar: "))

        # Consultar la base de datos para obtener la información del usuario
        query = """
        SELECT u.ID_Usuario, u.Nombre, u.Apellido, u.Fecha_Nacimiento,
               u.Genero, u.Direccion, u.Telefono, u.Correo_Electronico
        FROM Usuarios u
        JOIN Personal p ON u.ID_Usuario = p.ID_Personal
        WHERE u.ID_Usuario = %s
        """

        cursor.execute(query, (id_usuario,))
        usuario_info = cursor.fetchone()

        if usuario_info:
            print("\nInformación del Usuario:")
            print(f"ID Usuario: {usuario_info['ID_Usuario']}")
            print(f"Nombre: {usuario_info['Nombre']}")
            print(f"Apellido: {usuario_info['Apellido']}")
            print(f"Teléfono: {usuario_info['Telefono']}")
            print(f"Correo Electrónico: {usuario_info['Correo_Electronico']}")
        else:
            print("No se encontró información para el ID de usuario proporcionado.")
    except ValueError:
        # Capturar cualquier excepción y mostrar información sobre la excepción
        print("Error: El ID de usuario debe ser un número entero.")
        return



def eliminar_usuario():
    print("Eliminar Usuario")

    # Pedir al personal ingresar el ID del usuario a eliminar
    id_usuario_a_eliminar = input("Ingrese el ID del Usuario que desea eliminar: ")

    try:
        # Convertir el ID a entero y realizar la eliminación en la base de datos
        id_usuario_a_eliminar = int(id_usuario_a_eliminar)

        # Verificar si el usuario existe antes de eliminarlo
        cursor.execute("SELECT * FROM Usuarios WHERE ID_Usuario = %s", (id_usuario_a_eliminar,))
        usuario_existente = cursor.fetchone()

        if usuario_existente:
            # Confirmar la eliminación con el personal
            confirmacion = input(f"¡Advertencia! Esta acción eliminará al usuario con ID {id_usuario_a_eliminar} y sus horarios asociados. ¿Está seguro? (si/no): ").lower()

            if confirmacion == "si":
                # Eliminar al usuario de la base de datos relacional
                cursor.execute("DELETE FROM Usuarios WHERE ID_Usuario = %s", (id_usuario_a_eliminar,))
                conn.commit()
                print(f"Usuario con ID {id_usuario_a_eliminar} eliminado correctamente.")

                # Eliminar horarios asociados en MongoDB
                mongo_collection_horarios.delete_many({"id_usuario": id_usuario_a_eliminar})
                print(f"Horarios asociados al usuario con ID {id_usuario_a_eliminar} eliminados en MongoDB.")
            else:
                print("Operación cancelada. No se ha eliminado ningún usuario.")
        else:
            print("No existe un usuario con el ID proporcionado.")

    except ValueError:
        print("Error: El ID de usuario debe ser un número entero.")




















# Conexión a la base de datos NoSQL (MongoDB)
            
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["Project_GYM"]
mongo_collection_horarios = mongo_db["Horarios"]

def interfazusuario():
    while True:
        os.system("cls")
        print("Bienvenido a la interfaz del usuario")
        print("1. Crear Horario de Ejercicios")
        print("2. Ver tu Horario")
        print("3. salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system('cls')
            crear_horario_usuario()

        elif opcion == "2":
            os.system('cls')
            ver_horarios_usuario()
            
        elif opcion == "3":
            os.system('cls')
            print("saliendo del programa, AHORA AL GYM COMO UN TORO ")
            print("\U0001F47A")
            sys.exit(0)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def crear_horario_usuario():
    print("Crear Horario de Ejercicios")

    # Preguntar al usuario si desea volver atrás inmediatamente
    while True:
        opcion_volver_atras_inmediatamente = input("¿Desea volver atrás sin ingresar detalles del horario? (si/no): ").lower()

        if opcion_volver_atras_inmediatamente == "si":
            print("Operación cancelada. No se ha creado ningún horario.")
            return
        elif opcion_volver_atras_inmediatamente == "no":
            os.system("cls")
            break
        else:
            print("Por favor, seleccione una de las opciones válidas ('si' o 'no').")

    id_usuario = input("Ingrese su ID de Usuario: ")
    nombre_horario = input("Ingrese el nombre de su horario: ")

    # Consulta MongoDB para verificar si ya existe un horario con el mismo nombre
    existing_horario = mongo_collection_horarios.find_one({"id_usuario": int(id_usuario), "nombre": nombre_horario})

    if existing_horario:
        print(f"Ya existe un horario con el nombre '{nombre_horario}' para este usuario. No se puede crear otro.")
    else:
        fecha_creacion = input("Ingrese la fecha de creación (AAAA-MM-DD): ")
        nivel_dificultad = input("Ingrese el nivel de dificultad: ")
        lunes = input("Ingrese las actividades para el lunes: ")
        martes = input("Ingrese las actividades para el martes: ")
        miercoles = input("Ingrese las actividades para el miercoles: ")
        Jueves = input("Ingrese las actividades para el jueves: ")
        Viernes = input("Ingrese las actividades para el viernes: ")

        # Registro del horario en MongoDB
        horario = {
            "id_usuario": int(id_usuario),
            "nombre": nombre_horario,
            "fecha_creacion": fecha_creacion,
            "nivel_dificultad": nivel_dificultad,
            "lunes": lunes,
            "martes": martes,
            "Miercoles": miercoles,
            "Jueves": Jueves,
            "Viernes": Viernes
        }

        # Preguntar si el usuario quiere volver atrás antes de insertar el horario
        while True:
            opcion_volver_atras = input("¿Desea volver atrás sin guardar el horario? (si/no): ").lower()

            if opcion_volver_atras == "si":
                print("Operación cancelada. No se ha creado ningún horario.")
                return
            elif opcion_volver_atras == "no":
                print("Horario creado y guardado exitosamente en MongoDB")
                break
            else:
                print("Por favor, seleccione una de las opciones válidas ('si' o 'no').")

        mongo_collection_horarios.insert_one(horario)




def ver_horarios_usuario():
    print("Ver tus Horarios")

    # Preguntar al usuario si desea volver atrás antes de ingresar el ID
    opcion_volver_atras = input("¿Desea volver atrás sin consultar los horarios? (si/no): ").lower()

    if opcion_volver_atras == "si":
        print("Operación cancelada. No se ha consultado ningún horario.")
        return

    id_usuario = input("Ingrese su ID de Usuario: ")

    # Convertir id_usuario a entero
    id_usuario = int(id_usuario)

    # Consulta MongoDB para obtener horarios del usuario
    count_horarios = mongo_collection_horarios.count_documents({"id_usuario": id_usuario})

    if count_horarios > 0:
        print("Horarios del Usuario:")
        horarios_usuario = mongo_collection_horarios.find({"id_usuario": id_usuario})
        for horario in horarios_usuario:
            print(f"Nombre: {horario['nombre']}")
            print(f"Fecha de Creación: {horario['fecha_creacion']}")
            print(f"Nivel de Dificultad: {horario['nivel_dificultad']}")
            print(f"Lunes: {horario['lunes']}")
            print(f"Martes: {horario['martes']}")
            print(f"Miercoles: {horario['Miercoles']}")
            print(f"Jueves: {horario['Jueves']}")
            print(f"Viernes: {horario['Viernes']}")
            print("------------------------")

        # Mensaje para presionar Enter antes de finalizar
        input("Presione Enter para finalizar y volver atrás.")
    else:
        print("No se encontraron horarios para el usuario.")


       









