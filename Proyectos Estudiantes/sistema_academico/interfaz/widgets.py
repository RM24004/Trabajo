import tkinter as tk
from tkinter import ttk

from interfaz import estilos


class Aviso:
    def __init__(self, master, texto_inicial=""):
        self.var = tk.StringVar(value=texto_inicial)
        self.label = ttk.Label(master, textvariable=self.var, style="Aviso.TLabel", wraplength=520)

    def exito(self, texto):
        self.var.set(texto)
        self.label.configure(style="Aviso.TLabel")

    def error(self, texto):
        self.var.set(texto)
        self.label.configure(style="Error.TLabel")

    def info(self, texto):
        self.var.set(texto)
        self.label.configure(style="Aviso.TLabel")

    def limpiar(self):
        self.var.set("")


class CampoTexto:
    def __init__(self, master, etiqueta, valor="", ancho=34, tipo="texto", ayuda="", unidad=""):
        self.tipo = tipo
        self.var = tk.StringVar(value=str(valor))
        self.unidad = unidad

        marco = tk.Frame(master, bg="#ffffff", highlightbackground="#d0d7de", highlightthickness=1)
        marco.pack(fill="x", padx=18, pady=5)

        fila = tk.Frame(marco, bg="#ffffff")
        fila.pack(fill="x", padx=10, pady=(7, 2))

        ttk.Label(fila, text=etiqueta + " *", style="Campo.TLabel").pack(side="left")
        if unidad:
            ttk.Label(fila, text=unidad, style="Campo.TLabel").pack(side="right")

        self.entrada = ttk.Entry(
            marco,
            textvariable=self.var,
            width=ancho,
            style="Campo.TEntry",
            show="*" if tipo == "clave" else "",
            justify="left",
        )
        self.entrada.pack(fill="x", padx=10, pady=(0, 8))

        if ayuda:
            ttk.Label(marco, text=ayuda, style="Campo.TLabel", foreground="#8a8a8a").pack(
                anchor="w", padx=10, pady=(0, 6)
            )

    def obtener(self):
        return self.var.get().strip()

    def fijar(self, valor):
        self.var.set(str(valor))

    def enfocar(self):
        self.entrada.focus_set()
        self.entrada.selection_range(0, "end")


class CampoSeleccion:
    def __init__(self, master, etiqueta, valores, ancho=32, ayuda=""):
        self.var = tk.StringVar()

        marco = tk.Frame(master, bg="#ffffff", highlightbackground="#d0d7de", highlightthickness=1)
        marco.pack(fill="x", padx=18, pady=5)

        ttk.Label(marco, text=etiqueta + " *", style="Campo.TLabel").pack(anchor="w", padx=10, pady=(7, 2))

        combo = ttk.Combobox(
            marco,
            textvariable=self.var,
            values=list(valores),
            width=ancho,
            state="readonly",
            style="Campo.TCombobox",
        )
        combo.pack(fill="x", padx=10, pady=(0, 8))

        if ayuda:
            ttk.Label(marco, text=ayuda, style="Campo.TLabel", foreground="#8a8a8a").pack(
                anchor="w", padx=10, pady=(0, 6)
            )
        self.combo = combo

    def obtener(self):
        return self.var.get()

    def fijar(self, valor):
        if valor:
            self.var.set(valor)

    def habilitar(self, estado):
        self.combo.configure(state="readonly" if estado else "disabled")


class Tabla:
    def __init__(self, master, columnas, titulos, anchos, altura=12, on_doble_clic=None, on_seleccion=None):
        self.marco = ttk.Frame(master)
        self.marco.pack(fill="both", expand=True, padx=12, pady=(8, 4))

        self.arbol = ttk.Treeview(
            self.marco,
            columns=columnas,
            show="headings",
            height=altura,
            selectmode="browse",
        )
        for columna, titulo, ancho in zip(columnas, titulos, anchos):
            self.arbol.heading(columna, text=titulo)
            self.arbol.column(columna, width=ancho, anchor="w", stretch=True)

        barra = ttk.Scrollbar(self.marco, orient="vertical", command=self.arbol.yview)
        self.arbol.configure(yscrollcommand=barra.set)
        self.arbol.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        if on_doble_clic:
            self.arbol.bind("<Double-1>", lambda _e: on_doble_clic(self.id_seleccionada()))
        if on_seleccion:
            self.arbol.bind("<<TreeviewSelect>>", lambda _e: on_seleccion(self.id_seleccionada()))

    def limpiar(self):
        self.arbol.delete(*self.arbol.get_children())

    def insertar(self, id_registro, valores, etiqueta=""):
        self.arbol.insert("", "end", iid=str(id_registro), values=valores, tags=(etiqueta,) if etiqueta else ())

    def id_seleccionada(self):
        seleccion = self.arbol.selection()
        return seleccion[0] if seleccion else None

    def resaltado_si_existe(self, id_registro):
        if id_registro and self.arbol.exists(str(id_registro)):
            self.arbol.selection_set(str(id_registro))
            self.arbol.focus(str(id_registro))
            self.arbol.see(str(id_registro))


class TarjetaEstadistica:
    def __init__(self, master, titulo, valor_inicial="0"):
        marco = ttk.Labelframe(master, text=titulo, style="Estadistica.TLabelframe", padding=(10, 8))
        self.var = tk.StringVar(value=str(valor_inicial))
        ttk.Label(marco, textvariable=self.var, style="Valor.TLabel").pack(anchor="center")
        marco.pack(side="left", fill="x", expand=True, padx=5, pady=(10, 0))

    def actualizar(self, valor):
        self.var.set(str(valor))