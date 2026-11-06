SET search_path TO clinica, public;

INSERT INTO servicios (nombre, duracion_minutos) VALUES
('Primera consulta de psicología', 60), ('Sesión individual de psicología', 50),
('Terapia de pareja', 60), ('Consulta de medicina general', 30),
('Consulta de nutrición', 45), ('Sesión de fisioterapia', 45),
('Psiquiatría', 50), ('Terapia familiar', 60),
('Evaluación psicométrica', 90), ('Consulta de seguimiento', 30);

INSERT INTO personal (num_empleado, nombre, primer_apellido, puesto, cedula_profesional, especialidad) VALUES
('EMP-001', 'Marcela', 'Ibarra', 'Administración', NULL, NULL),
('EMP-002', 'Laura', 'Quintero', 'Recepción', NULL, NULL),
('EMP-003', 'Andrés', 'Villa', 'Terapeuta', 'CED-003', 'Psicología clínica'),
('EMP-004', 'Sofía', 'Barraza', 'Terapeuta', 'CED-004', 'Psicología infantil'),
('EMP-005', 'Diego', 'Cuevas', 'Terapeuta', 'CED-005', 'Terapia de pareja'),
('EMP-006', 'Patricia', 'Herrera', 'Médico', 'CED-006', 'Medicina general'),
('EMP-007', 'Ricardo', 'Salas', 'Nutriólogo', 'CED-007', 'Nutrición clínica'),
('EMP-008', 'Elena', 'Rangel', 'Trabajo social', NULL, NULL),
('EMP-009', 'Mario', 'Gomez', 'Fisioterapeuta', 'CED-009', 'Rehabilitación'),
('EMP-010', 'Carla', 'Diaz', 'Enfermería', 'CED-010', 'Enfermera general');

INSERT INTO pacientes (folio, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, sexo) VALUES
('PAC-000001', 'Ana', 'López', 'García', '1990-04-12', 'F'),
('PAC-000002', 'Carlos', 'Ramírez', 'Torres', '1985-09-30', 'M'),
('PAC-000003', 'Valeria', 'Soto', 'Hernández', '1998-01-22', 'F'),
('PAC-000004', 'Miguel', 'Nava', 'Durán', '1976-11-05', 'M'),
('PAC-000005', 'Fernanda', 'Ríos', 'Campos', '2001-07-18', 'F'),
('PAC-000006', 'José', 'Medina', '', '1969-03-02', 'M'),
('PAC-000007', 'Lucía', 'Carrillo', 'Vega', '2012-05-14', 'F'),
('PAC-000008', 'Pablo', 'Arriaga', 'León', '2010-10-09', 'M'),
('PAC-000009', 'Roberto', 'Mendez', 'Paz', '1995-02-11', 'M'),
('PAC-000010', 'Diana', 'Ruiz', 'Solis', '1988-12-01', 'F');

INSERT INTO personal_servicios (id_personal, id_servicio) VALUES
(3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (5, 3), (6, 4), (7, 5), (9, 6);

INSERT INTO citas (folio, id_paciente, id_personal, id_servicio, consultorio, fecha, hora_inicio, hora_fin, estado) VALUES
('CIT-000001', 1, 3, 1, 'Consultorio 1', '2026-11-10', '09:00', '10:00', 'confirmada'),
('CIT-000002', 2, 3, 2, 'Consultorio 1', '2026-11-10', '10:00', '10:50', 'completada'),
('CIT-000003', 3, 4, 1, 'Consultorio 2', '2026-11-11', '09:00', '10:00', 'pendiente'),
('CIT-000004', 4, 6, 4, 'Consultorio 3', '2026-11-11', '11:00', '11:30', 'cancelada');

INSERT INTO consultas (id_cita, motivo_consulta, diagnostico) VALUES
(2, 'Estrés laboral crónico', 'Reacción a estrés agudo');

INSERT INTO usuarios (id_personal, rol, nombre_usuario, contrasena_hash) VALUES
(1, 'administracion', 'admin_demo', 'hashfalso123'),
(3, 'profesional', 'profesional_demo', 'hashfalso123');
