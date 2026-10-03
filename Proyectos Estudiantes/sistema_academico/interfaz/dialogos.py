import tkinter as tk
from tkinter import messagebox, ttk

from config import CREDITOS_MAXIMOS, CREDITOS_MINIMOS, NOTA_MAXIMA, NOTA_MINIMA
from interfaz import estilos, widgets
from nucleo.servicios import ErrorAutenticacion, ErrorPermiso, ErrorValidacion


MARGEN_PANTALLA = 80
BORDE_HORIZONTAL = 28
BORDE_VERTICAL = 30


class AreaDesplazable(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=estilos.GRIS_FONDO)
        self.lienzo = tk.Canvas(self, highlightthickness=0, bd=0, bg=estilos.GRIS_FONDO)
        self.barra = ttk.Scrollbar(self, orient="vertical", command=self.lienzo.yview)
        self.lienzo.configure(yscrollcommand=self.barra.set)
        self.lienzo.pack(side="left", fill="both", expand=True)
        self.interior = tk.Frame(self.lienzo, bg=estilos.GRIS_FONDO)
        self._ventana = self.lienzo.create_window((0, 0), window=self.interior, anchor="nw")
        self.interior.bind("<Configure>", self._al_redimensionar_interior)
        self.lienzo.bind("<Configure>", self._al_redimensionar_lienzo)

    def _al_redimensionar_interior(self, _evento):
        self.lienzo.configure(scrollregion=self.lienzo.bbox("all"))

    def _al_redimensionar_lienzo(self, evento):
        self.lienzo.itemconfigure(self._ventana, width=evento.width)

    def desplazar(self, delta):
        self.lienzo.yview_scroll(delta, "units")

    def paginas(self):
        try:
            low, high = self.lienzo.yview()
        except tk.TclError:
            return 0
        return high - low


