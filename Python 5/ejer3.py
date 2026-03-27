##crear una clase persona y utilizarla para crear objetos de tipo persona con atributos como nombre, edad y género. Luego, implementar un método para mostrar la información de la persona.
class Persona:
    def __init__(self, nombre: str, edad: int, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")
        
## Crear objetos de tipo persona y mostrar su información

persona1 = Persona("Juan", 30, "Masculino")
persona2 = Persona("María", 25, "Femenino")
persona1.mostrar_informacion()
print()  # Línea en blanco para separar la información
persona2.mostrar_informacion()
