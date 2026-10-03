import sys
import tkinter as tk
from tkinter import messagebox

from config import TITULO_APP, VERSION
from interfaz import estilos
from interfaz.vista_docente import VistaDocente
from interfaz.vista_estudiante import VistaEstudiante
from interfaz.vista_login import VistaLogin
from nucleo.almacen import ArchivoInvalido
from nucleo.servicios import Servicio


class Aplicacion:
    def __init__(self):
        self.servicio = Servicio()
        self.raiz = tk.Tk()
        self.raiz.title(f"{TITULO_APP}  v{VERSION}")
        self.raiz.geometry("1180x720")
        self.raiz.minsize(1000, 620)
        self.raiz.configure(bg=estilos.GRIS_FONDO)

        estilos.aplicar_estilos(self.raiz)
        self._icono()

        self.contenedor = tk.Frame(self.raiz, bg=estilos.GRIS_FONDO)
        self.contenedor.pack(fill="both", expand=True)

        self.raiz.protocol("WM_DELETE_WINDOW", self.cerrar)
        self._mostrar_login()

    def _icono(self):
        try:
            self.raiz.iconname(TITULO_APP)
        except tk.TclError:
            pass

    def _limpiar(self):
        for hijo in self.contenedor.winfo_children():
            hijo.destroy()

    def _mostrar_login(self, mensaje=None):
        self._limpiar()
        vista = VistaLogin(self.contenedor, self.servicio, self._al_entrar)
        vista.pack(fill="both", expand=True)
        if mensaje:
            messagebox.showinfo(title="Sesion cerrada", message=mensaje, parent=self.raiz)
        self.raiz.deiconify()

    def _al_entrar(self, sesion):
        self._limpiar()
        if sesion.es_docente:
            VistaDocente(self.contenedor, self.servicio, self._cerrar_sesion).pack(fill="both", expand=True)
        else:
            VistaEstudiante(self.contenedor, self.servicio, self._cerrar_sesion).pack(
                fill="both", expand=True
            )

    def _cerrar_sesion(self):
        if messagebox.askyesno(
            "Cerrar sesion", "Quieres salir de la cuenta actual?", icon="question", parent=self.raiz
        ):
            self.servicio.cerrar_sesion()
            self._mostrar_login("Sesion cerrada correctamente.")

    def cerrar(self):
        self.servicio.cerrar_sesion()
        self.raiz.destroy()

    def ejecutar(self):
        self.raiz.mainloop()

def principal():
    try:
        Aplicacion().ejecutar()
    except ArchivoInvalido as error:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(title="Error de almacenamiento", message=str(error), parent=root)
        root.destroy()
        return 1
    except Exception as error:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(title="Error inesperado", message=f"{type(error).__name__}: {error}", parent=root)
        root.destroy()
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(principal())