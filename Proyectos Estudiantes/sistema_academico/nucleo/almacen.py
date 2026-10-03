import json
import os
import tempfile
import threading
from pathlib import Path


class ArchivoInvalido(Exception):
    pass


class AlmacenJSON:
    def __init__(self, ruta, etiqueta: str = "registros"):
        self.ruta = Path(ruta)
        self.etiqueta = etiqueta
        self._candado = threading.Lock()
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        if not self.ruta.exists():
            self._escribir([])

    def _leer(self):
        try:
            contenido = self.ruta.read_text(encoding="utf-8").strip()
        except OSError as exc:
            raise ArchivoInvalido(f"No se pudo leer '{self.ruta.name}': {exc}") from exc
        if not contenido:
            return []
        try:
            datos = json.loads(contenido)
        except json.JSONDecodeError as exc:
            raise ArchivoInvalido(
                f"'{self.ruta.name}' esta danado. Corrigelo o eliminalo para regenerarlo."
            ) from exc
        if not isinstance(datos, list):
            raise ArchivoInvalido(f"'{self.ruta.name}' debe contener una lista.")
        return [item for item in datos if isinstance(item, dict)]

    def _escribir(self, registros):
        carpeta = self.ruta.parent
        temporal = None
        try:
            with tempfile.NamedTemporaryFile(
                "w",
                encoding="utf-8",
                dir=carpeta,
                delete=False,
                suffix=".tmp",
            ) as archivo:
                json.dump(registros, archivo, indent=2, ensure_ascii=False)
                temporal = archivo.name
            os.replace(temporal, self.ruta)
        except OSError as exc:
            if temporal and os.path.exists(temporal):
                os.unlink(temporal)
            raise ArchivoInvalido(f"No se pudo guardar '{self.ruta.name}': {exc}") from exc

    def listar(self):
        with self._candado:
            return self._leer()

    def buscar_por_id(self, id_registro):
        for registro in self.listar():
            if registro.get("id") == id_registro:
                return registro
        return None

    def guardar(self, registros):
        with self._candado:
            self._escribir(registros)

    def agregar(self, registro):
        with self._candado:
            registros = self._leer()
            registros.append(registro)
            self._escribir(registros)
        return registro

    def actualizar(self, id_registro, cambios):
        with self._candado:
            registros = self._leer()
            for indice, registro in enumerate(registros):
                if registro.get("id") == id_registro:
                    actualizado = dict(registro)
                    actualizado.update(cambios)
                    registros[indice] = actualizado
                    self._escribir(registros)
                    return actualizado
        return None

    def eliminar(self, id_registro):
        with self._candado:
            registros = self._leer()
            restantes = [r for r in registros if r.get("id") != id_registro]
            if len(restantes) == len(registros):
                return False
            self._escribir(restantes)
        return True

    def eliminar_varios(self, ids):
        ids = set(ids)
        with self._candado:
            registros = self._leer()
            restantes = [r for r in registros if r.get("id") not in ids]
            self._escribir(restantes)
        return len(registros) - len(restantes)