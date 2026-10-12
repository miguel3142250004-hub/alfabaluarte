"""

Aqui vamos a poner todos los visuales,
osea colores, diseños y cosas relacionadas
a la vista del sistema chat :D

"""

import tkinter as tk
from tkinter import ttk

COLORES = {
     "fondo": "#F4F7FB",             # gris muy claro: fondo de toda la app
    "blanco": "#FFFFFF",            # tarjetas y cabecera
    "navy": "#14233B",              # azul marino: menú lateral
    "navy_hover": "#243D5D",        # azul marino más claro: botón activo del menú
    "turquesa": "#16A394",          # color principal de la clínica
    "turquesa_oscuro": "#118779",   # turquesa al presionar un botón
    "turquesa_claro": "#E2F6F2",    # turquesa suave: etiquetas y selección
    "texto": "#172B4D",             # texto principal (casi negro)
    "texto_secundario": "#748198",  # texto gris para descripciones
    "borde": "#E3EAF2",             # líneas finas alrededor de tarjetas
    "campo": "#F8FAFD",             # fondo de campos de texto
    "azul": "#377DCC",              # acento azul
    "amarillo": "#A86D00",          # acento amarillo (pendiente)
    "verde": "#16794B",             # acento verde (confirmada)
    "rojo": "#B83B3B",              # acento rojo (errores)
}

FUENTES = {
    "titulo": ("Arial", 22, "bold"),
    "subtitulo": ("Arial", 10),
    "tarjeta_titulo": ("Arial", 12, "bold"),
    "etiqueta": ("Arial", 9, "bold"),
    "texto": ("Arial", 10),
    "numero": ("Arial", 26, "bold"),
    "boton": ("Arial", 10, "bold"),
    "menu": ("Arial", 11),
    "menu_activo": ("Arial", 11, "bold"),
}

def configurar_estilos(ventana):

    """ 
    Aqui vamos a darle estilos para que se vea mas moderno uuwuwuwu
    """

    estilo = ttk.Style(ventana)

    try:
        estilo.theme_use("clam") #AQUI clam nos permite ir cambiando colores en el tema sin errores :D
    except tk.TclError:
        pass

#Ahora se configuran los estilos dentro de los parameteos de una tabla

#FILAs:
    estilo.configure(
        "Treeview",
        background = COLORES["blanco"],
        foreground = COLORES["texto"],
        fieldbackground = COLORES["blanco"],
        rowheight = 34,
        borderwidth = 0,
        font = ("Arial", 10),
    )

#ENCABEZADOS:
    estilo.configure(
        "Treeview.Heading",
        background="#EDF2F7",
        foreground="#43536B",
        font=("Arial", 9, "bold"),
        relief="flat",
        padding=(10, 10),
    )

    estilo.map(
        "Treeview",
        background = [("selected", COLORES["turquesa_claro"])],
        foreground = [("selected", COLORES["texto"])],
    )
    estilo.map("Treeview.Heading", background = [("active", "#E3EAF2")])