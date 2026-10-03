import tkinter as tk
from tkinter import messagebox, ttk

from interfaz import estilos, widgets
from interfaz.dialogos import DialogoContrasena, DialogoEstudiante, DialogoMateria, DialogoNota
from nucleo.servicios import ErrorPermiso, ErrorValidacion

NOTA_APROBACION = 60


class VistaDocente(ttk.Frame):
    def __init__(self, master, servicio, al_cerrar_sesion):
        super().__init__(master, style="TFrame")
        self.servicio = servicio
        self.al_cerrar_sesion = al_cerrar_sesion

        self.filtro_estudiantes_var = tk.StringVar()
        self.filtro_materias_var = tk.StringVar()
        self.filtro_notas_var = tk.StringVar()

        self._construir_cabecera()
        self._construir_cuerpo()

        self.filtro_estudiantes_var.trace_add("write", lambda *_: self._cargar_estudiantes())
        self.filtro_materias_var.trace_add("write", lambda *_: self._cargar_materias())
        self.filtro_notas_var.trace_add("write", lambda *_: self._cargar_notas())

        self.refrescar_todo()

    def _construir_cabecera(self):
        cabecera = ttk.Frame(self, style="Superior.TFrame")
        cabecera.pack(fill="x")
        interior = ttk.Frame(cabecera, style="Superior.TFrame")
        interior.pack(fill="x", padx=16, pady=10)

        ttk.Label(interior, text="Panel del docente", style="Superior.TLabel").pack(side="left")
        ttk.Label(
            interior,
            text=f"Sesion: {self.servicio.sesion}",
            style="SuperiorRol.TLabel",
        ).pack(side="left", padx=14)

        acciones = ttk.Frame(interior, style="Superior.TFrame")
        acciones.pack(side="right")
        ttk.Button(acciones, text="Cambiar contrasena", command=self._cambiar_contrasena).pack(side="left", padx=4)
        ttk.Button(acciones, text="Cerrar sesion", command=self.al_cerrar_sesion).pack(side="left", padx=4)

    def _construir_cuerpo(self):
        self.tarjetas = ttk.Frame(self)
        self.tarjetas.pack(fill="x", padx=12, pady=(12, 0))
        self.tarjeta_estudiantes = widgets.TarjetaEstadistica(self.tarjetas, "Estudiantes")
        self.tarjeta_materias = widgets.TarjetaEstadistica(self.tarjetas, "Materias")
        self.tarjeta_notas = widgets.TarjetaEstadistica(self.tarjetas, "Notas registradas")
        self.tarjeta_promedio = widgets.TarjetaEstadistica(self.tarjetas, "Promedio general")

        self.libro = ttk.Notebook(self)
        self.libro.pack(fill="both", expand=True, padx=12, pady=(10, 12))

        self.pestana_estudiantes = self._crear_pestana_estudiantes()
        self.pestana_materias = self._crear_pestana_materias()
        self.pestana_notas = self._crear_pestana_notas()

    def _crear_pestana_estudiantes(self):
        marco = ttk.Frame(self.libro, style="TFrame")
        self.libro.add(marco, text="  Estudiantes  ")

        barra = ttk.Frame(marco)
        barra.pack(fill="x", padx=12, pady=(12, 4))
        ttk.Label(barra, text="Buscar:").pack(side="left")
        ttk.Entry(barra, textvariable=self.filtro_estudiantes_var, width=34, style="Buscador.TEntry").pack(
            side="left", padx=6
        )
        ttk.Button(barra, text="Limpiar", command=lambda: self.filtro_estudiantes_var.set("")).pack(side="left")

        acciones = ttk.Frame(barra)
        acciones.pack(side="right")
        ttk.Button(acciones, text="+ Nuevo estudiante", command=self._nuevo_estudiante).pack(side="left", padx=4)
        ttk.Button(acciones, text="Editar", command=self._editar_estudiante).pack(side="left", padx=4)
        ttk.Button(acciones, text="Ver notas", command=self._ver_notas_estudiante).pack(side="left", padx=4)
        ttk.Button(
            acciones, text="Restablecer clave", command=self._restablecer_clave
        ).pack(side="left", padx=4)
        ttk.Button(acciones, text="Eliminar", style="Peligro.TButton", command=self._eliminar_estudiante).pack(
            side="left", padx=4
        )

        self.tabla_estudiantes = widgets.Tabla(
            marco,
            columnas=("cedula", "nombres", "carrera", "email", "telefono", "usuario"),
            titulos=("Cedula", "Estudiante", "Carrera", "Email", "Telefono", "Usuario"),
            anchos=(110, 200, 200, 190, 110, 110),
            on_doble_clic=lambda _id: self._editar_estudiante(),
        )
        self.resumen_estudiantes = widgets.Aviso(marco)
        self.resumen_estudiantes.label.pack(anchor="w", padx=16, pady=(0, 8))
        return marco

    def _crear_pestana_materias(self):
        marco = ttk.Frame(self.libro, style="TFrame")
        self.libro.add(marco, text="  Materias  ")

        barra = ttk.Frame(marco)
        barra.pack(fill="x", padx=12, pady=(12, 4))
        ttk.Label(barra, text="Buscar:").pack(side="left")
        ttk.Entry(barra, textvariable=self.filtro_materias_var, width=34, style="Buscador.TEntry").pack(
            side="left", padx=6
        )
        ttk.Button(barra, text="Limpiar", command=lambda: self.filtro_materias_var.set("")).pack(side="left")

        acciones = ttk.Frame(barra)
        acciones.pack(side="right")
        ttk.Button(acciones, text="+ Nueva materia", command=self._nueva_materia).pack(side="left", padx=4)
        ttk.Button(acciones, text="Editar", command=self._editar_materia).pack(side="left", padx=4)
        ttk.Button(acciones, text="Eliminar", style="Peligro.TButton", command=self._eliminar_materia).pack(
            side="left", padx=4
        )

        self.tabla_materias = widgets.Tabla(
            marco,
            columnas=("codigo", "nombre", "creditos", "semestre", "docente", "inscritos"),
            titulos=("Codigo", "Materia", "Creditos", "Semestre", "Docente", "Notas"),
            anchos=(100, 300, 80, 80, 200, 70),
            on_doble_clic=lambda _id: self._editar_materia(),
        )
        return marco

    def _crear_pestana_notas(self):
        marco = ttk.Frame(self.libro, style="TFrame")
        self.libro.add(marco, text="  Notas  ")

        barra = ttk.Frame(marco)
        barra.pack(fill="x", padx=12, pady=(12, 4))
        ttk.Label(barra, text="Buscar:").pack(side="left")
        ttk.Entry(barra, textvariable=self.filtro_notas_var, width=30, style="Buscador.TEntry").pack(
            side="left", padx=6
        )
        ttk.Button(barra, text="Limpiar", command=lambda: self.filtro_notas_var.set("")).pack(side="left")

        acciones = ttk.Frame(barra)
        acciones.pack(side="right")
        ttk.Button(acciones, text="+ Nueva nota", command=self._nueva_nota).pack(side="left", padx=4)
        ttk.Button(acciones, text="Editar", command=self._editar_nota).pack(side="left", padx=4)
        ttk.Button(acciones, text="Eliminar", style="Peligro.TButton", command=self._eliminar_nota).pack(
            side="left", padx=4
        )

        self.tabla_notas = widgets.Tabla(
            marco,
            columnas=("estudiante", "materia", "valor", "tipo", "periodo", "fecha"),
            titulos=("Estudiante", "Materia", "Nota", "Tipo", "Periodo", "Fecha"),
            anchos=(220, 260, 70, 110, 90, 100),
            on_doble_clic=lambda _id: self._editar_nota(),
        )
        self.tabla_notas.arbol.tag_configure("aprobado", background="#eaf7ee")
        self.tabla_notas.arbol.tag_configure("reprobado", background="#fdecea")
        self.resumen_notas = widgets.Aviso(marco)
        self.resumen_notas.label.pack(anchor="w", padx=16, pady=(0, 8))
        return marco

    def refrescar_todo(self):
        if self.servicio.sesion is None:
            return
        try:
            estadisticas = self.servicio.estadisticas_generales()
        except Exception as error:
            messagebox.showerror(title="Error de datos", message=str(error), parent=self)
            return
        self.tarjeta_estudiantes.actualizar(estadisticas["estudiantes"])
        self.tarjeta_materias.actualizar(estadisticas["materias"])
        self.tarjeta_notas.actualizar(estadisticas["notas"])
        self.tarjeta_promedio.actualizar(f"{estadisticas['promedio_general']:.2f}")
        self._cargar_estudiantes()
        self._cargar_materias()
        self._cargar_notas()

    @staticmethod
    def _coincide(filtro, *campos):
        filtro = filtro.strip().lower()
        if not filtro:
            return True
        return any(filtro in str(campo or "").lower() for campo in campos)

    def _cargar_estudiantes(self):
        if not hasattr(self, "tabla_estudiantes"):
            return
        filtro = self.filtro_estudiantes_var.get() if hasattr(self, "filtro_estudiantes_var") else ""
        self.tabla_estudiantes.limpiar()
        visibles = 0
        estudiantes = [
            e
            for e in self.servicio.estudiantes.listar()
            if all(clave in e for clave in ("id", "cedula", "nombres", "apellidos"))
        ]
        for estudiante in sorted(estudiantes, key=lambda e: (e["apellidos"], e["nombres"])):
            if not self._coincide(
                filtro,
                estudiante["cedula"],
                estudiante["nombres"],
                estudiante["apellidos"],
                estudiante.get("carrera", ""),
                estudiante.get("email", ""),
            ):
                continue
            usuario = next(
                (u for u in self.servicio.usuarios.listar() if u.get("estudiante_id") == estudiante["id"]),
                None,
            )
            self.tabla_estudiantes.insertar(
                estudiante["id"],
                (
                    estudiante["cedula"],
                    f"{estudiante['nombres']} {estudiante['apellidos']}",
                    estudiante.get("carrera", "-"),
                    estudiante.get("email", "-"),
                    estudiante.get("telefono", "-"),
                    usuario["nombre_usuario"] if usuario else "-",
                ),
            )
            visibles += 1
        total = len(estudiantes)
        self.resumen_estudiantes.info(f"Mostrando {visibles} de {total} estudiantes registrados.")

    def _cargar_materias(self):
        if not hasattr(self, "tabla_materias"):
            return
        filtro = self.filtro_materias_var.get() if hasattr(self, "filtro_materias_var") else ""
        self.tabla_materias.limpiar()
        conteo = {}
        for nota in self.servicio.notas.listar():
            clave = nota.get("materia_id")
            if clave:
                conteo[clave] = conteo.get(clave, 0) + 1
        materias = [m for m in self.servicio.materias.listar() if "id" in m and "codigo" in m]
        for materia in sorted(materias, key=lambda m: m["codigo"]):
            if not self._coincide(
                filtro, materia.get("codigo", ""), materia.get("nombre", ""), materia.get("docente", "")
            ):
                continue
            self.tabla_materias.insertar(
                materia["id"],
                (
                    materia.get("codigo", "-"),
                    materia.get("nombre", "(sin nombre)"),
                    materia.get("creditos", "-"),
                    materia.get("semestre", "-"),
                    materia.get("docente") or "-",
                    conteo.get(materia["id"], 0),
                ),
            )

    def _cargar_notas(self):
        if not hasattr(self, "tabla_notas"):
            return
        filtro = self.filtro_notas_var.get() if hasattr(self, "filtro_notas_var") else ""
        self.tabla_notas.limpiar()
        if not hasattr(self, "filtro_notas_var"):
            return
        notas = [
            nota
            for nota in self.servicio.notas.listar()
            if all(clave in nota for clave in ("id", "estudiante_id", "materia_id", "valor"))
        ]
        notas = sorted(
            notas,
            key=lambda n: (n.get("periodo", ""), n.get("fecha", ""), n["id"]),
            reverse=True,
        )
        aprobadas = reprobadas = 0
        visibles = 0
        for nota in notas:
            estudiante = self.servicio.nombre_estudiante(nota["estudiante_id"])
            codigo = self.servicio.codigo_materia(nota["materia_id"])
            materia = self.servicio.nombre_materia(nota["materia_id"])
            if not self._coincide(filtro, estudiante, materia, codigo, nota["tipo"], nota["periodo"], nota["valor"]):
                continue
            aprobado = nota["valor"] >= NOTA_APROBACION
            aprobadas += aprobado
            reprobadas += not aprobado
            self.tabla_notas.insertar(
                nota["id"],
                (
                    estudiante,
                    f"{codigo} - {materia}",
                    f"{nota['valor']:g}",
                    nota["tipo"],
                    nota["periodo"],
                    nota.get("fecha", ""),
                ),
                etiqueta="aprobado" if aprobado else "reprobado",
            )
            visibles += 1
        if visibles:
            promedio = sum(n["valor"] for n in notas) / len(notas)
            self.resumen_notas.info(
                f"{visibles} notas visibles  |  promedio general: {promedio:.2f}  |  "
                f"aprobadas: {aprobadas}  |  reprobadas: {reprobadas}"
            )
        else:
            self.resumen_notas.info("No hay notas registradas todavia.")

    def _seleccion(self, tabla, entidad):
        id_registro = tabla.id_seleccionada()
        if not id_registro:
            messagebox.showinfo(title="Selecciona un registro", message=f"Primero selecciona {entidad} en la tabla.", parent=self)
        return id_registro

    def _nuevo_estudiante(self):
        resultado = DialogoEstudiante(self, self.servicio).mostrar()
        if resultado:
            self.refrescar_todo()
            self.tabla_estudiantes.resaltado_si_existe(resultado["id"])
            self.resumen_estudiantes.exito(resultado["mensaje"].splitlines()[0])

    def _editar_estudiante(self):
        id_registro = self._seleccion(self.tabla_estudiantes, "un estudiante")
        if not id_registro:
            return
        estudiante = self.servicio.estudiantes.buscar_por_id(id_registro)
        if estudiante is None:
            return
        resultado = DialogoEstudiante(self, self.servicio, estudiante).mostrar()
        if resultado:
            self.refrescar_todo()
            self.tabla_estudiantes.resaltado_si_existe(id_registro)
            self.resumen_estudiantes.exito(resultado["mensaje"])

    def _eliminar_estudiante(self):
        id_registro = self._seleccion(self.tabla_estudiantes, "un estudiante")
        if not id_registro:
            return
        estudiante = self.servicio.estudiantes.buscar_por_id(id_registro)
        if estudiante is None:
            return
        notas = self.servicio.notas_de(id_registro)
        detalle = (
            f"\n\nTambien se eliminaran sus {len(notas)} notas registradas."
            if notas
            else "\n\nNo tiene notas registradas."
        )
        if not messagebox.askyesno(
            "Confirmar borrado",
            f"Eliminar a {estudiante['nombres']} {estudiante['apellidos']} y su usuario de acceso?{detalle}",
            icon="warning",
            parent=self,
        ):
            return
        try:
            self.servicio.eliminar_estudiante(id_registro)
        except ErrorPermiso as error:
            messagebox.showerror(title="Sin permisos", message=str(error), parent=self)
            return
        self.refrescar_todo()
        self.resumen_estudiantes.exito("Estudiante eliminado.")

    def _restablecer_clave(self):
        id_registro = self._seleccion(self.tabla_estudiantes, "un estudiante")
        if not id_registro:
            return
        estudiante = self.servicio.estudiantes.buscar_por_id(id_registro)
        if estudiante is None:
            return
        if not messagebox.askyesno(
            "Restablecer contrasena",
            f"Generar una nueva contrasena para {estudiante['nombres']} {estudiante['apellidos']}?",
            parent=self,
        ):
            return
        try:
            clave = self.servicio.restablecer_clave_estudiante(id_registro)
        except (ErrorPermiso, ErrorValidacion) as error:
            messagebox.showerror(title="No se pudo restablecer", message=str(error), parent=self)
            return
        messagebox.showinfo(
            title="Nueva contrasena",
            message=f"Usuario: {estudiante['nombres']}\nContrasena nueva: {clave}\n\nAnotala, no volvera a mostrarse.",
            parent=self,
        )

    def _ver_notas_estudiante(self):
        id_registro = self._seleccion(self.tabla_estudiantes, "un estudiante")
        if not id_registro:
            return
        self.refrescar_todo()
        self.filtro_notas_var.set(self.servicio.nombre_estudiante(id_registro))
        self.libro.select(self.pestana_notas)
        self._cargar_notas()

    def _nueva_materia(self):
        resultado = DialogoMateria(self, self.servicio).mostrar()
        if resultado:
            self.refrescar_todo()
            self.tabla_materias.resaltado_si_existe(resultado["id"])

    def _editar_materia(self):
        id_registro = self._seleccion(self.tabla_materias, "una materia")
        if not id_registro:
            return
        materia = self.servicio.materias.buscar_por_id(id_registro)
        if materia is None:
            return
        if DialogoMateria(self, self.servicio, materia).mostrar():
            self.refrescar_todo()
            self.tabla_materias.resaltado_si_existe(id_registro)

    def _eliminar_materia(self):
        id_registro = self._seleccion(self.tabla_materias, "una materia")
        if not id_registro:
            return
        materia = self.servicio.materias.buscar_por_id(id_registro)
        if materia is None:
            return
        notas = [n for n in self.servicio.notas.listar() if n["materia_id"] == id_registro]
        detalle = f"\n\nTambien se eliminaran sus {len(notas)} notas." if notas else ""
        if not messagebox.askyesno(
            "Confirmar borrado",
            f"Eliminar la materia {materia['codigo']} - {materia['nombre']}?{detalle}",
            icon="warning",
            parent=self,
        ):
            return
        try:
            self.servicio.eliminar_materia(id_registro)
        except ErrorPermiso as error:
            messagebox.showerror(title="Sin permisos", message=str(error), parent=self)
            return
        self.refrescar_todo()

    def _nueva_nota(self):
        if not self.servicio.estudiantes.listar() or not self.servicio.materias.listar():
            messagebox.showwarning(
                title="Faltan datos",
                message="Necesitas al menos un estudiante y una materia registrados para poder capturar notas.",
                parent=self,
            )
            return
        resultado = DialogoNota(self, self.servicio).mostrar()
        if resultado:
            self.refrescar_todo()
            self.tabla_notas.resaltado_si_existe(resultado["id"])
            self.resumen_notas.exito(resultado["mensaje"])

    def _editar_nota(self):
        id_registro = self._seleccion(self.tabla_notas, "una nota")
        if not id_registro:
            return
        nota = self.servicio.notas.buscar_por_id(id_registro)
        if nota is None:
            return
        if DialogoNota(self, self.servicio, nota=nota).mostrar():
            self.refrescar_todo()
            self.tabla_notas.resaltado_si_existe(id_registro)

    def _eliminar_nota(self):
        id_registro = self._seleccion(self.tabla_notas, "una nota")
        if not id_registro:
            return
        nota = self.servicio.notas.buscar_por_id(id_registro)
        if nota is None:
            return
        if not messagebox.askyesno(
            "Confirmar borrado",
            f"Eliminar la nota de {self.servicio.nombre_estudiante(nota['estudiante_id'])} "
            f"en {self.servicio.codigo_materia(nota['materia_id'])} ({nota['valor']:g})?",
            icon="warning",
            parent=self,
        ):
            return
        try:
            self.servicio.eliminar_nota(id_registro)
        except ErrorPermiso as error:
            messagebox.showerror(title="Sin permisos", message=str(error), parent=self)
            return
        self.refrescar_todo()
        self.resumen_notas.exito("Nota eliminada.")

    def _cambiar_contrasena(self):
        resultado = DialogoContrasena(self, self.servicio).mostrar()
        if resultado:
            messagebox.showinfo(title="Listo", message=resultado["mensaje"], parent=self)