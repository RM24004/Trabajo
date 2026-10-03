import tkinter as tk
from tkinter import ttk

AZUL = "#1f4e79"
AZUL_CLARO = "#2e6da4"
AZUL_SUAVE = "#e8f0f8"
GRIS_FONDO = "#f4f6f8"
GRIS_TEXTO = "#555555"
VERDE = "#1e7e34"
ROJO = "#c0392b"
AMBAR = "#b9770e"


def aplicar_estilos(root: tk.Misc):
    try:
        ttk.Style().theme_use("vista")
    except tk.TclError:
        try:
            ttk.Style().theme_use("clam")
        except tk.TclError:
            pass

    estilo = ttk.Style()
    estilo.configure(".", font=("Segoe UI", 10))

    estilo.configure("TFrame", background=GRIS_FONDO)
    estilo.configure("Superior.TFrame", background=AZUL)
    estilo.configure("Superior.TLabel", background=AZUL, foreground="white", font=("Segoe UI", 13, "bold"))
    estilo.configure("SuperiorRol.TLabel", background=AZUL, foreground="#cfe2f3", font=("Segoe UI", 9))

    estilo.configure("TLabel", background=GRIS_FONDO, foreground=GRIS_TEXTO)
    estilo.configure("Campo.TLabel", background="#ffffff", foreground=GRIS_TEXTO, font=("Segoe UI", 9))
    estilo.configure("Negrita.TLabel", background=GRIS_FONDO, foreground="#222222", font=("Segoe UI", 11, "bold"))
    estilo.configure("Error.TLabel", background=GRIS_FONDO, foreground=ROJO, font=("Segoe UI", 9))
    estilo.configure("Aviso.TLabel", background=GRIS_FONDO, foreground=VERDE, font=("Segoe UI", 9))
    estilo.configure("Seccion.TLabel", background=GRIS_FONDO, foreground=AZUL, font=("Segoe UI", 11, "bold"))

    estilo.configure("Tarjeta.TLabelframe", background=GRIS_FONDO, borderwidth=1, relief="solid")
    estilo.configure("Tarjeta.TLabelframe.Label", background=GRIS_FONDO, foreground=AZUL, font=("Segoe UI", 10, "bold"))

    estilo.configure("TButton", padding=(12, 6), font=("Segoe UI", 10))
    estilo.configure("Primario.TButton", padding=(12, 6), font=("Segoe UI", 10, "bold"))
    estilo.configure("Peligro.TButton", padding=(10, 6), font=("Segoe UI", 9))

    estilo.configure("TLabelframe", background=GRIS_FONDO)
    estilo.configure("TLabelframe.Label", background=GRIS_FONDO, foreground=AZUL, font=("Segoe UI", 10, "bold"))

    estilo.configure("Accion.TButton", font=("Segoe UI", 9), padding=(8, 4))
    estilo.configure("Buscador.TEntry", padding=4)

    estilo.configure("Estadistica.TLabelframe", background="#ffffff", relief="solid", borderwidth=1)
    estilo.configure("Estadistica.TLabelframe.Label", background=GRIS_FONDO, foreground=AZUL_CLARO, font=("Segoe UI", 9, "bold"))
    estilo.configure("Valor.TLabel", background=GRIS_FONDO, foreground=AZUL, font=("Segoe UI", 16, "bold"))

    estilo.configure("Treeview", rowheight=24, font=("Segoe UI", 9))
    estilo.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))
    estilo.map("Treeview", background=[("selected", AZUL_CLARO)], foreground=[("selected", "white")])

    estilo.configure("TNotebook", background=GRIS_FONDO, borderwidth=0)
    estilo.configure("TNotebook.Tab", padding=(16, 8), font=("Segoe UI", 10))
    estilo.map("TNotebook.Tab", background=[("selected", "#ffffff")], foreground=[("selected", AZUL)])

    estilo.configure("TCheckbutton", background="#ffffff")
    estilo.configure("Blanco.TCheckbutton", background="#ffffff")
    estilo.configure("Campo.TEntry", padding=4)
    estilo.configure("Campo.TCombobox", padding=4)

    root.option_add("*tearOff", False)
    return estilo