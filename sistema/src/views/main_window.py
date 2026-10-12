"""VENTANA PRINCIPAL del sistema.
aqui practicamente acomodamos y importamos todo lo de 
los demas archivos para que despues
aparezca en la ejecucion :D
"""
"""VENTANA PRINCIPAL del sistema.

Esta clase es el "director de orquesta": arma la estructura fija (menú lateral,
cabecera, pie) y decide qué pantalla se muestra en el centro.
"""

import tkinter as tk

from src.views.theme import COLORES, configurar_estilos
from src.views.components.barra_lateral import BarraLateral
from src.views.components.cabecera import Cabecera

# Importamos las CLASES de cada pantalla (todavía no se crea ningún objeto).
from src.views.pagina_inicio import PaginaInicio
from src.views.pagina_pacientes import PaginaPacientes
from src.views.pagina_citas import PaginaCitas


class VentanaPrincipal(tk.Tk):

   
    OPCIONES_MENU = [
        ("inicio", "⌂   Inicio"),
        ("pacientes", "◉   Pacientes"),
        ("citas", "▦   Agenda de citas"),
    ]

   
    PAGINAS = {
        "inicio": PaginaInicio,
        "pacientes": PaginaPacientes,
        "citas": PaginaCitas,
    }

    def __init__(self):
        super().__init__()

        self.title("Clínica Alfa Baluarte | Sistema de gestión")
        self.geometry("1360x830")
        self.minsize(1100, 700)
        self.configure(bg=COLORES["fondo"])
        configurar_estilos(self)

      
        self.pagina_actual = None

        self._construir_estructura()
        self.mostrar_pagina("inicio")

    def _construir_estructura(self):
        """Arma las partes FIJAS de la ventana (las que no cambian al navegar)."""

        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

       
        self.barra_lateral = BarraLateral(self, self.OPCIONES_MENU, self.mostrar_pagina)
        self.barra_lateral.grid(row=0, column=0, sticky="nsw")

       
        panel = tk.Frame(self, bg=COLORES["fondo"])
        panel.grid(row=0, column=1, sticky="nsew")
        panel.grid_rowconfigure(1, weight=1)        
        panel.grid_columnconfigure(0, weight=1)


        Cabecera(panel).grid(row=0, column=0, sticky="ew")

      
        self.contenedor = tk.Frame(panel, bg=COLORES["fondo"])
        self.contenedor.grid(row=1, column=0, sticky="nsew", padx=28, pady=(22, 12))
        self.contenedor.grid_columnconfigure(0, weight=1)
        self.contenedor.grid_rowconfigure(0, weight=1)

        
        tk.Label(
            panel,
            text="Clínica Alfa Baluarte  ·  Prototipo académico  ·  Datos ficticios",
            bg=COLORES["fondo"], fg=COLORES["texto_secundario"],
            font=("Arial", 9), anchor="w",
        ).grid(row=2, column=0, sticky="ew", padx=30, pady=(0, 12))

    def mostrar_pagina(self, clave):
        """Cambia la pantalla visible. Se llama al dar clic en el menú.

        Pasos:
          1) destruir la pantalla anterior (si hay una)
          2) crear la nueva
          3) resaltar el botón del menú
        """

     
        if self.pagina_actual is not None:
            self.pagina_actual.destroy()

  
        clase_pagina = self.PAGINAS[clave]
        self.pagina_actual = clase_pagina(self.contenedor, self)
        self.pagina_actual.grid(row=0, column=0, sticky="nsew")

       
        self.barra_lateral.marcar_activo(clave)