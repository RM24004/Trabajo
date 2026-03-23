#calcular el tiempo de llegada a un destino
velocidad = float(input("Ingrese la velocidad en km/h: "))
distancia = float(input("Ingrese la distancia en km: "))
tiempo = distancia / velocidad
horas = int(tiempo)
minutos = int((tiempo - horas) * 60)
print(f"El tiempo estimado de llegada es: {horas} horas y {minutos} minutos.")
