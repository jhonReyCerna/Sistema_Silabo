import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk

class FormularioGeneral(tb.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(style='MainPanel.TFrame')


        # Agrupar los campos en pares para dos columnas
        field_pairs = [
            [("Código", "codigo_entry"), ("Versión", "version_entry")],
            [("Fecha", "fecha_entry"), ("Maestría", "rama_entry")],
            [("Asignatura", "asignatura_entry"), ("Semestre 2025 - ", "semestre_combobox")],
            [("Docente", "docente_entry"), ("Horas Teoría", "horas_teoria_entry")],
            [("Horas Práctica", "horas_practica_entry"), ("Créditos", "creditos_entry")],
            [("Sesiones", "sesiones_entry"), ("Semanas", "semanas_entry")],
            [("Correo", "correo_entry"), ("Código del Posgrado", "codigo_programa_entry")],
            [("Carácter", "caracter_entry"), ("Propósito del Curso", "proposito_entry")],
            [("Seleccionar Horario", "horario_entry"), ("Modalidad", "modalidad_entry")],
        ]

        # Crear un frame interno para centrar el contenido
        content = tb.Frame(self, style='MainPanel.TFrame')
        content.pack(expand=True, fill='both')

        entries = {}
        for row, pair in enumerate(field_pairs):
            for col, (label_text, var_name) in enumerate(pair):
                # Mucho mayor separación entre columnas
                label = tk.Label(content, text=label_text, anchor="w", font=("Segoe UI", 13, "bold"))
                label.grid(row=row, column=col*2, padx=(60 if col == 1 else 10, 10), pady=12, sticky="w")
                if var_name == "version_entry":
                    entry = tk.Spinbox(content, from_=0, to=99, width=28, font=("Segoe UI", 12), bg='#f3f5f7')
                elif var_name in ["horas_teoria_entry", "horas_practica_entry", "sesiones_entry", "semanas_entry"]:
                    entry = tk.Spinbox(content, from_=0, to=99, width=28, font=("Segoe UI", 12), bg='#f3f5f7')
                elif var_name == "fecha_entry":
                    entry = tk.Entry(content, width=32, font=("Segoe UI", 12), bg='#f3f5f7')  # Simula DateEntry
                elif var_name == "semestre_combobox":
                    entry = ttk.Combobox(content, width=30, font=("Segoe UI", 12), state="readonly", values=["A", "B", "C", "D"])
                    entry.current(0)
                elif var_name == "creditos_entry":
                    entry = tk.Entry(content, width=32, font=("Segoe UI", 12), state="readonly", bg='#f3f5f7')
                elif var_name == "caracter_entry":
                    entry = ttk.Combobox(content, width=30, font=("Segoe UI", 12), state="readonly", values=["Seleccionar", "Obligatorio", "Electivo"])
                    entry.current(0)
                elif var_name == "horario_entry":
                    entry = ttk.Combobox(content, width=32, font=("Segoe UI", 12), state="readonly", values=[
                        "Horario: Lunes - Miércoles - Viernes",
                        "Horario: Sábado - Domingo",
                        "Horario: Personalizado"
                    ])
                    entry.current(0)
                elif var_name == "modalidad_entry":
                    entry = ttk.Combobox(content, width=30, font=("Segoe UI", 12), state="readonly", values=["Seleccionar", "Presencial", "Virtual"])
                    entry.current(0)
                elif var_name == "proposito_entry":
                    entry = tk.Text(content, width=28, height=4, font=("Segoe UI", 12), wrap=tk.WORD, bg='#f3f5f7')
                    entry.insert("1.0", "tiene por propósito")
                else:
                    entry = tk.Entry(content, width=32, font=("Segoe UI", 12), bg='#f3f5f7')
                if var_name != "proposito_entry":
                    entry.grid(row=row, column=col*2+1, padx=(0, 60 if col == 0 else 10), pady=12)
                else:
                    entry.grid(row=row, column=col*2+1, padx=(0, 60 if col == 0 else 10), pady=12, sticky="nsew")
                entries[var_name] = entry

        self.entries = entries

        self.btn_guardar = tb.Button(content, text="Guardar", style='General.TButton', width=16)
        self.btn_guardar.grid(row=len(field_pairs), column=0, columnspan=4, pady=20)
