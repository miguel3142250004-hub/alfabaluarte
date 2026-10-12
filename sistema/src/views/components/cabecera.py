"""
este va ser como el header de todo el proyecto es un"
"componente por lo mismo del  de barra lateral chicles uwu

"""

import tkinter as tk
from src.views.theme import COLORES

class Cabecera(tk.Frame):

#Siempre qeu pongamos padre en un parametro, se refiere a que 
#va ser como ese contenedor principal, de la ventana donde va salir esto
#tipo es la caja principal de la cabecera y en la barra lateral
#era la caja principal donde se guarda todo lo de la barra lateral
#esto para que ps chat, todo este guardado es como si fueran objetos justamebnte XDXDXdDxdX
    def __init__(self, padre, rol = "ADMINISTRACION", usuario ="Usuario Administrador"):
        super().__init__(
            padre, bg=COLORES["blanco"], height=76,
            highlightbackground=COLORES["borde"], highlightthickness=1,
        )

        self.grid_propagate(False) #Esto siempre es qeu no se encoja sin importat su cntenido dentro de la caja de "padre" padresintos
        
        self.grid_columnconfigure(0, weight=1) #Esto basicamente es para que en la izquieda se adapte el contenido a la caja y n oal reves OnO


        #vamos a agrupar los testos aki
        izquierda = tk.Frame(self, bg=COLORES["blanco"])
        izquierda.grid(row = 0, column = 0, sticky="w", padx=30, pady=14)
        #la "w" siempre va significar que se aline a la izquierda por que significa ueste owo

        tk.Label(
            izquierda, text = "Sistema de gestion clinica",
            bg = COLORES["blanco"], fg=COLORES["texto"],
            font=("Arial", 14, "bold"),
        ).pack(anchor="w")


        tk.Label(
            izquierda, text = "Organizacion de pacientes, especialistas y citas",
            bg = COLORES["blanco"], fg = COLORES["texto_secundario"],
            font = ("Arial", 9)

        ).pack(anchor="w", pady=(3, 0))

        #ahora haremos lo mismo pero en la parte de los bloques derechos chicos

        derecha = tk.Frame(self, bg=COLORES["blanco"])
        derecha.grid(row=0, column=1, sticky="e", padx=28) #"e" es de este agora osea deresha

        tk.Label(
            derecha, text=rol,
            bg=COLORES["turquesa_claro"], fg="#137D72",
            font=("Arial", 8, "bold"), padx=12, pady=7,
        ).pack(side="left", padx=(0, 12))
        
        tk.Label(
            derecha, text=usuario,
            bg=COLORES["blanco"], fg=COLORES["texto"],
            font=("Arial", 9, "bold"),
        ).pack(side="left")
