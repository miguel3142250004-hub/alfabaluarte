CREATE SCHEMA IF NOT EXISTS clinica;
SET search_path TO clinica, public;

CREATE TABLE personal (
    id_personal INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    num_empleado VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(80) NOT NULL,
    primer_apellido VARCHAR(60) NOT NULL,
    segundo_apellido VARCHAR(60),
    puesto VARCHAR(30) NOT NULL CHECK (puesto IN ('Administración', 'Recepción', 'Terapeuta', 'Médico', 'Nutriólogo', 'Fisioterapeuta', 'Enfermería', 'Trabajo social')),
    tipo_vinculacion VARCHAR(25) NOT NULL DEFAULT 'Empleado' CHECK (tipo_vinculacion IN ('Empleado', 'Prestador de servicios', 'Colaborador')),
    cedula_profesional VARCHAR(20) UNIQUE,
    especialidad VARCHAR(80),
    estatus BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE usuarios (
    id_usuario INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_personal INT NOT NULL UNIQUE,
    rol VARCHAR(20) NOT NULL CHECK (rol IN ('administracion', 'recepcion', 'profesional')),
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena_hash VARCHAR(100) NOT NULL,
    estatus BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (id_personal) REFERENCES personal(id_personal) ON DELETE CASCADE
);

CREATE TABLE pacientes (
    id_paciente INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    folio VARCHAR(12) NOT NULL UNIQUE,
    nombre VARCHAR(80) NOT NULL,
    primer_apellido VARCHAR(60) NOT NULL,
    segundo_apellido VARCHAR(60) NOT NULL DEFAULT '',
    fecha_nacimiento DATE NOT NULL CHECK (fecha_nacimiento <= CURRENT_DATE),
    sexo CHAR(1) CHECK (sexo IN ('F', 'M', 'O')),
    estatus BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE contactos_pacientes (
    id_contacto INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_paciente INT NOT NULL,
    nombre VARCHAR(120) NOT NULL,
    parentesco VARCHAR(40),
    telefono VARCHAR(10) NOT NULL,
    es_tutor BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente) ON DELETE CASCADE
);

CREATE TABLE consentimientos_pacientes (
    id_consentimiento INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_paciente INT NOT NULL,
    version_aviso VARCHAR(20) NOT NULL,
    fecha_aceptacion DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente) ON DELETE CASCADE
);

CREATE TABLE medios_contacto (
    id_medio INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_paciente INT,
    id_personal INT,
    tipo VARCHAR(10) NOT NULL CHECK (tipo IN ('telefono', 'correo')),
    valor VARCHAR(100) NOT NULL,
    es_principal BOOLEAN NOT NULL DEFAULT FALSE,
    estatus BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente) ON DELETE CASCADE,
    FOREIGN KEY (id_personal) REFERENCES personal(id_personal) ON DELETE CASCADE
);

CREATE TABLE servicios (
    id_servicio INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL UNIQUE,
    duracion_minutos INT NOT NULL CHECK (duracion_minutos > 0),
    estatus BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE personal_servicios (
    id_personal_servicio INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_personal INT NOT NULL,
    id_servicio INT NOT NULL,
    FOREIGN KEY (id_personal) REFERENCES personal(id_personal) ON DELETE CASCADE,
    FOREIGN KEY (id_servicio) REFERENCES servicios(id_servicio) ON DELETE CASCADE
);

CREATE TABLE horarios_personal (
    id_horario INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_personal INT NOT NULL,
    dia_semana INT NOT NULL CHECK (dia_semana BETWEEN 1 AND 7),
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    estatus BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (id_personal) REFERENCES personal(id_personal) ON DELETE CASCADE
);

CREATE TABLE citas (
    id_cita INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    folio VARCHAR(12) NOT NULL UNIQUE,
    id_paciente INT NOT NULL,
    id_personal INT NOT NULL,
    id_servicio INT NOT NULL,
    consultorio VARCHAR(40),
    modalidad VARCHAR(10) NOT NULL DEFAULT 'Presencial',
    fecha DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    estado VARCHAR(15) NOT NULL DEFAULT 'pendiente',
    motivo_cancelacion VARCHAR(200),
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente) ON DELETE RESTRICT,
    FOREIGN KEY (id_personal) REFERENCES personal(id_personal) ON DELETE RESTRICT,
    FOREIGN KEY (id_servicio) REFERENCES servicios(id_servicio) ON DELETE RESTRICT
);

CREATE TABLE antecedentes_pacientes (
    id_antecedente INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_paciente INT NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    descripcion TEXT NOT NULL,
    estatus BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente) ON DELETE CASCADE
);

CREATE TABLE consultas (
    id_consulta INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_cita INT NOT NULL UNIQUE,
    motivo_consulta TEXT NOT NULL,
    diagnostico VARCHAR(300),
    FOREIGN KEY (id_cita) REFERENCES citas(id_cita) ON DELETE CASCADE
);

CREATE TABLE notas_clinicas (
    id_nota INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_consulta INT NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    id_personal INT NOT NULL,
    contenido TEXT NOT NULL,
    estatus BOOLEAN NOT NULL DEFAULT TRUE,
    fecha_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_consulta) REFERENCES consultas(id_consulta) ON DELETE CASCADE,
    FOREIGN KEY (id_personal) REFERENCES personal(id_personal) ON DELETE RESTRICT
);

CREATE TABLE bitacora (
    id_bitacora INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_usuario INT,
    accion VARCHAR(20) NOT NULL,
    tabla VARCHAR(40),
    descripcion VARCHAR(300),
    fecha_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE SET NULL
);

CREATE TABLE respaldos (
    id_respaldo INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tipo VARCHAR(12) NOT NULL,
    archivo VARCHAR(500) NOT NULL,
    exitoso BOOLEAN NOT NULL,
    fecha_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
