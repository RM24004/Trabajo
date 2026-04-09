import numpy as np
import tkinter as tk
from tkinter import messagebox

def jacobi(A, b, x0, tol=1e-10, max_iterations=100):
    n = len(b)
    x = np.zeros_like(b)
    
    for it_count in range(max_iterations):
        for i in range(n):
            sum1 = np.dot(A[i, :i], x0[:i])
            sum2 = np.dot(A[i, i+1:], x0[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        # Check for convergence
        if np.linalg.norm(x - x0, ord=np.inf) < tol:
            return x, it_count + 1
        
        x0 = x.copy()
    
    return x, max_iterations

def solve_jacobi():
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError("La dimensión debe ser un entero positivo.")
        
        A = np.zeros((n, n))
        b = np.zeros(n)
        
        for i in range(n):
            row = entry_A[i].get().strip().split(',')
            if len(row) != n:
                raise ValueError(f"La fila {i + 1} debe tener {n} valores.")
            A[i] = [float(num) for num in row]
        
        b_row = entry_b.get().strip().split(',')
        if len(b_row) != n:
            raise ValueError(f"El vector b debe tener {n} valores.")
        b = [float(num) for num in b_row]
        
        x0 = np.zeros(n)  # Valor inicial
        solution, iterations = jacobi(A, b, x0)
        
        messagebox.showinfo("Resultado", f"Solución: {solution}\nIteraciones: {iterations}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Método de Jacobi")

# Ingreso de dimensión de la matriz
label_n = tk.Label(root, text="Dimensión de la matriz (n):")
label_n.pack()
entry_n = tk.Entry(root)
entry_n.pack()

# Ingreso de la matriz A
entry_A = []
label_A = tk.Label(root, text="Ingresa la matriz A (filas separadas por Enter, columnas separadas por ','):")
label_A.pack()

def add_row():
    entry = tk.Entry(root)
    entry.pack()
    entry_A.append(entry)

add_row()  # Agregar la primera fila

# Botón para agregar más filas
btn_add_row = tk.Button(root, text="Agregar fila", command=add_row)
btn_add_row.pack()

# Ingreso del vector b
label_b = tk.Label(root, text="Ingresa el vector b (valores separados por ','):")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

# Botón para resolver el sistema
btn_solve = tk.Button(root, text="Resolver", command=solve_jacobi)
btn_solve.pack()

# Ejecutar la aplicación
root.mainloop()