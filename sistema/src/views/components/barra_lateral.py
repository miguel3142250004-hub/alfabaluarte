"""
Este va ser un componente chat ya que solo lo haremos una vez
y lo reutilizaremos en todos lados oki babys uwu

y va ser la barra lateral del sistema uwu
bueno si es que se queda veda capaz y se va a la chingada ñya
"""
import tkinter as tk
from pathlib import Path

from src.views.theme import COLORES, FUENTES


class BarraLateral(tk.Frame):

    def __init__(self, padre, opciones, al_navegar):
        super().__init__(padre, bg=COLORES["navy"], width=245)
        self.pack_propagate(False)
        self.botones = {}

        logo_bloque = tk.Frame(self, bg=COLORES["navy"])
        logo_bloque.pack(fill="x", padx=22, pady=(27, 30))

        logo_path = Path(__file__).resolve().parents[2] / "assets" / "logo.png"
        try:
            self.logo_imagen = tk.PhotoImage(file=str(logo_path))
        except (FileNotFoundError, tk.TclError) as error:
            raise RuntimeError(
                f"Error, logo no encontrado."
            ) from error

        factor_reduccion = max(1, (self.logo_imagen.width() + 63) // 64)
        if factor_reduccion > 1:
            self.logo_imagen = self.logo_imagen.subsample(
                factor_reduccion, factor_reduccion
            )

        tk.Label(
            logo_bloque, image=self.logo_imagen,
            bg=COLORES["navy"], bd=0,
        ).pack(side="left", anchor="n")

        textos = tk.Frame(logo_bloque, bg=COLORES["navy"])
        textos.pack(side="left", padx=(11, 0), fill="x", expand=True)

        tk.Label(
            textos, text="ALFA BALUARTE",
            bg=COLORES["navy"], fg="white",
            font=("Arial", 11, "bold"), anchor="w",
        ).pack(fill="x", pady=(2, 3))

        tk.Label(
            textos, text="GESTIÓN CLÍNICA",
            bg=COLORES["navy"], fg="#A8B8CC",
            font=("Arial", 8, "bold"), anchor="w",
        ).pack(fill="x")

        tk.Label(
            self, text="MENÚ PRINCIPAL",
            bg=COLORES["navy"], fg="#8497AE",
            font=("Arial", 8, "bold"), anchor="w",
        ).pack(fill="x", padx=25, pady=(0, 12))

        for clave, texto in opciones:
            boton = tk.Button(
                self,
                text=texto,
                command=lambda c=clave: al_navegar(c),
                bg=COLORES["navy"],
                fg="#C7D3E0",
                activebackground=COLORES["navy_hover"],
                activeforeground="white",
                font=FUENTES["menu"],
                anchor="w",
                bd=0,
                relief="flat",
                cursor="hand2",
                padx=22, pady=13,
                highlightthickness=0,
            )
            boton.pack(fill="x", padx=12, pady=3)
            self.botones[clave] = boton

        aviso = tk.Frame(
            self, bg="#1B304D",
            highlightbackground="#2B4260", highlightthickness=1,
        )
        aviso.pack(side="bottom", fill="x", padx=16, pady=18)

        tk.Label(
            aviso, text="PRIMER PROTOTIPO",
            bg="#1B304D", fg="#76D7CA",
            font=("Arial", 8, "bold"), anchor="w",
        ).pack(fill="x", padx=13, pady=(12, 5))

        tk.Label(
            aviso, text="Los registros mostrados son\nsolo información de ejemplo.",
            bg="#1B304D", fg="#C0CCDA",
            font=("Arial", 9), justify="left", anchor="w",
        ).pack(fill="x", padx=13, pady=(0, 12))

    def marcar_activo(self, clave_activa):
        for clave, boton in self.botones.items():
            if clave == clave_activa:
                boton.configure(bg=COLORES["navy_hover"], fg="white",
                                font=FUENTES["menu_activo"])
            else:
                boton.configure(bg=COLORES["navy"], fg="#C7D3E0",
                                font=FUENTES["menu"])
