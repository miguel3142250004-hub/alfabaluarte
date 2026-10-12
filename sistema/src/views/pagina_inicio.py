"""
es como la pagina especifica en la que estamos,
pagina_base es como el molde, de todas las paginas,
pero esta es la pagina de inicio en la que vamos a estar primero
"""


from src.views.pagina_base import PaginaBase
from src.views.components.encabezado_pagina import EncabezadoPagina

"""
como estamos herando paginabase entonces ya tenemos esa cajita con el fondo
sin tener que crearla denuevo esa caja paddre, donde se almacena
el fondaso si o no
"""

class PaginaInicio(PaginaBase):

    def construir(self):
        EncabezadoPagina(
            self,
            "Resumen de la clínica",
            "Una vista rápida de la actividad y de los registros del sistema.",
            "+ Nueva cita",
            lambda: self.app.mostrar_pagina("citas"),
        ).grid(row=0, column=0, sticky="ew", pady=(0, 22))