class DialogoBase(tk.Toplevel):
    def __init__(self, master, titulo, ancho=560, alto=None):
        super().__init__(master)
        self.title(titulo)
        self.resizable(False, False)
        self.configure(bg=estilos.GRIS_FONDO)
        self.transient(master)
        self.valores = None
        self.ancho, self.alto = ancho, alto

        self.pie = tk.Frame(self, bg=estilos.GRIS_FONDO)
        self.pie.pack(side="bottom", fill="x", padx=14, pady=12)

        self.area = AreaDesplazable(self)
        self.area.pack(fill="both", expand=True, padx=14, pady=(14, 0))

        self.cuerpo = tk.Frame(
            self.area.interior, bg="#ffffff", highlightbackground="#d7dee5", highlightthickness=1
        )
        self.cuerpo.pack(fill="both", expand=True)

        self.aviso = widgets.Aviso(self.pie)
        self.aviso.label.pack(anchor="w", padx=6)

        acciones = tk.Frame(self.pie, bg=estilos.GRIS_FONDO)
        acciones.pack(side="right", anchor="e")
        ttk.Button(acciones, text="Cancelar", command=self.cancelar, width=12).pack(side="right", padx=(6, 0))
        ttk.Button(acciones, text="Guardar", command=self.guardar, style="Primario.TButton", width=12).pack(
            side="right"
        )

        self._rueda = self._al_girar_rueda
        self.bind_all("<MouseWheel>", self._rueda)
        self.bind_all("<Button-4>", self._rueda)
        self.bind_all("<Button-5>", self._rueda)
        self.protocol("WM_DELETE_WINDOW", self.cancelar)

    def _al_girar_rueda(self, evento):
        if getattr(self, "_destruido", False) or not self.area.paginas() > 0:
            return
        delta = -1 if getattr(evento, "num", 0) == 4 or evento.delta > 0 else 1
        self.area.desplazar(delta)
        return "break"

    def destroy(self):
        if getattr(self, "_destruido", False):
            return
        self._destruido = True
        for secuencia in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            try:
                self.unbind_all(secuencia)
            except tk.TclError:
                pass
        super().destroy()

    def ajustar(self):
        self.update_idletasks()
        ancho = max(int(self.ancho or 560), self.area.interior.winfo_reqwidth() + BORDE_HORIZONTAL)
        alto_pie = self.pie.winfo_reqheight()
        alto_texto = self.area.interior.winfo_reqheight()
        alto = min(alto_texto + alto_pie + BORDE_VERTICAL, max(300, self.winfo_screenheight() - MARGEN_PANTALLA))
        if alto < alto_texto + alto_pie + BORDE_VERTICAL:
            self.area.barra.pack(side="right", fill="y")
        else:
            self.area.barra.pack_forget()

        x = self.master.winfo_rootx() + max(0, (self.master.winfo_width() - ancho) // 2)
        y = self.master.winfo_rooty() + max(0, (self.master.winfo_height() - alto) // 3)
        x = min(max(0, x), max(0, self.winfo_screenwidth() - ancho))
        y = min(max(0, y), max(0, self.winfo_screenheight() - alto))
        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def titulo(self, texto, subtitulo=""):
        marco = tk.Frame(self.cuerpo, bg="#ffffff")
        marco.pack(fill="x", padx=18, pady=(14, 6))
        tk.Label(marco, text=texto, bg="#ffffff", fg=estilos.AZUL, font=("Segoe UI", 13, "bold")).pack(anchor="w")
        if subtitulo:
            tk.Label(
                marco,
                text=subtitulo,
                bg="#ffffff",
                fg=estilos.GRIS_TEXTO,
                font=("Segoe UI", 9),
                wraplength=ancho_fijo(self) - 60,
                justify="left",
            ).pack(anchor="w", pady=(2, 0))

    def aceptar(self):
        self.ajustar()
        self.grab_set()
        self.focus_set()

    def guardar(self):
        raise NotImplementedError

    def cancelar(self):
        self.valores = None
        self.destroy()

    def mostrar(self):
        self.wait_window()
        return self.valores


def ancho_fijo(dialogo):
    return int(dialogo.ancho) if dialogo.ancho else 520


class DialogoEstudiante(DialogoBase):
    def __init__(self, master, servicio, estudiante=None):
        super().__init__(master, "Estudiante", ancho=540)
        self.servicio = servicio
        self.estudiante = estudiante
        self.editando = estudiante is not None

        if self.editando:
            self.titulo(
                "Editar estudiante",
                "Modifica los datos del alumno. La cedula debe seguir siendo unica en el sistema.",
            )
        else:
            self.titulo(
                "Nuevo estudiante",
                "Registra un alumno y su usuario de acceso al sistema. Si dejas vacios el usuario o la "
                "contrasena, se generan automaticamente.",
            )

        marco = tk.Frame(self.cuerpo, bg="#ffffff")
        marco.pack(fill="both", expand=True)

        self.cedula = widgets.CampoTexto(marco, "Cedula / Matricula", ancho=40)
        self.nombres = widgets.CampoTexto(marco, "Nombres", ancho=40)
        self.apellidos = widgets.CampoTexto(marco, "Apellidos", ancho=40)
        self.email = widgets.CampoTexto(marco, "Email", ancho=40)
        self.telefono = widgets.CampoTexto(marco, "Telefono", ancho=40)
        self.carrera = widgets.CampoTexto(marco, "Carrera", ancho=40)

        separador = tk.Frame(marco, bg="#e3e8ee", height=1)
        separador.pack(fill="x", padx=18, pady=8)

        self.usuario = widgets.CampoTexto(
            marco,
            "Usuario de acceso",
            ancho=24,
            ayuda="Solo si dejas el campo vacio el sistema lo arma automaticamente.",
        )
        self.clave = widgets.CampoTexto(
            marco,
            "Contrasena inicial",
            tipo="clave",
            ancho=24,
            ayuda="Minimo 4 caracteres. Si la dejas vacia se genera una y se muestra al guardar.",
        )

        if self.editando:
            for campo in (self.usuario, self.clave):
                campo.entrada.configure(state="disabled")
            tk.Label(
                marco,
                text="Las credenciales solo se cambian desde 'Restablecer contrasena'.",
                bg="#ffffff",
                fg="#8a8a8a",
                font=("Segoe UI", 8),
            ).pack(anchor="w", padx=28, pady=(0, 10))
        else:
            tk.Label(
                marco,
                text="Deja vacio lo que quieras autogenerar.",
                bg="#ffffff",
                fg="#8a8a8a",
                font=("Segoe UI", 8),
            ).pack(anchor="w", padx=28, pady=(0, 10))

        if self.editando:
            self._cargar(estudiante)

        for campo in (self.cedula, self.nombres, self.apellidos, self.email, self.telefono, self.carrera):
            campo.entrada.bind("<Return>", lambda _e: self.guardar())
        if not self.editando:
            for campo in (self.usuario, self.clave):
                campo.entrada.bind("<Return>", lambda _e: self.guardar())

        self.cedula.enfocar()
        self.aceptar()

    def _cargar(self, estudiante):
        self.cedula.fijar(estudiante.get("cedula", ""))
        self.nombres.fijar(estudiante.get("nombres", ""))
        self.apellidos.fijar(estudiante.get("apellidos", ""))
        self.email.fijar(estudiante.get("email", ""))
        self.telefono.fijar(estudiante.get("telefono", ""))
        self.carrera.fijar(estudiante.get("carrera", ""))

    def guardar(self):
        datos = {
            "cedula": self.cedula.obtener(),
            "nombres": self.nombres.obtener(),
            "apellidos": self.apellidos.obtener(),
            "email": self.email.obtener(),
            "telefono": self.telefono.obtener(),
            "carrera": self.carrera.obtener(),
            "nombre_usuario": self.usuario.obtener(),
            "clave": self.clave.obtener(),
        }
        try:
            if self.editando:
                resultado = self.servicio.actualizar_estudiante(self.estudiante["id"], datos)
                mensaje = f"Datos de {resultado['nombres']} {resultado['apellidos']} actualizados."
            else:
                resultado = self.servicio.agregar_estudiante(datos)
                mensaje = (
                    f"Estudiante creado.\n\nUsuario: {resultado['nombre_usuario']}\n"
                    f"Contrasena: {resultado['clave']}\n\nAnotala, no volvera a mostrarse."
                )
        except ErrorValidacion as error:
            self.aviso.error(str(error))
            return

        self.valores = {"id": resultado["id"], "mensaje": mensaje}
        self.destroy()
        if not self.editando:
            messagebox.showinfo(title="Estudiante registrado", message=mensaje, parent=self.master)


class DialogoMateria(DialogoBase):
    def __init__(self, master, servicio, materia=None):
        super().__init__(master, "Materia", ancho=520)
        self.servicio = servicio
        self.materia = materia
        self.editando = materia is not None

        self.titulo(
            "Editar materia" if self.editando else "Nueva materia",
            "Define el codigo, los creditos y el semestre en el que se imparte.",
        )

        marco = tk.Frame(self.cuerpo, bg="#ffffff")
        marco.pack(fill="both", expand=True)

        self.codigo = widgets.CampoTexto(
            marco,
            "Codigo",
            ancho=24,
            ayuda=f"Entre 3 y 15 caracteres, por ejemplo MAT101.",
        )
        self.nombre = widgets.CampoTexto(marco, "Nombre de la materia", ancho=40)
        self.creditos = widgets.CampoTexto(
            marco,
            "Creditos",
            ancho=12,
            unidad=f"({CREDITOS_MINIMOS} - {CREDITOS_MAXIMOS})",
        )
        self.semestre = widgets.CampoTexto(marco, "Semestre", ancho=12, unidad="(1 - 12)")

        separador = tk.Frame(marco, bg="#e3e8ee", height=1)
        separador.pack(fill="x", padx=18, pady=10)

        self.docente = tk.StringVar(value=servicio.sesion.nombre if servicio.sesion else "")
        marco_docente = tk.Frame(marco, bg="#ffffff")
        marco_docente.pack(fill="x", padx=18, pady=5)
        ttk.Label(marco_docente, text="Docente responsable *", style="Campo.TLabel").pack(anchor="w")
        ttk.Entry(
            marco_docente,
            textvariable=self.docente,
            state="disabled",
            style="Campo.TEntry",
            width=40,
        ).pack(fill="x", pady=(4, 8))

        tk.Label(
            marco,
            text="El docente se toma de la sesion iniciada.",
            bg="#ffffff",
            fg="#8a8a8a",
            font=("Segoe UI", 8),
        ).pack(anchor="w", padx=28, pady=(0, 10))

        if self.editando:
            self.codigo.fijar(materia.get("codigo", ""))
            self.nombre.fijar(materia.get("nombre", ""))
            self.creditos.fijar(materia.get("creditos", ""))
            self.semestre.fijar(materia.get("semestre", ""))
            self.docente.set(materia.get("docente", ""))

        for campo in (self.codigo, self.nombre, self.creditos, self.semestre):
            campo.entrada.bind("<Return>", lambda _e: self.guardar())

        self.codigo.enfocar()
        self.aceptar()

    def guardar(self):
        datos = {
            "codigo": self.codigo.obtener(),
            "nombre": self.nombre.obtener(),
            "creditos": self.creditos.obtener(),
            "semestre": self.semestre.obtener(),
            "docente": self.docente.get(),
        }
        try:
            if self.editando:
                resultado = self.servicio.actualizar_materia(self.materia["id"], datos)
                mensaje = f"Materia {resultado['codigo']} actualizada."
            else:
                resultado = self.servicio.agregar_materia(datos)
                mensaje = f"Materia {resultado['codigo']} registrada."
        except ErrorValidacion as error:
            self.aviso.error(str(error))
            return
        self.valores = {"id": resultado["id"], "mensaje": mensaje}
        self.destroy()


class DialogoNota(DialogoBase):
    def __init__(self, master, servicio, nota=None, estudiante_id=None, materia_id=None):
        super().__init__(master, "Nota", ancho=540)
        self.servicio = servicio
        self.nota = nota
        self.editando = nota is not None

        self.titulo(
            "Editar nota" if self.editando else "Registrar nota",
            f"Las notas van de {NOTA_MINIMA:g} a {NOTA_MAXIMA:g} puntos. El aprobado es 60.",
        )

        marco = tk.Frame(self.cuerpo, bg="#ffffff")
        marco.pack(fill="both", expand=True)

        estudiantes = self.servicio.estudiantes.listar()
        materias = self.servicio.materias.listar()

        if not estudiantes:
            self.aviso.error("Primero registra al menos un estudiante.")
            marco.pack_forget()
        elif not materias:
            self.aviso.error("Primero registra al menos una materia.")
            marco.pack_forget()

        self.etiquetas_estudiante = {
            f"{e['nombres']} {e['apellidos']}  ({e['cedula']})": e["id"] for e in estudiantes
        }
        self.etiquetas_materia = {f"{m['codigo']} - {m['nombre']}": m["id"] for m in materias}

        self.estudiante = widgets.CampoSeleccion(marco, "Estudiante", list(self.etiquetas_estudiante))
        self.materia = widgets.CampoSeleccion(marco, "Materia", list(self.etiquetas_materia))
        self.valor = widgets.CampoTexto(
            marco,
            "Nota",
            ancho=14,
            unidad=f"({NOTA_MINIMA:g} - {NOTA_MAXIMA:g})",
        )
        self.tipo = widgets.CampoTexto(marco, "Tipo de nota", valor="Parcial", ancho=24)
        self.periodo = widgets.CampoTexto(marco, "Periodo", valor="2026-1", ancho=24)

        if not self.editando:
            if estudiante_id:
                for etiqueta, id_ in self.etiquetas_estudiante.items():
                    if id_ == estudiante_id:
                        self.estudiante.fijar(etiqueta)
                        break
            if materia_id:
                for etiqueta, id_ in self.etiquetas_materia.items():
                    if id_ == materia_id:
                        self.materia.fijar(etiqueta)
                        break

        if self.editando:
            self._cargar(nota, estudiantes, materias)
            self.estudiante.habilitar(False)
            self.materia.habilitar(False)

        for campo in (self.valor, self.tipo, self.periodo):
            campo.entrada.bind("<Return>", lambda _e: self.guardar())

        if self.editando:
            self.valor.enfocar()
        else:
            self.estudiante.combo.focus_set()
        self.aceptar()

    def _cargar(self, nota, estudiantes, materias):
        for estudiante in estudiantes:
            if estudiante["id"] == nota.get("estudiante_id"):
                self.estudiante.fijar(f"{estudiante['nombres']} {estudiante['apellidos']}  ({estudiante['cedula']})")
                break
        for materia in materias:
            if materia["id"] == nota.get("materia_id"):
                self.materia.fijar(f"{materia['codigo']} - {materia['nombre']}")
                break
        self.valor.fijar(nota.get("valor", ""))
        self.tipo.fijar(nota.get("tipo", ""))
        self.periodo.fijar(nota.get("periodo", ""))

    def guardar(self):
        etiqueta_estudiante = self.estudiante.obtener()
        etiqueta_materia = self.materia.obtener()
        if not etiqueta_estudiante:
            self.aviso.error("Selecciona un estudiante.")
            return
        if not etiqueta_materia:
            self.aviso.error("Selecciona una materia.")
            return

        datos = {
            "estudiante_id": self.etiquetas_estudiante[etiqueta_estudiante],
            "materia_id": self.etiquetas_materia[etiqueta_materia],
            "valor": self.valor.obtener(),
            "tipo": self.tipo.obtener(),
            "periodo": self.periodo.obtener(),
        }
        try:
            if self.editando:
                resultado = self.servicio.actualizar_nota(self.nota["id"], datos)
                mensaje = f"Nota de {resultado['valor']} actualizada."
            else:
                resultado = self.servicio.agregar_nota(datos)
                mensaje = (
                    f"Nota registrada: {resultado['valor']} / 100  "
                    f"({self.servicio.nombre_estudiante(resultado['estudiante_id'])}, "
                    f"{self.servicio.codigo_materia(resultado['materia_id'])})"
                )
        except ErrorValidacion as error:
            self.aviso.error(str(error))
            return
        self.valores = {"id": resultado["id"], "mensaje": mensaje}
        self.destroy()


class DialogoContrasena(DialogoBase):
    def __init__(self, master, servicio):
        super().__init__(master, "Cambiar contrasena", ancho=480)
        self.servicio = servicio
        self.titulo(
            "Cambiar mi contrasena",
            "Debes confirmar la contrasena actual para poder entrar en el sistema.",
        )

        marco = tk.Frame(self.cuerpo, bg="#ffffff")
        marco.pack(fill="both", expand=True)

        self.actual = widgets.CampoTexto(marco, "Contrasena actual", tipo="clave", ancho=26)
        self.nueva = widgets.CampoTexto(marco, "Nueva contrasena", tipo="clave", ancho=26, ayuda="Minimo 4 caracteres.")
        self.confirmacion = widgets.CampoTexto(marco, "Confirmar nueva contrasena", tipo="clave", ancho=26)

        for campo in (self.actual, self.nueva, self.confirmacion):
            campo.entrada.bind("<Return>", lambda _e: self.guardar())

        self.actual.enfocar()
        self.aceptar()

    def guardar(self):
        try:
            self.servicio.cambiar_contrasena(
                self.actual.obtener(), self.nueva.obtener(), self.confirmacion.obtener()
            )
        except (ErrorValidacion, ErrorAutenticacion, ErrorPermiso) as error:
            self.aviso.error(str(error))
            return
        self.valores = {"mensaje": "Contrasena actualizada correctamente."}
        self.destroy()