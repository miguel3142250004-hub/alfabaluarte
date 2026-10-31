CREATE DATABASE IF NOT EXISTS alfabaluarte
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE alfabaluarte;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(120) NOT NULL,
    nombre_usuario VARCHAR(50) NOT NULL,
    correo VARCHAR(150) NOT NULL,
    contrasena_hash VARCHAR(255) NOT NULL,
    rol ENUM('administrador', 'recepcionista', 'especialista') NOT NULL DEFAULT 'recepcionista',
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uq_usuarios_nombre_usuario (nombre_usuario),
    UNIQUE KEY uq_usuarios_correo (correo)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(120) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono VARCHAR(25) NOT NULL,
    correo VARCHAR(150) NULL,
    direccion VARCHAR(255) NULL,
    notas TEXT NULL,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uq_pacientes_correo (correo),
    KEY idx_pacientes_nombre (nombre_completo)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS especialistas (
    id_especialista INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(120) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    cedula_profesional VARCHAR(30) NOT NULL,
    telefono VARCHAR(25) NULL,
    correo VARCHAR(150) NULL,
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uq_especialistas_cedula (cedula_profesional),
    UNIQUE KEY uq_especialistas_correo (correo),
    KEY idx_especialistas_nombre (nombre_completo)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS citas (
    id_cita INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT UNSIGNED NOT NULL,
    id_especialista INT UNSIGNED NOT NULL,
    fecha_cita DATE NOT NULL,
    hora_cita TIME NOT NULL,
    motivo VARCHAR(255) NOT NULL,
    estado ENUM('programada', 'confirmada', 'atendida', 'cancelada') NOT NULL DEFAULT 'programada',
    observaciones TEXT NULL,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_citas_paciente
        FOREIGN KEY (id_paciente) REFERENCES pacientes (id_paciente)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_citas_especialista
        FOREIGN KEY (id_especialista) REFERENCES especialistas (id_especialista)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    UNIQUE KEY uq_citas_especialista_horario (id_especialista, fecha_cita, hora_cita),
    KEY idx_citas_paciente_fecha (id_paciente, fecha_cita),
    KEY idx_citas_agenda (fecha_cita, hora_cita, estado)
) ENGINE = InnoDB;
