"""
es lo misma razon de los otros
reutilizaremos este boton para no estarlo creando siempre
es como cuando el profe dago hacia su archivo de funciones
donee guardaba todas las de presine tecla y eso el señor profesor
"""

import tkinter as tk
from src.views.theme import COLORES, FUENTES


class Boton(tk.Button):


    def __init__(self, padre, texto, comando, tipo ="primario"):

        if tipo == "primario":
            fondo = COLORES["turquesa"]
            color_texto = "white"
            fondo_activo = COLORES["turquesa_oscuro"]
        else:
            fondo = COLORES["blanco"]
            color_texto = COLORES["texto"]
            fondo_activo = "#EAF0F6"


        super().__init__(
            padre,
            text=texto,
            command=comando,
            bg=fondo,
            fg=color_texto,
            activebackground=fondo_activo,
            activeforeground=color_texto,
            font=FUENTES["boton"],
            bd=0,
            relief="flat",
            cursor="hand2",
            padx=16,
            pady=10,
            highlightthickness=0,
        )