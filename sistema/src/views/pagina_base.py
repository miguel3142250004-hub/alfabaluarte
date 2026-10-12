"""

okey esto esta medio raro de explicar pero ahi va
este archivo ba ser como un "molde" osea que aqui vamos a heredar 
todas las pantallas del sistema, que pantallas?
bueno, la de inicio que es la que se ejecuta primero, y posteriormente,
pacientes, o agendas o lo que pongamos etc,  bamos a crear un metodo
aqui para que a raiz de este archivo se puedan heredar esas pantallas entre si
vale tios? les gou

es decir es como un molde que todas las pantallas van a usar pues 
para que funcionen correctamente y tengan como una tipo sinergia entre si vale tios

es la "base" precisamente que todas las paginas seguiran

"""

from abc import ABC, abstractmethod

import tkinter as tk
from src.views.theme import COLORES

class PaginaBase(tk.Frame, ABC):

    #el atributo app es para que cada pantallapueda pedir las mismas cosas
    #tipo como cambiar de pantallas entre si, por la misma herencia que aplicaremos

    def __init__(self, padre, app):
        super().__init__(padre, bg=COLORES["fondo"])

        self.app = app #Es la ventana principal osea va estar disponibles en todos los apartados o metodos pues
        self.grid_columnconfigure(0, weight=1)

        self.construir()

    @abstractmethod
    def construir(self):
        pass
