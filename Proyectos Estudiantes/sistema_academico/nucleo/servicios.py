from __future__ import annotations

import re
import unicodedata
from datetime import date

from config import (
    ARCHIVO_ESTUDIANTES,
    ARCHIVO_MATERIAS,
    ARCHIVO_NOTAS,
    ARCHIVO_USUARIOS,
    CREDITOS_MAXIMOS,
    CREDITOS_MINIMOS,
    NOTA_MAXIMA,
    NOTA_MINIMA,
)
from nucleo import seguridad
from nucleo.almacen import AlmacenJSON

ROLES = ("docente", "estudiante")
CAMPOS_ESTUDIANTE = ("cedula", "nombres", "apellidos", "email", "telefono", "carrera")
CAMPOS_MATERIA = ("codigo", "nombre", "creditos", "semestre", "docente")
CAMPOS_NOTA = ("estudiante_id", "materia_id", "valor", "tipo", "periodo")


class ErrorValidacion(Exception):
    pass


class ErrorAutenticacion(Exception):
    pass


class ErrorPermiso(Exception):
    pass


def _sin_acentos(texto: str) -> str:
    normalizado = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in normalizado if not unicodedata.combining(c))


def _normalizar(texto: str) -> str:
    return re.sub(r"\s+", " ", _sin_acentos(texto or "").strip().lower())


def _validar_texto(valor, campo: str, obligatorio: bool = True, minimo=2, maximo=80) -> str:
    valor = (valor or "").strip()
    if not valor:
        if obligatorio:
            raise ErrorValidacion(f"El campo '{campo}' es obligatorio.")
        return ""
    if len(valor) < minimo:
        raise ErrorValidacion(f"'{campo}' debe tener al menos {minimo} caracteres.")
    if len(valor) > maximo:
        raise ErrorValidacion(f"'{campo}' no puede superar {maximo} caracteres.")
    return valor


def _validar_numero(valor, campo: str, minimo, maximo, decimales=0):
    texto = str(valor if valor is not None else "").strip().replace(",", ".")
    if not texto:
        raise ErrorValidacion(f"El campo '{campo}' es obligatorio.")
    try:
        numero = float(texto)
    except ValueError as exc:
        raise ErrorValidacion(f"'{campo}' debe ser un numero valido.") from exc
    if numero != numero or numero in (float("inf"), float("-inf")):
        raise ErrorValidacion(f"'{campo}' debe ser un numero valido.")
    if not (minimo <= numero <= maximo):
        raise ErrorValidacion(f"'{campo}' debe estar entre {minimo} y {maximo}.")
    return round(numero, decimales) if decimales else int(round(numero))


def _validar_correo(valor) -> str:
    valor = (valor or "").strip()
    if not valor:
        raise ErrorValidacion("El campo 'Email' es obligatorio.")
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", valor):
        raise ErrorValidacion("El email no tiene un formato valido.")
    return valor


def _validar_cedula(valor) -> str:
    valor = re.sub(r"[^0-9A-Za-z-]", "", (valor or "").strip().upper())
    if not valor:
        raise ErrorValidacion("El campo 'Cedula / Matricula' es obligatorio.")
    if len(valor) < 5 or len(valor) > 20:
        raise ErrorValidacion("La cedula debe tener entre 5 y 20 caracteres.")
    return valor


class Sesion:
    def __init__(self, usuario: dict):
        self.id = usuario["id"]
        self.nombre_usuario = usuario["nombre_usuario"]
        self.rol = usuario["rol"]
        self.nombre = usuario.get("nombre", usuario["nombre_usuario"])
        self.estudiante_id = usuario.get("estudiante_id")

    @property
    def es_docente(self) -> bool:
        return self.rol == "docente"

    @property
    def es_estudiante(self) -> bool:
        return self.rol == "estudiante"

    def __str__(self) -> str:
        return f"{self.nombre} ({self.rol})"


