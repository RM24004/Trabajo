# renta anual por tramos 
renta = float(input("Ingrese su renta anual: "))

# Tramos de renta y cálculo de retención
if renta <= 487.60:
    print("Tramo: I TRAMO")
    print("Retención: Sin retención")

#Tramo 2 se calcula: (Renta - Exceso) * 10% + Cuota Fija
elif renta <= 642.85:
    print("Tramo: II TRAMO")
    # Calculamos: (Renta - Exceso) * 10% + Cuota Fija
    impuesto = (renta - 487.60) * 0.10 + 17.48
    print(f"Total a pagar: ${impuesto:.2f}")

#Tramo 3 se calcula: (Renta - Exceso) * 10% + Cuota Fija
elif renta <= 915.81:
    print("Tramo: III TRAMO")
    impuesto = (renta - 642.85) * 0.10 + 32.70
    print(f"Total a pagar: ${impuesto:.2f}")

#Tramo 4 se calcula: (Renta - Exceso) * 20% + Cuota Fija
elif renta <= 2058.67:
    print("Tramo: IV TRAMO")
    impuesto = (renta - 915.81) * 0.20 + 60.00
    print(f"Total a pagar: ${impuesto:.2f}")

#Tramo 5 se calcula: (Renta - Exceso) * 30% + Cuota Fija
else:
    print("Tramo: V TRAMO")
    impuesto = (renta - 2058.67) * 0.30 + 288.57
    print(f"Total a pagar: ${impuesto:.2f}")