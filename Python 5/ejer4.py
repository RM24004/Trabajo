##crear una clase persona con los atributos nombre, edad y un metodo cumpleaños que incremente la edad en 1 cada vez que se llame.
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")
## Crear un objeto de tipo persona y llamar al método cumpleaños varias veces
persona1 = Persona("Juan", 30)
persona1.cumpleaños()  # Incrementa a 31
persona1.cumpleaños()  # Incrementa a 32
persona1.cumpleaños()  # Incrementa a 33