class Servicio:
    def __init__(self):
        self.usuarios = AlmacenJSON(ARCHIVO_USUARIOS, "usuarios")
        self.estudiantes = AlmacenJSON(ARCHIVO_ESTUDIANTES, "estudiantes")
        self.materias = AlmacenJSON(ARCHIVO_MATERIAS, "materias")
        self.notas = AlmacenJSON(ARCHIVO_NOTAS, "notas")
        self.sesion: Sesion | None = None
        self._asegurar_admin()

    def _asegurar_admin(self):
        if self.usuarios.listar():
            return
        self.usuarios.agregar(self._crear_usuario("admin", "admin123", "docente", "Docente Principal", None))

    def _crear_usuario(self, nombre_usuario, clave, rol, nombre, estudiante_id) -> dict:
        sal = seguridad.generar_sal()
        return {
            "id": self._nuevo_id(self.usuarios.listar(), "USR"),
            "nombre_usuario": nombre_usuario,
            "sal": sal,
            "clave_hash": seguridad.hashear(clave, sal),
            "rol": rol,
            "nombre": nombre,
            "estudiante_id": estudiante_id,
        }

    @staticmethod
    def _nuevo_id(registros, prefijo: str) -> str:
        mayor = 0
        for registro in registros:
            partes = str(registro.get("id", "")).rsplit("-", 1)
            if len(partes) == 2 and partes[1].isdigit():
                mayor = max(mayor, int(partes[1]))
        return f"{prefijo}-{mayor + 1:04d}"

    def _exigir_docente(self):
        if self.sesion is None:
            raise ErrorPermiso("Debes iniciar sesion.")
        if not self.sesion.es_docente:
            raise ErrorPermiso("Solo los docentes pueden realizar esta accion.")

    def _usuario_por_nombre(self, nombre_usuario):
        objetivo = _normalizar(nombre_usuario)
        for usuario in self.usuarios.listar():
            if _normalizar(usuario.get("nombre_usuario", "")) == objetivo:
                return usuario
        return None

    def _nombre_usuario_disponible(self, nombre_usuario, ignorar_id=None) -> str:
        nombre_usuario = _validar_texto(nombre_usuario, "Usuario", minimo=3, maximo=25)
        if not re.fullmatch(r"[A-Za-z0-9._-]+", nombre_usuario):
            raise ErrorValidacion("El usuario solo admite letras, numeros, punto, guion y guion bajo.")
        if self._usuario_por_nombre(nombre_usuario) is not None:
            existente = self._usuario_por_nombre(nombre_usuario)
            if ignorar_id is None or existente.get("id") != ignorar_id:
                raise ErrorValidacion(f"El usuario '{nombre_usuario}' ya esta registrado.")
        return nombre_usuario

    def iniciar_sesion(self, nombre_usuario: str, clave: str) -> Sesion:
        usuario = self._usuario_por_nombre(nombre_usuario)
        if usuario is None:
            raise ErrorAutenticacion("Usuario o contrasena incorrectos.")
        if not seguridad.verificar(clave or "", usuario.get("sal", ""), usuario.get("clave_hash", "")):
            raise ErrorAutenticacion("Usuario o contrasena incorrectos.")
        self.sesion = Sesion(usuario)
        return self.sesion

    def cerrar_sesion(self):
        self.sesion = None

    def cambiar_contrasena(self, actual: str, nueva: str, confirmacion: str):
        if self.sesion is None:
            raise ErrorPermiso("Debes iniciar sesion.")
        usuario = self.usuarios.buscar_por_id(self.sesion.id)
        if usuario is None:
            raise ErrorAutenticacion("El usuario ya no existe.")
        if not seguridad.verificar(actual or "", usuario.get("sal", ""), usuario.get("clave_hash", "")):
            raise ErrorAutenticacion("La contrasena actual no es correcta.")
        if nueva != confirmacion:
            raise ErrorValidacion("La nueva contrasena no coincide con la confirmacion.")
        if len(nueva or "") < 4:
            raise ErrorValidacion("La nueva contrasena debe tener al menos 4 caracteres.")
        sal = seguridad.generar_sal()
        self.usuarios.actualizar(
            usuario["id"],
            {"sal": sal, "clave_hash": seguridad.hashear(nueva, sal)},
        )

    def _sugerir_usuario(self, nombres: str, apellidos: str) -> str:
        partes = []
        for palabra in (nombres or "").split() + (apellidos or "").split():
            palabra = re.sub(r"[^A-Za-z0-9]", "", palabra)
            if palabra:
                partes.append(palabra[:2].lower())
        base = (".".join(partes[:3])) or "estudiante"
        candidato = base
        sufijo = 1
        while self._usuario_por_nombre(candidato) is not None:
            sufijo += 1
            candidato = f"{base}{sufijo}"
        return candidato

    def cedula_ocupada(self, cedula, ignorar_id=None) -> bool:
        objetivo = cedula.upper()
        for estudiante in self.estudiantes.listar():
            if estudiante.get("cedula", "").upper() == objetivo and estudiante.get("id") != ignorar_id:
                return True
        return False

    def agregar_estudiante(self, datos: dict) -> dict:
        self._exigir_docente()
        cedula = _validar_cedula(datos.get("cedula"))
        if self.cedula_ocupada(cedula):
            raise ErrorValidacion(f"Ya existe un estudiante con la cedula {cedula}.")
        nombres = _validar_texto(datos.get("nombres"), "Nombres", minimo=2, maximo=40)
        apellidos = _validar_texto(datos.get("apellidos"), "Apellidos", minimo=2, maximo=40)
        email = _validar_correo(datos.get("email"))
        telefono = _validar_texto(datos.get("telefono"), "Telefono", minimo=7, maximo=20)
        carrera = _validar_texto(datos.get("carrera"), "Carrera", minimo=3, maximo=60)

        usuario_solicitado = (datos.get("nombre_usuario") or "").strip()
        clave_solicitada = (datos.get("clave") or "").strip()
        if usuario_solicitado:
            nombre_usuario = self._nombre_usuario_disponible(usuario_solicitado)
        else:
            nombre_usuario = self._sugerir_usuario(nombres, apellidos)
        if clave_solicitada:
            if len(clave_solicitada) < 4:
                raise ErrorValidacion("La contrasena debe tener al menos 4 caracteres.")
            clave = clave_solicitada
        else:
            clave = seguridad.generar_clave()

        estudiante = {
            "id": self._nuevo_id(self.estudiantes.listar(), "EST"),
            "cedula": cedula,
            "nombres": nombres,
            "apellidos": apellidos,
            "email": email,
            "telefono": telefono,
            "carrera": carrera,
            "activo": True,
            "fecha_registro": date.today().isoformat(),
        }
        usuario = self._crear_usuario(
            nombre_usuario, clave, "estudiante", f"{nombres} {apellidos}", estudiante["id"]
        )
        self.estudiantes.agregar(estudiante)
        self.usuarios.agregar(usuario)
        return dict(estudiante, nombre_usuario=nombre_usuario, clave=clave)

    def actualizar_estudiante(self, id_estudiante: str, datos: dict) -> dict:
        self._exigir_docente()
        estudiante = self.estudiantes.buscar_por_id(id_estudiante)
        if estudiante is None:
            raise ErrorValidacion("El estudiante ya no existe.")
        cedula = _validar_cedula(datos.get("cedula"))
        if self.cedula_ocupada(cedula, ignorar_id=id_estudiante):
            raise ErrorValidacion(f"Ya existe otro estudiante con la cedula {cedula}.")
        cambios = {
            "cedula": cedula,
            "nombres": _validar_texto(datos.get("nombres"), "Nombres", minimo=2, maximo=40),
            "apellidos": _validar_texto(datos.get("apellidos"), "Apellidos", minimo=2, maximo=40),
            "email": _validar_correo(datos.get("email")),
            "telefono": _validar_texto(datos.get("telefono"), "Telefono", minimo=7, maximo=20),
            "carrera": _validar_texto(datos.get("carrera"), "Carrera", minimo=3, maximo=60),
        }
        actualizado = self.estudiantes.actualizar(id_estudiante, cambios)
        usuario = self._usuario_del_estudiante(id_estudiante)
        if usuario is not None:
            self.usuarios.actualizar(
                usuario["id"],
                {"nombre": f"{cambios['nombres']} {cambios['apellidos']}"},
            )
        return actualizado

    def eliminar_estudiante(self, id_estudiante: str):
        self._exigir_docente()
        usuario = self._usuario_del_estudiante(id_estudiante)
        notas = [n for n in self.notas.listar() if n.get("estudiante_id") == id_estudiante]
        if usuario is not None:
            self.usuarios.eliminar(usuario["id"])
        self.notas.eliminar_varios({n["id"] for n in notas})
        self.estudiantes.eliminar(id_estudiante)
        return len(notas)

    def _usuario_del_estudiante(self, id_estudiante):
        for usuario in self.usuarios.listar():
            if usuario.get("estudiante_id") == id_estudiante:
                return usuario
        return None

    def restablecer_clave_estudiante(self, id_estudiante: str):
        self._exigir_docente()
        usuario = self._usuario_del_estudiante(id_estudiante)
        if usuario is None:
            raise ErrorValidacion("El estudiante no tiene un usuario asignado.")
        clave = seguridad.generar_clave()
        sal = seguridad.generar_sal()
        self.usuarios.actualizar(
            usuario["id"], {"sal": sal, "clave_hash": seguridad.hashear(clave, sal)}
        )
        return clave

    def codigo_materia_ocupado(self, codigo, ignorar_id=None) -> bool:
        objetivo = _normalizar(codigo)
        for materia in self.materias.listar():
            if _normalizar(materia.get("codigo", "")) == objetivo and materia.get("id") != ignorar_id:
                return True
        return False

    def agregar_materia(self, datos: dict) -> dict:
        self._exigir_docente()
        codigo = _validar_texto(datos.get("codigo"), "Codigo", minimo=3, maximo=15)
        if self.codigo_materia_ocupado(codigo):
            raise ErrorValidacion(f"Ya existe una materia con el codigo {codigo}.")
        materia = {
            "id": self._nuevo_id(self.materias.listar(), "MAT"),
            "codigo": codigo.upper(),
            "nombre": _validar_texto(datos.get("nombre"), "Nombre de la materia", minimo=3, maximo=70),
            "creditos": _validar_numero(datos.get("creditos"), "Creditos", CREDITOS_MINIMOS, CREDITOS_MAXIMOS),
            "semestre": _validar_numero(datos.get("semestre"), "Semestre", 1, 12),
            "docente": self.sesion.nombre if self.sesion else _validar_texto(datos.get("docente"), "Docente"),
        }
        return self.materias.agregar(materia)

    def actualizar_materia(self, id_materia: str, datos: dict) -> dict:
        self._exigir_docente()
        if self.materias.buscar_por_id(id_materia) is None:
            raise ErrorValidacion("La materia ya no existe.")
        codigo = _validar_texto(datos.get("codigo"), "Codigo", minimo=3, maximo=15)
        if self.codigo_materia_ocupado(codigo, ignorar_id=id_materia):
            raise ErrorValidacion(f"Ya existe otra materia con el codigo {codigo}.")
        cambios = {
            "codigo": codigo.upper(),
            "nombre": _validar_texto(datos.get("nombre"), "Nombre de la materia", minimo=3, maximo=70),
            "creditos": _validar_numero(datos.get("creditos"), "Creditos", CREDITOS_MINIMOS, CREDITOS_MAXIMOS),
            "semestre": _validar_numero(datos.get("semestre"), "Semestre", 1, 12),
        }
        return self.materias.actualizar(id_materia, cambios)

    def eliminar_materia(self, id_materia: str):
        self._exigir_docente()
        notas = [n for n in self.notas.listar() if n.get("materia_id") == id_materia]
        self.notas.eliminar_varios({n["id"] for n in notas})
        self.materias.eliminar(id_materia)
        return len(notas)

    def agregar_nota(self, datos: dict) -> dict:
        self._exigir_docente()
        estudiante = self.estudiantes.buscar_por_id(datos.get("estudiante_id"))
        if estudiante is None:
            raise ErrorValidacion("Selecciona un estudiante valido.")
        materia = self.materias.buscar_por_id(datos.get("materia_id"))
        if materia is None:
            raise ErrorValidacion("Selecciona una materia valida.")
        nota = {
            "id": self._nuevo_id(self.notas.listar(), "NOT"),
            "estudiante_id": estudiante["id"],
            "materia_id": materia["id"],
            "valor": _validar_numero(datos.get("valor"), "Nota", NOTA_MINIMA, NOTA_MAXIMA, decimales=2),
            "tipo": _validar_texto(datos.get("tipo"), "Tipo de nota", minimo=3, maximo=30),
            "periodo": _validar_texto(datos.get("periodo"), "Periodo", minimo=4, maximo=20),
            "fecha": date.today().isoformat(),
        }
        return self.notas.agregar(nota)

    def actualizar_nota(self, id_nota: str, datos: dict) -> dict:
        self._exigir_docente()
        nota = self.notas.buscar_por_id(id_nota)
        if nota is None:
            raise ErrorValidacion("La nota ya no existe.")
        cambios = {
            "valor": _validar_numero(datos.get("valor"), "Nota", NOTA_MINIMA, NOTA_MAXIMA, decimales=2),
            "tipo": _validar_texto(datos.get("tipo"), "Tipo de nota", minimo=3, maximo=30),
            "periodo": _validar_texto(datos.get("periodo"), "Periodo", minimo=4, maximo=20),
        }
        if datos.get("estudiante_id"):
            if self.estudiantes.buscar_por_id(datos["estudiante_id"]) is None:
                raise ErrorValidacion("Selecciona un estudiante valido.")
            cambios["estudiante_id"] = datos["estudiante_id"]
        if datos.get("materia_id"):
            if self.materias.buscar_por_id(datos["materia_id"]) is None:
                raise ErrorValidacion("Selecciona una materia valida.")
            cambios["materia_id"] = datos["materia_id"]
        return self.notas.actualizar(id_nota, cambios)

    def eliminar_nota(self, id_nota: str) -> bool:
        self._exigir_docente()
        return self.notas.eliminar(id_nota)

    def nombre_estudiante(self, id_estudiante) -> str:
        estudiante = self.estudiantes.buscar_por_id(id_estudiante)
        if estudiante is None:
            return "(eliminado)"
        return f"{estudiante['nombres']} {estudiante['apellidos']}"

    def materia_por_id(self, id_materia):
        return self.materias.buscar_por_id(id_materia)

    def codigo_materia(self, id_materia) -> str:
        materia = self.materias.buscar_por_id(id_materia)
        return materia["codigo"] if materia else "(eliminada)"

    def nombre_materia(self, id_materia) -> str:
        materia = self.materias.buscar_por_id(id_materia)
        return materia["nombre"] if materia else "(materia eliminada)"

    def notas_de(self, id_estudiante):
        registros = [n for n in self.notas.listar() if n.get("estudiante_id") == id_estudiante]
        return sorted(registros, key=lambda n: (n.get("periodo", ""), n.get("materia_id", ""), n.get("id", "")))

    def resumen_estudiante(self, id_estudiante) -> dict:
        notas = self.notas_de(id_estudiante)
        if not notas:
            return {"promedio": 0.0, "aprobadas": 0, "reprobadas": 0, "total": 0}
        valores = [n["valor"] for n in notas]
        return {
            "promedio": round(sum(valores) / len(valores), 2),
            "aprobadas": sum(1 for v in valores if v >= 60),
            "reprobadas": sum(1 for v in valores if v < 60),
            "total": len(valores),
        }

    def promedios_por_materia(self, id_estudiante):
        agrupado = {}
        for nota in self.notas_de(id_estudiante):
            agrupado.setdefault(nota["materia_id"], []).append(nota["valor"])
        return {
            id_materia: {
                "promedio": round(sum(valores) / len(valores), 2),
                "total": len(valores),
            }
            for id_materia, valores in agrupado.items()
        }

    def indice_por_id(self, almacen, clave="id"):
        return {registro.get(clave): registro for registro in almacen.listar()}

    def estadisticas_generales(self) -> dict:
        estudiantes = self.estudiantes.listar()
        notas = self.notas.listar()
        valores = [n["valor"] for n in notas]
        return {
            "estudiantes": len(estudiantes),
            "materias": len(self.materias.listar()),
            "notas": len(notas),
            "promedio_general": round(sum(valores) / len(valores), 2) if valores else 0.0,
            "aprobadas": sum(1 for v in valores if v >= 60),
            "reprobadas": sum(1 for v in valores if v < 60),
        }