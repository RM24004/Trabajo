import tkinter as tk
from tkinter import messagebox, ttk

from interfaz import estilos, widgets
from interfaz.dialogos import DialogoContrasena
from nucleo.servicios import ErrorPermiso

NOTA_APROBACION = 60


class VistaEstudiante(ttk.Frame):
    def __init__(self, master, servicio, al_cerrar_sesion):
        super().__init__(master, style="TFrame")
        self.servicio = servicio
        self.al_cerrar_sesion = al_cerrar_sesion
        self.id_estudiante = servicio.sesion.estudiante_id

        self._construir_cabecera()
        self._construir_cuerpo()
        self.refrescar()

    def _construir_cabecera(self):
        cabecera = ttk.Frame(self, style="Superior.TFrame")
        cabecera.pack(fill="x")
        interior = ttk.Frame(cabecera, style="Superior.TFrame")
        interior.pack(fill="x", padx=16, pady=10)

        ttk.Label(interior, text="Mis notas", style="Superior.TLabel").pack(side="left")
        ttk.Label(
            interior,
            text=f"Sesion: {self.servicio.sesion}",
            style="SuperiorRol.TLabel",
        ).pack(side="left", padx=14)

        acciones = ttk.Frame(interior, style="Superior.TFrame")
        acciones.pack(side="right")
        ttk.Button(acciones, text="Actualizar", command=self.refrescar).pack(side="left", padx=4)
        ttk.Button(acciones, text="Cambiar contrasena", command=self._cambiar_contrasena).pack(side="left", padx=4)
        ttk.Button(acciones, text="Cerrar sesion", command=self.al_cerrar_sesion).pack(side="left", padx=4)

    def _construir_cuerpo(self):
        self.tarjetas = ttk.Frame(self)
        self.tarjetas.pack(fill="x", padx=12, pady=(12, 0))
        self.tarjeta_promedio = widgets.TarjetaEstadistica(self.tarjetas, "Promedio general")
        self.tarjeta_aprobadas = widgets.TarjetaEstadistica(self.tarjetas, "Notas aprobadas")
        self.tarjeta_reprobadas = widgets.TarjetaEstadistica(self.tarjetas, "Notas reprobadas")
        self.tarjeta_total = widgets.TarjetaEstadistica(self.tarjetas, "Total de notas")

        self.libro = ttk.Notebook(self)
        self.libro.pack(fill="both", expand=True, padx=12, pady=(10, 12))

        self.pestana_detalle = ttk.Frame(self.libro, style="TFrame")
        self.pestana_materias = ttk.Frame(self.libro, style="TFrame")
        self.pestana_perfil = ttk.Frame(self.libro, style="TFrame")
        self.libro.add(self.pestana_detalle, text="  Todas mis notas  ")
        self.libro.add(self.pestana_materias, text="  Por materia  ")
        self.libro.add(self.pestana_perfil, text="  Mi perfil  ")

        marco = ttk.Frame(self.pestana_detalle, style="TFrame")
        marco.pack(fill="both", expand=True)
        self.tabla_notas = widgets.Tabla(
            marco,
            columnas=("materia", "valor", "tipo", "periodo", "fecha", "estado"),
            titulos=("Materia", "Nota", "Tipo", "Periodo", "Fecha", "Estado"),
            anchos=(280, 70, 110, 90, 100, 110),
        )
        self.tabla_notas.arbol.tag_configure("aprobado", background="#eaf7ee")
        self.tabla_notas.arbol.tag_configure("reprobado", background="#fdecea")
        self.resumen_notas = widgets.Aviso(marco)
        self.resumen_notas.label.pack(anchor="w", padx=16, pady=(0, 8))

        marco_materias = ttk.Frame(self.pestana_materias, style="TFrame")
        marco_materias.pack(fill="both", expand=True)
        self.tabla_materias = widgets.Tabla(
            marco_materias,
            columnas=("materia", "promedio", "total", "creditos", "estado"),
            titulos=("Materia", "Promedio", "Notas", "Creditos", "Estado"),
            anchos=(300, 100, 80, 90, 120),
        )
        self.resumen_materias = widgets.Aviso(marco_materias)
        self.resumen_materias.label.pack(anchor="w", padx=16, pady=(0, 8))

        self._construir_perfil()

    def _construir_perfil(self):
        marco = ttk.Frame(self.pestana_perfil, style="TFrame")
        marco.pack(fill="both", expand=True)
        tarjeta = ttk.Labelframe(marco, text="Datos personales", style="Tarjeta.TLabelframe", padding=16)
        tarjeta.pack(fill="x", padx=16, pady=16)

        estudiante = self.servicio.estudiantes.buscar_por_id(self.id_estudiante)
        usuario = next(
            (u for u in self.servicio.usuarios.listar() if u.get("estudiante_id") == self.id_estudiante),
            None,
        )

        campos = []
        if estudiante:
            campos = [
                ("Cedula / Matricula", estudiante["cedula"]),
                ("Nombres", estudiante["nombres"]),
                ("Apellidos", estudiante["apellidos"]),
                ("Carrera", estudiante["carrera"]),
                ("Email", estudiante["email"]),
                ("Telefono", estudiante["telefono"]),
                ("Fecha de registro", estudiante.get("fecha_registro", "-")),
                ("Usuario de acceso", usuario["nombre_usuario"] if usuario else "-"),
            ]
        else:
            campos = [("Aviso", "No se encontro tu ficha de estudiante.")]

        for indice, (etiqueta, valor) in enumerate(campos):
            fila = tk.Frame(tarjeta, bg="#ffffff")
            fila.pack(fill="x", pady=4)
            ttk.Label(fila, text=etiqueta, style="Campo.TLabel", width=22).pack(side="left")
            ttk.Label(fila, text=str(valor), style="Campo.TLabel", foreground="#1f2a33").pack(side="left")
            if indice == 0:
                marco.columnconfigure(0, weight=1)

        nota = tk.Label(
            marco,
            text="Aqui solo puedes consultar tus calificaciones. Para corregirlas, comunicate con tu docente.",
            bg=estilos.GRIS_FONDO,
            fg="#8a8a8a",
            font=("Segoe UI", 9),
        )
        nota.pack(anchor="w", padx=20, pady=(0, 10))

    def refrescar(self):
        if self.servicio.sesion is None:
            return
        if not self.servicio.estudiantes.buscar_por_id(self.id_estudiante):
            messagebox.showwarning(
                title="Ficha no encontrada",
                message="Tu usuario no tiene una ficha de estudiante asociada. Contacta a la secretaria academica.",
                parent=self,
            )

        resumen = self.servicio.resumen_estudiante(self.id_estudiante)
        self.tarjeta_promedio.actualizar(f"{resumen['promedio']:.2f}")
        self.tarjeta_aprobadas.actualizar(resumen["aprobadas"])
        self.tarjeta_reprobadas.actualizar(resumen["reprobadas"])
        self.tarjeta_total.actualizar(resumen["total"])

        notas = self.servicio.notas_de(self.id_estudiante)
        self.tabla_notas.limpiar()
        for nota in notas:
            aprobado = nota["valor"] >= NOTA_APROBACION
            self.tabla_notas.insertar(
                nota["id"],
                (
                    f"{self.servicio.codigo_materia(nota['materia_id'])} - "
                    f"{self.servicio.nombre_materia(nota['materia_id'])}",
                    f"{nota['valor']:g}",
                    nota["tipo"],
                    nota["periodo"],
                    nota.get("fecha", ""),
                    "Aprobado" if aprobado else "Reprobado",
                ),
                etiqueta="aprobado" if aprobado else "reprobado",
            )

        if notas:
            promedios = self.servicio.promedios_por_materia(self.id_estudiante)
            self.resumen_notas.info(
                f"{len(notas)} notas registradas  |  promedio: {resumen['promedio']:.2f}  |  "
                f"aprobadas: {resumen['aprobadas']}  |  reprobadas: {resumen['reprobadas']}"
            )
        else:
            self.resumen_notas.info("Todavia no tienes notas registradas.")

        self.tabla_materias.limpiar()
        promedios = self.servicio.promedios_por_materia(self.id_estudiante)
        for id_materia, info in sorted(
            promedios.items(), key=lambda par: self.servicio.codigo_materia(par[0])
        ):
            materia = self.servicio.materia_por_id(id_materia) or {}
            aprobado = info["promedio"] >= NOTA_APROBACION
            self.tabla_materias.insertar(
                id_materia,
                (
                    f"{self.servicio.codigo_materia(id_materia)} - {self.servicio.nombre_materia(id_materia)}",
                    f"{info['promedio']:.2f}",
                    info["total"],
                    materia.get("creditos", "-"),
                    "Aprobado" if aprobado else "Reprobado",
                ),
            )
        if promedios:
            self.resumen_materias.info(
                f"{len(promedios)} materias con notas registradas. El minimo para aprobar es {NOTA_APROBACION}."
            )
        else:
            self.resumen_materias.info("Aun no hay notas por materia.")

    def _cambiar_contrasena(self):
        resultado = DialogoContrasena(self, self.servicio).mostrar()
        if resultado:
            messagebox.showinfo(title="Listo", message=resultado["mensaje"], parent=self)