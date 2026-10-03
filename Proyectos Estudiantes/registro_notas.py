import tkinter as tk
from tkinter import ttk, messagebox


# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Estudiantes")
ventana.geometry("750x500")
ventana.resizable(False, False)


# -----------------------------
# TÍTULO
# -----------------------------

titulo = tk.Label(
    ventana,
    text="REGISTRO DE ESTUDIANTES",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=15)


# -----------------------------
# MARCO DE DATOS
# -----------------------------

marco_datos = tk.Frame(ventana)
marco_datos.pack(pady=10)


# Nombre
tk.Label(
    marco_datos,
    text="Nombre del estudiante:",
    font=("Arial", 11)
).grid(row=0, column=0, padx=10, pady=8)

entrada_nombre = tk.Entry(
    marco_datos,
    width=30,
    font=("Arial", 11)
)
entrada_nombre.grid(row=0, column=1, padx=10, pady=8)


# Nota 1
tk.Label(
    marco_datos,
    text="Nota 1:",
    font=("Arial", 11)
).grid(row=1, column=0, padx=10, pady=8)

entrada_nota1 = tk.Entry(
    marco_datos,
    width=10,
    font=("Arial", 11)
)
entrada_nota1.grid(row=1, column=1, padx=10, pady=8)


# Nota 2
tk.Label(
    marco_datos,
    text="Nota 2:",
    font=("Arial", 11)
).grid(row=2, column=0, padx=10, pady=8)

entrada_nota2 = tk.Entry(
    marco_datos,
    width=10,
    font=("Arial", 11)
)
entrada_nota2.grid(row=2, column=1, padx=10, pady=8)


# Nota 3
tk.Label(
    marco_datos,
    text="Nota 3:",
    font=("Arial", 11)
).grid(row=3, column=0, padx=10, pady=8)

entrada_nota3 = tk.Entry(
    marco_datos,
    width=10,
    font=("Arial", 11)
)
entrada_nota3.grid(row=3, column=1, padx=10, pady=8)


# -----------------------------
# FUNCIÓN PARA GUARDAR
# -----------------------------

def guardar_estudiante():

    nombre = entrada_nombre.get()

    try:
        nota1 = float(entrada_nota1.get())
        nota2 = float(entrada_nota2.get())
        nota3 = float(entrada_nota3.get())

    except ValueError:
        messagebox.showerror(
            "Error",
            "Las notas deben ser números."
        )
        return

    if nombre == "":
        messagebox.showwarning(
            "Advertencia",
            "Escribe el nombre del estudiante."
        )
        return

    if not (0 <= nota1 <= 10 and
            0 <= nota2 <= 10 and
            0 <= nota3 <= 10):

        messagebox.showerror(
            "Error",
            "Las notas deben estar entre 0 y 10."
        )
        return

    promedio = (nota1 + nota2 + nota3) / 3

    tabla.insert(
        "",
        tk.END,
        values=(
            nombre,
            nota1,
            nota2,
            nota3,
            round(promedio, 2)
        )
    )

    limpiar_campos()


# -----------------------------
# FUNCIÓN PARA LIMPIAR
# -----------------------------

def limpiar_campos():

    entrada_nombre.delete(0, tk.END)
    entrada_nota1.delete(0, tk.END)
    entrada_nota2.delete(0, tk.END)
    entrada_nota3.delete(0, tk.END)
    entrada_nombre.focus()

def limpiar_grid(tabla):
    for item in tabla.get_children():
        tabla.delete(item)
# -----------------------------
# BOTONES
# -----------------------------

marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=10)


boton_guardar = tk.Button(
    marco_botones,
    text="Guardar estudiante",
    command=guardar_estudiante,
    width=18
)
boton_guardar.grid(row=0, column=0, padx=5)


boton_limpiar = tk.Button(
    marco_botones,
    text="Limpiar",
    command=limpiar_campos,
    width=12
)
boton_limpiar.grid(row=0, column=1, padx=5)


boton_salir = tk.Button(
    marco_botones,
    text="Salir",
    command=ventana.destroy,
    width=12
)
boton_salir.grid(row=0, column=2, padx=5)

boton_borrar_grid = tk.Button(
    marco_botones,
    text="Borrar Grid",
    command=lambda: limpiar_grid(tabla),
    width=12
)
boton_borrar_grid.grid(row=0, column=3, padx=5)

# -----------------------------
# TABLA
# -----------------------------

columnas = (
    "Nombre",
    "Nota 1",
    "Nota 2",
    "Nota 3",
    "Promedio"
)

tabla = ttk.Treeview(
    ventana,
    columns=columnas,
    show="headings",
    height=8
)

for columna in columnas:
    tabla.heading(columna, text=columna)
    tabla.column(columna, width=130, anchor="center")

tabla.pack(pady=15)


# -----------------------------
# EJECUTAR PROGRAMA
# -----------------------------

ventana.mainloop()
