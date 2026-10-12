from src.views.pagina_base import PaginaBase
from src.views.components.encabezado_pagina import EncabezadoPagina


class PaginaPacientes(PaginaBase):

    def construir(self):
        EncabezadoPagina(
            self,
            "Pacientes",
            "Consulta los expedientes registrados y agrega nuevos pacientes.",
        ).grid(row=0, column=0, sticky="ew", pady=(0, 22))