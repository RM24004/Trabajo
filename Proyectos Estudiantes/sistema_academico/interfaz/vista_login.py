import tkinter as tk
from tkinter import ttk

from config import TITULO_APP, VERSION
from interfaz import estilos, widgets
from nucleo.servicios import ErrorAutenticacion


class VistaLogin(ttk.Frame):
    ANCHO_MINIMO = 440

    def __init__(self, master, servicio, al_entrar):
        super().__init__(master, style="TFrame")
        self.servicio = servicio
        self.al_entrar = al_entrar

        tarjeta = tk.Frame(
            self,
            bg="#ffffff",
            highlightbackground="#d7dee5",
            highlightthickness=1,
        )
        self.tarjeta = tarjeta

        cabecera = tk.Frame(tarjeta, bg=estilos.AZUL, height=76)
        cabecera.pack(fill="x")
        cabecera.pack_propagate(False)

        tk.Label(
            cabecera,
            text=TITULO_APP,
            bg=estilos.AZUL,
            fg="white",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=(16, 0))
        tk.Label(
            cabecera,
            text=f"Gestion de estudiantes, materias y notas  -  v{VERSION}",
            bg=estilos.AZUL,
            fg="#cfe2f3",
            font=("Segoe UI", 8),
        ).pack(pady=(2, 16))

        cuerpo = tk.Frame(tarjeta, bg="#ffffff")
        cuerpo.pack(fill="both", expand=True, padx=12, pady=(6, 4))

        tk.Label(
            cuerpo,
            text="Iniciar sesion",
            bg="#ffffff",
            fg=estilos.AZUL,
            font=("Segoe UI", 12, "bold"),
        ).pack(anchor="w", padx=8, pady=(6, 2))

        self.campo_usuario = widgets.CampoTexto(cuerpo, "Usuario", ancho=36)
        self.campo_clave = widgets.CampoTexto(cuerpo, "Contrasena", tipo="clave", ancho=36)

        opciones = tk.Frame(cuerpo, bg="#ffffff")
        opciones.pack(fill="x", padx=28, pady=(2, 4))
        self.ver_clave = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            opciones,
            text="Mostrar contrasena",
            variable=self.ver_clave,
            command=self._alternar_clave,
            style="Blanco.TCheckbutton",
        ).pack(side="left")

        self.credenciales = tk.StringVar(value="Usuario por defecto:  admin  /  admin123")
        tk.Label(
            cuerpo,
            textvariable=self.credenciales,
            bg="#ffffff",
            fg="#8a8a8a",
            font=("Segoe UI", 8),
            wraplength=390,
            justify="left",
        ).pack(anchor="w", padx=28, pady=(4, 8))

        self.aviso = widgets.Aviso(cuerpo)
        self.aviso.label.pack(anchor="w", padx=28, pady=(0, 6))

        botones = tk.Frame(cuerpo, bg="#ffffff")
        botones.pack(fill="x", padx=28, pady=(2, 12))
        ttk.Button(botones, text="Entrar", command=self._entrar, style="Primario.TButton", width=14).pack(
            side="left"
        )
        ttk.Button(botones, text="Salir", command=self._salir, width=10).pack(side="left", padx=8)

        for widget in (self.campo_usuario, self.campo_clave):
            widget.entrada.bind("<Return>", lambda _e: self._entrar())
        self.campo_usuario.enfocar()

        self._ajustar()
        self.bind("<Configure>", self._al_redimensionar)

    def _ajustar(self):
        self.update_idletasks()
        ancho = max(self.ANCHO_MINIMO, self.tarjeta.winfo_reqwidth())
        alto = self.tarjeta.winfo_reqheight()
        disponible_ancho = max(ancho, self.winfo_width())
        disponible_alto = max(alto, self.winfo_height())
        x = max(0, (disponible_ancho - ancho) // 2)
        y = max(0, (disponible_alto - alto) // 2)
        self.tarjeta.place(x=x, y=y, width=ancho, height=alto)
        self._ultimo_tamano = (self.winfo_width(), self.winfo_height())

    def _al_redimensionar(self, _evento):
        actual = (self.winfo_width(), self.winfo_height())
        if actual != getattr(self, "_ultimo_tamano", None):
            self._ajustar()

    def _alternar_clave(self):
        self.campo_clave.entrada.configure(show="" if self.ver_clave.get() else "*")

    def _entrar(self):
        usuario = self.campo_usuario.obtener()
        clave = self.campo_clave.obtener()
        if not usuario:
            self.aviso.error("Escribe tu nombre de usuario.")
            self.campo_usuario.enfocar()
            return
        if not clave:
            self.aviso.error("Escribe tu contrasena.")
            self.campo_clave.enfocar()
            return
        try:
            sesion = self.servicio.iniciar_sesion(usuario, clave)
        except ErrorAutenticacion as error:
            self.aviso.error(str(error))
            self.campo_clave.fijar("")
            self.campo_clave.enfocar()
            return
        self.aviso.limpiar()
        self.al_entrar(sesion)

    def _salir(self):
        self.campo_usuario.fijar("")
        self.campo_clave.fijar("")
        self.aviso.limpiar()
        self.campo_usuario.enfocar()