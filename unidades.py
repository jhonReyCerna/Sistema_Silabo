import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk

class UnidadesFrame(tb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(style='MainPanel.TFrame')

        field_pairs = [
            [("Unidad", "unidad_entry"), ("Tema", "tema_entry")],
            [("Fecha de inicio", "fecha_inicio_entry"), ("Sesiones", "sesiones_entry")],
            [("Indicador de logro", "indicador_entry"), ("Instrumentos de Evaluación", "instrumentos_entry")],
            [("Resultado de aprendizaje", "resultado_entry"), ("Producto de aprendizaje", "producto_entry")],
            [("Link de referencia (APA 7)", "link_entry"), ("Días seleccionados", "dias_entry")],
        ]

        content = tb.Frame(self, style='MainPanel.TFrame')
        content.pack(expand=True, fill='both')

        entries = {}
        for row, pair in enumerate(field_pairs):
            for col, (label_text, var_name) in enumerate(pair):
                label = tk.Label(content, text=label_text, anchor="w", font=("Segoe UI", 13, "bold"))
                label.grid(row=row, column=col*2, padx=(60 if col == 1 else 10, 10), pady=12, sticky="w")
                if var_name in ["sesiones_entry"]:
                    entry = tk.Spinbox(content, from_=0, to=99, width=28, font=("Segoe UI", 12), bg='#f3f5f7')
                elif var_name == "fecha_inicio_entry":
                    entry = tk.Entry(content, width=32, font=("Segoe UI", 12), bg='#f3f5f7')
                elif var_name == "link_entry":
                    entry = tk.Entry(content, width=32, font=("Segoe UI", 12), bg='#f3f5f7')
                elif var_name in ["unidad_entry", "tema_entry", "indicador_entry", "instrumentos_entry", "resultado_entry", "producto_entry", "dias_entry"]:
                    entry = tk.Entry(content, width=32, font=("Segoe UI", 12), bg='#f3f5f7')
                else:
                    entry = tk.Entry(content, width=32, font=("Segoe UI", 12), bg='#f3f5f7')
                entry.grid(row=row, column=col*2+1, padx=(0, 60 if col == 0 else 10), pady=12, sticky="nsew")
                entries[var_name] = entry

        self.entries = entries

        self.btn_guardar = tb.Button(content, text="Guardar", style='Unidades.TButton', width=16)
        self.btn_guardar.grid(row=len(field_pairs), column=0, columnspan=4, pady=20)