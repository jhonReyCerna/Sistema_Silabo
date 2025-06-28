import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk

class UnidadesFrame(tb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(style='MainPanel.TFrame')

        # Título del formulario
        titulo = tk.Label(self, text="Formulario de las Unidades", font=("Segoe UI", 18, "bold"), anchor="center")
        titulo.pack(pady=(20, 10))