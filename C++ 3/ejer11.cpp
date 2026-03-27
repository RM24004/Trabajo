//crear una estructura para almacenar los datos de 3 estudiantes (nombre, edad, promedio), pedirlos al ususario, y mostrar los datos del mejor estudiante
#include <iostream>
#include <string>
using namespace std;
struct Estudiante {
    string nombre;
    int edad;
    float promedio;
};
int main() {
    const int SIZE = 3;
    Estudiante estudiantes[SIZE];

    // Pedir datos de los estudiantes
    for (int i = 0; i < SIZE; i++) {
        cout << "Ingrese el nombre del estudiante " << i + 1 << ": ";
        getline(cin, estudiantes[i].nombre);
        cout << "Ingrese la edad del estudiante " << i + 1 << ": ";
        cin >> estudiantes[i].edad;
        cout << "Ingrese el promedio del estudiante " << i + 1 << ": ";
        cin >> estudiantes[i].promedio;
        cin.ignore(); // Limpiar el buffer de entrada
    }

    // Encontrar al mejor estudiante
    Estudiante mejorEstudiante = estudiantes[0];
    for (int i = 1; i < SIZE; i++) {
        if (estudiantes[i].promedio > mejorEstudiante.promedio) {
            mejorEstudiante = estudiantes[i];
        }
    }

    // Mostrar los datos del mejor estudiante
    cout << "\nEl mejor estudiante es:" << endl;
    cout << "Nombre: " << mejorEstudiante.nombre << endl;
    cout << "Edad: " << mejorEstudiante.edad << endl;
    cout << "Promedio: " << mejorEstudiante.promedio << endl;

    return 0;
}
