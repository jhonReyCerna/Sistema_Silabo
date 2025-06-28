
import tkinter as tk
import ttkbootstrap as tb
from PIL import Image, ImageTk  
from Fomulario import FormularioGeneral

COLORES = {
    'pendiente': '#B0BEC5',    
    'en_edicion': '#1976D2',     
    'completado': '#388E3C',     
    'hover': '#1565C0',         
    'fondo': '#F4F8FB',          
    'borde': '#E3E7EB',          
    'texto': '#263238',          
    'gris': '#90A4AE'            
}

iconos = {
    'formulario': '📝',
    'unidades': '📚',
    'competencias': '🎯',
    'productos': '📦',
    'sesiones': '📅',
    'referencias': '🔗'
}

def centrar_ventana(ventana, ancho_deseado, alto_deseado, margen=40):
    ventana.update_idletasks()
    ws = ventana.winfo_screenwidth()
    hs = ventana.winfo_screenheight()
    ancho = min(ancho_deseado, ws - margen)
    alto = min(alto_deseado, hs - margen)
    x = (ws // 2) - (ancho // 2)
    y = (hs // 2) - (alto // 2) - 40
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def main():
    root = tb.Window(themename="flatly")
    root.state('zoomed')
    root.title("Panel de Control del Sílabo")
    ancho_deseado, alto_deseado = 1800, 950 
    root.resizable(False, False)
    root.configure(bg=COLORES['fondo'])

    style = tb.Style()
    style.configure('Header.TFrame', background="#1976D2")
    style.configure('Header.TLabel', background="#1976D2", foreground="white", font=("Segoe UI Emoji", 34, "bold"))
    style.configure('Sidebar.TFrame', background="#ffffff")
    style.configure('MainPanel.TFrame', background="#ffffff")
    style.configure('Footer.TLabel', background="#E3E7EB", foreground="#1976D2", font=("Segoe UI", 12, "italic"))
    style.configure('Superior.TFrame', background='#FFFFFF')

    pro_btn_bg = "#ffffff" 
    pro_btn_bg_active = "#3874fe"  
    pro_btn_bg_pressed = "#CFD8DC"
    pro_btn_fg = "#68737d"  

    for btn_style in [
        'General.TButton', 'Unidades.TButton', 'Competencias.TButton',
        'Productos.TButton', 'Sesiones.TButton', 'Referencias.TButton'
    ]:
        style.configure(
            btn_style,
            font=("Segoe UI", 13, "bold"),
            foreground=pro_btn_fg,
            background=pro_btn_bg,
            borderwidth=0,
            relief="flat",
            padding=(20, 12),
            bordercolor="#CFD8DC",
            focusthickness=3,
            focuscolor="#B0C5B5",
            lightcolor="#FFFFFF",
            darkcolor="#CFD8DC",
            anchor="center"
        )
        style.map(
            btn_style,
            foreground=[('active', '#ffffff'), ('pressed', '#1976D2')],
            background=[('active', pro_btn_bg_active), ('pressed', pro_btn_bg_pressed)]
        )

    style.configure(
        'GeneralSelected.TButton',
        font=("Segoe UI", 13, "bold"),
        foreground="#ffffff",
        background="#1976D2",
        borderwidth=0,
        relief="flat",
        padding=(20, 12),
        bordercolor="#CFD8DC",
        focusthickness=3,
        focuscolor="#B0C5B5",
        lightcolor="#1976D2",
        darkcolor="#1976D2",
        anchor="center"
    )
    style.map(
        'GeneralSelected.TButton',
        foreground=[('active', '#ffffff'), ('pressed', '#1976D2')],
        background=[('active', '#1976D2'), ('pressed', '#1976D2')]
    )

    style.configure('Hamburger.TButton', background='#ffffff', foreground='#191919', font=("Segoe UI", 26, "bold"), borderwidth=0, relief="flat", padding=(12, 10))
    style.map('Hamburger.TButton', background=[('active', '#e3e7eb')], foreground=[('active', '#191919')])

    header = tb.Frame(root, style='Header.TFrame', height=80)
    header.pack(fill='x', side='top')
    tb.Label(
        header,
        text="📋 Panel de Control del Sílabo",
        anchor="center",
        style='Header.TLabel',
        justify='center',
        padding=(30, 20)
    ).pack(expand=True)

    main_content = tb.Frame(root, style='MainPanel.TFrame')
    main_content.pack(fill='both', expand=True)

    sidebar = tb.Frame(main_content, style='Sidebar.TFrame', width=400)
    sidebar.pack(side='left', fill='y', padx=(0, 0), pady=(0, 0))
    sidebar.pack_propagate(False)


    main_panel = tb.Frame(main_content, style='MainPanel.TFrame')
    main_panel.pack(side='right', fill='both', expand=True, padx=(0, 0), pady=(0, 0))

    superior_frame = tb.Frame(main_panel, style='Superior.TFrame', height=120)
    superior_frame.pack(fill='x', side='top')
    inferior_frame = tb.Frame(main_panel, style='MainPanel.TFrame')
    inferior_frame.pack(fill='both', expand=True, side='bottom')
    formulario_general = None

    botones_superior = [
        ("General", 'General.TButton'),
        ("Unidades", 'Unidades.TButton'),
        ("Competencias", 'Competencias.TButton'),
        ("Productos", 'Productos.TButton'),
        ("Sesiones", 'Sesiones.TButton'),
        ("Referencias", 'Referencias.TButton')
    ]
    botones_frame_superior = tb.Frame(superior_frame, style='Superior.TFrame')
    botones_frame_superior.pack(side='top', fill='x', padx=20, pady=10)
    botones_superior_refs = []
    for i, (nombre, estilo) in enumerate(botones_superior):
        btn = tb.Button(
            botones_frame_superior,
            text=nombre,
            style=estilo,
            width=14,
            padding=(10, 8)
        )
        btn.pack(side='left', padx=8, pady=4)
        botones_superior_refs.append(btn)
        if i < len(botones_superior) - 1:
            flecha = tk.Label(
                botones_frame_superior,
                text='→',
                font=("Segoe UI", 18, "bold"),
                background="#FFFFFF",
                foreground="#1976D2",
                padx=2
            )
            flecha.pack(side='left', pady=4)

    nombres = {
        'formulario': 'General',
        'unidades': 'Unidades',
        'competencias': 'Competencias',
        'productos': 'Productos',
        'sesiones': 'Sesiones',
        'referencias': 'Referencias'
    }

    sidebar_expanded = {'value': True}
    sidebar_width_expanded = 400
    sidebar_width_collapsed = 70
    botones_refs = []  
    keys_ordenados = list(nombres.keys())

    nav_frame = tb.Frame(sidebar, style='Sidebar.TFrame')
    nav_frame.pack(fill='x', pady=(10, 0))
    nav_label = tk.Label(
        nav_frame,
        text="Navegación",
        font=("Segoe UI", 18, "bold"),
        background="#E3E7EB",
        foreground="#191919",
        anchor="center",
        padx=10
    )
    nav_label.pack(side='left', expand=True, fill='x')
    hamburger_btn = tb.Button(
        nav_frame,
        text='≡',
        style='Hamburger.TButton',
        width=2
    )
    hamburger_btn.pack(side='right', padx=(8, 0))

    botones_frame = tb.Frame(sidebar, style='Sidebar.TFrame')
    botones_frame.pack(fill='y', expand=True, padx=(10, 10), pady=(0, 0))

    hamburger_icon_btn = tb.Button(
        botones_frame,
        text='≡',
        style='Hamburger.TButton',
        width=4,
        padding=(0, 12)
    )
    hamburger_icon_btn.grid(row=0, column=0, padx=0, pady=18, sticky='ew')
    hamburger_icon_btn.grid_remove() 

    row = 0
    estilos_botones = {
        'formulario': 'General.TButton',
        'unidades': 'Unidades.TButton',
        'competencias': 'Competencias.TButton',
        'productos': 'Productos.TButton',
        'sesiones': 'Sesiones.TButton',
        'referencias': 'Referencias.TButton'
    }
    def mostrar_formulario_general():
        nonlocal formulario_general
        for widget in inferior_frame.winfo_children():
            widget.destroy()
        formulario_general = FormularioGeneral(inferior_frame)
        formulario_general.pack(fill='both', expand=True, padx=40, pady=40)
        for idx, btn in enumerate(botones_superior_refs):
            if idx == 0:
                btn.config(style='GeneralSelected.TButton')
            else:
                btn.config(style=botones_superior[idx][1])

    for key in keys_ordenados:
        if key == 'formulario':
            btn_command = mostrar_formulario_general
        else:
            btn_command = lambda: None
        btn = tb.Button(
            botones_frame,
            text=f"{iconos[key]} {nombres[key]}",
            style=estilos_botones[key],
            state='normal',
            command=btn_command,
            width=30,
            padding=(20, 12)
        )
        btn.grid(row=row+1, column=0, padx=0, pady=18, sticky='ew')
        btn.configure(cursor="hand2")
        botones_refs.append(btn)
        row += 1
    botones_frame.grid_columnconfigure(0, weight=1)
    sidebar.pack_propagate(False)

    def toggle_sidebar():
        if sidebar_expanded['value']:
            sidebar.config(width=sidebar_width_collapsed)
            for i, btn in enumerate(botones_refs):
                key = keys_ordenados[i]
                btn.config(text=iconos[key], width=4, padding=(0, 12))
            nav_label.config(text='')
            nav_frame.pack_forget()
            hamburger_icon_btn.grid()
            sidebar_expanded['value'] = False
        else:
            sidebar.config(width=sidebar_width_expanded)
            for i, btn in enumerate(botones_refs):
                key = keys_ordenados[i]
                btn.config(text=f"{iconos[key]} {nombres[key]}", width=30, padding=(20, 12))
            nav_label.config(text='Navegación')
            hamburger_icon_btn.grid_remove()
            
            nav_frame.pack_forget()
            nav_frame.pack(before=botones_frame, fill='x', pady=(10, 0))
            sidebar_expanded['value'] = True
        sidebar.pack_propagate(False)

    hamburger_icon_btn.config(command=toggle_sidebar)
    hamburger_btn.config(command=toggle_sidebar)

    footer = tb.Frame(root, style='Sidebar.TFrame', height=40)
    footer.pack(fill='x', side='bottom')
    tb.Label(
        footer,
        text="© 2025 Universidad UNAC - Sistema de Sílabo",
        style='Footer.TLabel',
        anchor="center"
    ).pack(expand=True)

    root.update_idletasks()
    centrar_ventana(root, ancho_deseado, alto_deseado)
    root.mainloop()

if __name__ == "__main__":
    main()
