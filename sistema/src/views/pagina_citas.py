from src.views.pagina_base import PaginaBase
from src.views.components.encabezado_pagina import EncabezadoPagina


class PaginaCitas(PaginaBase):

    def construir(self):
        EncabezadoPagina(
            self,
            "Agenda de citas",
            "Administra las citas y consulta qué paciente atenderá cada especialista.",
        ).grid(row=0, column=0, sticky="ew", pady=(0, 22))