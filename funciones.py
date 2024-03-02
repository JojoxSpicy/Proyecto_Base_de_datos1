import os
import mysql.connector
import sys
import interfaz
# coneccion con la base de datos
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Siempresemeolvida1",
    database="Project_Gym"
)

cursor = conn.cursor()

# funcion que registra los datos del usuario


def registro_usuario():
    print("Registrarse como Usuario")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de Nacimiento (AAAA-MM-DD): ")
    genero = input("Género(M/F): ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo_electronico = input("Correo Electrónico: ")
    tarjeta = input("Tarjeta: ")
    contrasena = input("Contraseña: ")

    # Insertar los datos en la base de datos
    cursor.execute("INSERT INTO Usuarios (Nombre, Apellido, Fecha_Nacimiento, Genero, Direccion, Telefono, Correo_Electronico, tarjeta, Contrasena) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (nombre, apellido, fecha_nacimiento, genero, direccion, telefono, correo_electronico, tarjeta, contrasena))
    conn.commit()
    # Obtener el ID del último usuario ingresado
    cursor.execute("SELECT LAST_INSERT_ID()")
    last_user_id = cursor.fetchone()[0]
    print("Su Id es el siguiente: ", last_user_id)

    print("Registro exitoso como Usuario")

# funcion que registra al personal


def login_personal():
    print("Ingresar como Personal")
    usuario = input("Nombre de administrador: ")
    contrasena = input("Contraseña: ")
    ID_Personal = input("ID_Personal: ")
    # Comprobar si el usuario y contraseña coinciden en la base de datos
    cursor.execute(
        "SELECT * FROM Personal WHERE Nombre = %s AND Contrasena = %s And ID_Personal = %s", (usuario, contrasena, ID_Personal))
    result = cursor.fetchone()
    if result:
        print("Inicio de sesión exitoso como Personal")
        # Aquí puedes agregar la lógica adicional para el Personal
        resultado = interfaz.interfazdepersonal()
    else:
        print("Credenciales inválidas")
        
# loging usuario


def login_usuario():
    print("Ingresar como Usuario")
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    ID_usuario = input("ID_Usuario: ")

    # Comprobar si el usuario y contraseña coinciden en la base de datos
    cursor.execute(
        "SELECT * FROM Usuarios WHERE Nombre = %s AND Contrasena = %s And ID_usuario= %s", (usuario, contrasena, ID_usuario))
    result = cursor.fetchone()
    if result:
        os.system('cls')
        print("Inicio de sesión exitoso como Usuario")
        # Aquí puedes agregar la lógica adicional para el Usuario
        resultado = interfaz.interfazusuario()
    else:
        print("Credenciales inválidas")


