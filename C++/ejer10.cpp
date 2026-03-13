//programa 5 notas con 2 decimales obtener su promedio y mostrar las notas y si el alumno aprobo o no
#include <iostream>
#include <iomanip> // Para usar setprecision
using namespace std;
int main() {
    const int SIZE = 5; // Puedes cambiar este valor para un tamaño diferente
    double notas[SIZE];
    double suma = 0.0;
    double promedio;

    cout << "Ingrese las notas del alumno:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> notas[i];
        suma += notas[i];
    }

    promedio = suma / SIZE;

    cout << fixed << setprecision(2); // Configura la salida para mostrar 2 decimales
    cout << "\nNotas del alumno:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cout << "Nota " << (i + 1) << ": " << notas[i] << endl;
    }
    cout << "Promedio: " << promedio << endl;

    if (promedio >= 60) { // Asumiendo que la nota mínima para aprobar es 60
        cout << "El alumno ha aprobado." << endl;
    } else {
        cout << "El alumno no ha aprobado." << endl;
    }

    return 0;
}