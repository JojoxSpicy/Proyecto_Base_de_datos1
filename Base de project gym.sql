Create database Project_Gym;

use Project_Gym;

-- Creación de la tabla Usuarios

CREATE TABLE
    Usuarios (
        ID_Usuario INT PRIMARY KEY AUTO_INCREMENT,
        Nombre VARCHAR(50),
        Apellido VARCHAR(50),
        Fecha_Nacimiento DATE,
        Genero VARCHAR(10),
        Direccion VARCHAR(100),
        Telefono VARCHAR(15),
        Correo_Electronico VARCHAR(100),
        tarjeta varchar(255),
        -- Almacenar la contraseña como un hash
        Contrasena VARCHAR(255) -- Almacenar la contraseña como un hash
    );

-- Creación de la tabla Membresias

CREATE TABLE
    Membresias (
        ID_Membresia INT PRIMARY KEY AUTO_INCREMENT,
        ID_Usuario INT,
        Tipo_Membresia VARCHAR(20),
        Fecha_Inicio DATE,
        Fecha_Vencimiento DATE,
        Estado_Membresia VARCHAR(20),
        Precio DECIMAL(10, 2),
        FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario)
    );

-- Creación de la tabla Asistencia

CREATE TABLE
    Asistencia (
        ID_Asistencia INT PRIMARY KEY AUTO_INCREMENT,
        ID_Usuario INT,
        Fecha DATE,
        Hora_Entrada TIME,
        Hora_Salida TIME,
        FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario)
    );

-- Creación de la tabla Personal

CREATE TABLE
    Personal (
        ID_Personal INT PRIMARY KEY AUTO_INCREMENT,
        Nombre VARCHAR(50),
        Apellido VARCHAR(50),
        Puesto VARCHAR(50),
        Telefono VARCHAR(15),
        Correo_Electronico VARCHAR(100),
        Contrasena VARCHAR(255) -- Almacenar la contraseña como un hash
    );

-- Creacion de la tabla rutinas

CREATE TABLE
    Horario (
        id_usuario INT,
        nombre VARCHAR(100) NOT NULL,
        fecha_creacion DATE NOT NULL,
        nivel_dificultad VARCHAR(55),
        lunes VARCHAR(55) NOT NULL,
        martes VARCHAR(55) NOT NULL,
        miercoles VARCHAR(55) NOT NULL,
        jueves VARCHAR(55) NOT NULL,
        viernes VARCHAR(55) NOT NULL,
        sabado VARCHAR(55) NOT NULL,
        domingo VARCHAR(55) NOT NULL,
        Foreign Key (id_usuario) REFERENCES usuarios(id_usuario)
    );

CREATE TABLE
    Rutinas (
        id_usuario INT,
        nombre VARCHAR(100) NOT NULL,
        descripcion TEXT,
        fecha_creacion DATE NOT NULL,
        nivel_dificultad VARCHAR(55),
        dias_semana ENUM(
            'LUNES',
            'MARTES',
            'MIERCOLES',
            'JUEVES',
            'VIERNES',
            'SABADO',
            'DOMINGO'
        ) NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    );

select * from personal;

DELETE FROM `personal` WHERE `ID_Personal`=2;

