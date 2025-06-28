import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk

class UnidadesFrame(tb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(style='MainPanel.TFrame')

        # Aquí puedes agregar el nuevo contenido del formulario de las unidades
        pass