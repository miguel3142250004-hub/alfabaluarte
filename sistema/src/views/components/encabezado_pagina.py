"""
Ps denuevo como el nombre le dice es el encabezado de cada pagina chat,
y ps otravez de aqui mismo lo reutilizamosh

"""

import tkinter as tk
from src.views.theme import COLORES, FUENTES
from src.views.components.boton import Boton

class EncabezadoPagina(tk.Frame):

    def __init__(self, padre, titulo, descripcion, texto_boton=None,
                 comando_boton = None):
        super().__init__(padre, bg=COLORES["fondo"])

        self.grid_columnconfigure(0, weight=1)

        bloque = tk.Frame(self, bg=COLORES["fondo"])
        bloque.grid(row=0, column=0, sticky="w")

        tk.Label(
                bloque, text=titulo,
                bg=COLORES["fondo"], fg=COLORES["texto"],
                font=FUENTES["titulo"], anchor="w",
            ).pack(anchor="w")

        tk.Label(
                bloque, text=descripcion,
                bg=COLORES["fondo"], fg=COLORES["texto_secundario"],
                font=FUENTES["subtitulo"], anchor="w",
            ).pack(anchor="w", pady=(6, 0))

        if texto_boton and comando_boton:

            Boton(self, texto_boton, comando_boton).grid(
                row=0, column=1, sticky="e", padx=(20, 0)
            )