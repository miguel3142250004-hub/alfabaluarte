SET search_path TO clinica, public;

SELECT c.folio AS folio_cita, 
       p.nombre || ' ' || p.primer_apellido AS paciente, 
       doc.nombre || ' ' || doc.primer_apellido AS profesional, 
       s.nombre AS servicio, 
       c.fecha, c.hora_inicio, c.estado
FROM citas c
JOIN pacientes p ON c.id_paciente = p.id_paciente
JOIN personal doc ON c.id_personal = doc.id_personal
JOIN servicios s ON c.id_servicio = s.id_servicio
ORDER BY c.fecha, c.hora_inicio;

SELECT doc.nombre || ' ' || doc.primer_apellido AS profesional, 
       COUNT(c.id_cita) AS total_citas
FROM personal doc
LEFT JOIN citas c ON doc.id_personal = c.id_personal
GROUP BY doc.id_personal, doc.nombre, doc.primer_apellido;

SELECT p.folio, p.nombre, con.motivo_consulta, con.diagnostico, c.fecha
FROM consultas con
JOIN citas c ON con.id_cita = c.id_cita
JOIN pacientes p ON c.id_paciente = p.id_paciente
WHERE p.id_paciente = 2;
